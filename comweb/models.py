from django.db import models

class MachineMode(models.Model):
    AB = models.CharField(max_length=100) # abbreviation
    NA = models.CharField(max_length=100) # name 
    SO = models.IntegerField() # sort order
    class Meta: 
        ordering = ['SO']

class MachineType(models.Model):
    AB = models.CharField(max_length=100) 
    NA = models.CharField(max_length=100)  
    SO = models.IntegerField() 
    class Meta:
        ordering = ['SO']

class Machine(models.Model):
    AB = models.CharField(max_length=100) 
    NA = models.CharField(max_length=100) 
    SO = models.IntegerField()

    # if a Mode instance is deleted, all related objects (instances of the current mode) will also be deleted.
    mode = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='machines')
    type = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='machines') 
    class Meta: 
        ordering = ['SO']

class ProblemType(models.Model):
    NA = models.CharField(max_length=100)
    SO = models.IntegerField() 
    order = models.IntegerField() # order of the problem type compared to other problem types
    class Meta:
        ordering = ['SO']

class ResourceBound(models.Model):
    NA = models.CharField(max_length=100) 
    AB = models.CharField(max_length=100) 
    SO = models.IntegerField() 
    order = models.IntegerField() # order of the bound compared to other bounds
    class Meta:
        ordering = ['SO']

def get_infinite_bound():
    return ResourceBound.objects.get(AB='inf')

class Class(models.Model):
    NA = models.CharField(max_length=100) 
    AB = models.CharField(max_length=100)
    problem_type = models.ForeignKey(ProblemType, on_delete=models.CASCADE, related_name='classes')   
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='classes')
    co = models.BooleanField(default=False)  # is this a co-complexity class?
    co_class = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='co_classes')
    time_bound = models.ForeignKey(
        ResourceBound, 
        on_delete=models.CASCADE,
        related_name='time_classes',
        null=True,
        blank=True,
        default=get_infinite_bound
    )
    space_bound = models.ForeignKey(
        ResourceBound,
        on_delete=models.CASCADE,
        related_name='space_classes',
        null=True,
        blank=True,
        default=get_infinite_bound
    )
    alternations_bound = models.ForeignKey(
        ResourceBound,
        on_delete=models.CASCADE,
        related_name='alternations_classes',
        null=True,
        blank=True,
        default=get_infinite_bound
    )

class Method(models.Model):
    NA = models.CharField(max_length=100)  
    AB = models.CharField(max_length=100) 
    SO = models.IntegerField() 
    DE = models.CharField(max_length=500) # description
    class Meta:
        ordering = ['SO']

# machine type generalization 
class MTG(models.Model):
    lower = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='lower_machine_types')
    upper = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='upper_machine_types')
    method = models.CharField(max_length=500) # manually added or by transitive closure
    # if this is a transitive closure, then row1 and row2 will point to the MTG instances that were used to deduce this instance
    row1 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mtg_row1_set') 
    row2 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mtg_row2_set')

class ManualMTG(models.Model):
    lower = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='manual_lower_machine_types')
    upper = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='manual_upper_machine_types')
    # justification for why lower machine type is a generalization of upper machine type
    justification = models.CharField(max_length=500) 

# machine mode generalization
class MMG(models.Model):
    lower = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='lower_machine_modes')
    upper = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='upper_machine_modes')
    method = models.CharField(max_length=500) # manually added or by transitive closure
    row1 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mmg_row1_set')
    row2 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mmg_row2_set')

class ManualMMG(models.Model):
    lower = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='manual_lower_machine_modes')
    upper = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='manual_upper_machine_modes')
    justification = models.CharField(max_length=500) # justification for why lower machine mode is a generalization of upper machine mode

class Reference(models.Model):
    # description
    DE = models.CharField(max_length=200)
    # DOI link to the publication, Google Books link or link to any online page that describes the publication
    doi = models.CharField(max_length=255)
    # Page numbers, section numbers etc. 
    locator = models.CharField(max_length=100)  

    class Meta:
        unique_together = ['doi', 'locator']

    def __str__(self):
        return f"{self.doi} ({self.locator})"

class ManualInclusion(models.Model):
    lower = models.ForeignKey(
        Class, 
        on_delete=models.CASCADE, 
        related_name='manual_lower_classes'
    )
    upper = models.ForeignKey(
        Class, 
        on_delete=models.CASCADE, 
        related_name='manual_upper_classes'
    )
    justification = models.CharField(
        max_length=500,
    )
    # list of doi and locator pairs that justify this inclusion
    references = models.ManyToManyField(
        Reference,
        related_name='inclusions',
    )

    def __str__(self):
        return f"{self.lower.AB} ⊆ {self.upper.AB}: {self.justification}"
    
class Inclusion(models.Model):
    lower = models.ForeignKey(
        Class, 
        on_delete=models.CASCADE, 
        related_name='inclusion_lower_classes'
    )
    upper = models.ForeignKey(
        Class, 
        on_delete=models.CASCADE, 
        related_name='inclusion_upper_classes'
    )
    method = models.ForeignKey(
        Method, 
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        related_name='inclusions'
    )
    # intermediary class (which proves the inclusion by transitivity)
    interm = models.ForeignKey(
        Class, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='inclusion_interm'
    )

    def __str__(self):
        return f"{self.lower.AB} ⊆ {self.upper.AB} by {self.method.AB}"
    
class Problem(models.Model): 
    NA = models.CharField(max_length=50)
    AB = models.CharField(max_length=50)
    TY = models.ForeignKey(ProblemType, on_delete=models.CASCADE)
    DE = models.CharField(max_length=200)
    co = models.BooleanField(default=False)
    co_problem = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class ManualMembership(models.Model): 
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    com_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    references = models.ManyToManyField(Reference)

class Membership(models.Model): 
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    com_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    # in case of transitivity we store how it was derived, eg. SAT ∈ NP ⊆ PSPACE
    row1 = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="membership_row1_set")
    row2 = models.ForeignKey(
        Inclusion, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="membership_row2_set")

class ManualNonMembership(models.Model): 
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    com_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    references = models.ManyToManyField(Reference)

class NonMembership(models.Model): 
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    com_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    # in case of transitivity we store how it was derived, eg. UNARY EQUALITY ∉ D-REGULAR ⊇ N-REGULAR
    row1 = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="nonmembership_row1_set")
    row2 = models.ForeignKey(
        Inclusion, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="nonmembership_row2_set")

# for non-inclusions which are justified by arguments which do not involve a witness problem
class ManualNonInclusion(models.Model): 
    # manual non inclusions are of the form e.g NP in P (i.e. Upper in Lower)
    upper = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="not_manual_subset_of")
    lower = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="not_manual_superset_of")
    # quick reason why the inclusion holds (e.g., “time upper bounds space”)
    justification = models.CharField(max_length=200)
    references = models.ManyToManyField(Reference)

class NonInclusion(models.Model): 
    upper = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="not_subset_of")
    lower = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="not_superset_of")
    # if we arrive at this non-inclusion via a witness problem, we store it here
    witness_problem = models.ForeignKey(
        Problem, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="non_inclusion_witness_problem"
    )
    # if we arrive via transitivity through non-inclusion
    # interm_class = models.ForeignKey(
    #     Class, 
    #     on_delete=models.CASCADE, 
    #     null=True, 
    #     blank=True, 
    #     related_name="non_inclusion_interm"
    # )
    # A ⊄ B and B ⊇ C implies A ⊄ C
    method = models.ForeignKey(Method, on_delete=models.CASCADE, null=True, blank=True, related_name='non_inclusions')
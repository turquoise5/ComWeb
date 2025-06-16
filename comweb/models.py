from django.db import models

class MachineMode(models.Model):
    AB = models.CharField(max_length=100) # abbreviation
    NA = models.CharField(max_length=100) # name 
    SO = models.IntegerField() # sort order
    class Meta: 
        ordering = ['SO']

class MachineType(models.Model):
    AB = models.CharField(max_length=100) # abbreviation
    NA = models.CharField(max_length=100) # name 
    SO = models.IntegerField() # sort order
    class Meta:
        ordering = ['SO']

class Machine(models.Model):
    AB = models.CharField(max_length=100) # abbreviation
    NA = models.CharField(max_length=100) # name 
    SO = models.IntegerField() # sort order

    # if a Mode instance is deleted, all related objects (instances of the current mode) will also be deleted.
    mode = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='machines')
    type = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='machines') 
    class Meta: 
        ordering = ['SO']

class ProblemType(models.Model):
    NA = models.CharField(max_length=100) # name 
    SO = models.IntegerField() # sort order
    order = models.IntegerField() # order of the problem type compared to other problem types
    class Meta:
        ordering = ['SO']

class ResourceBound(models.Model):
    NA = models.CharField(max_length=100) # name 
    AB = models.CharField(max_length=100) # abbreviation
    SO = models.IntegerField() # sort order
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
    NA = models.CharField(max_length=100) # name 
    AB = models.CharField(max_length=100) # abbreviation
    SO = models.IntegerField() # sort order
    DE = models.CharField(max_length=500) # description
    class Meta:
        ordering = ['SO']

# machine type generalization 
class MTG(models.Model):
    lower = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='lower_machine_types')
    upper = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='upper_machine_types')
    method = models.CharField(max_length=100) # manually added or by transitive closure
    row1 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mtg_row1_set') # if this is a transitive closure, then row1 and row2 will point to the MTG instances that were used to deduce this instance
    row2 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mtg_row2_set')

class ManualMTG(models.Model):
    lower = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='manual_lower_machine_types')
    upper = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='manual_upper_machine_types')
    justification = models.CharField(max_length=500) # justification for why lower machine type is a generalization of upper machine type

# machine mode generalization
class MMG(models.Model):
    lower = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='lower_machine_modes')
    upper = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='upper_machine_modes')
    method = models.CharField(max_length=100) # manually added or by transitive closure
    row1 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mmg_row1_set')
    row2 = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mmg_row2_set')

class ManualMMG(models.Model):
    lower = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='manual_lower_machine_modes')
    upper = models.ForeignKey(MachineMode, on_delete=models.CASCADE, related_name='manual_upper_machine_modes')
    justification = models.CharField(max_length=500) # justification for why lower machine mode is a generalization of upper machine mode

class AutoInclusion(models.Model):
    lower = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lower_classes')
    upper = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='upper_classes')
    method = models.ForeignKey(Method, on_delete=models.PROTECT, related_name='auto_inclusions')

class Reference(models.Model):
    doi = models.CharField(max_length=255)
    locator = models.CharField(max_length=100)  # Page numbers, section numbers etc.

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
        related_name='inclusions'
    )
    row1 = models.ForeignKey(
        ManualInclusion, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='inclusion_row1_set'
    )
    row2 = models.ForeignKey(
        ManualInclusion, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='inclusion_row2_set'
    )

    def __str__(self):
        return f"{self.lower.AB} ⊆ {self.upper.AB} by {self.method.AB}"
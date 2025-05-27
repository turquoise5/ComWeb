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
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name='machines') 
    class Meta: 
        ordering = ['SO']

class Resource(models.Model):
    NA = models.CharField(max_length=100) # name 
    SO = models.IntegerField() # sort order
    class Meta:
        ordering = ['SO']

class ProblemType(models.Model):
    NA = models.CharField(max_length=100) # name 
    SO = models.IntegerField() # sort order
    class Meta:
        ordering = ['SO']

class ResourceBound(models.Model):
    NA = models.CharField(max_length=100) # name 
    AB = models.CharField(max_length=100) # abbreviation
    SO = models.IntegerField() # sort order
    order = models.IntegerField() # order of the bound compared to other bounds
    class Meta:
        ordering = ['SO']

class Class(models.Model):
    NA = models.CharField(max_length=100) # name 
    AB = models.CharField(max_length=100) # abbreviation
    problem_type = models.ForeignKey(ProblemType, on_delete=models.CASCADE, related_name='classes')   
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='classes')
    resource1 = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='classes1')
    resource2 = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='classes2', blank=True, null=True)
    bound1 = models.ForeignKey(ResourceBound, on_delete=models.CASCADE, related_name='classes1')
    bound2 = models.ForeignKey(ResourceBound, on_delete=models.CASCADE, related_name='classes2', blank=True, null=True) 

class Method(models.Model):
    NA = models.CharField(max_length=100) # name 
    AB = models.CharField(max_length=100) # abbreviation
    SO = models.IntegerField() # sort order
    DE = models.CharField(max_length=500) # description
    class Meta:
        ordering = ['SO']

class AutoInclusion(models.Model):
    lower = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lower_classes')
    upper = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='upper_classes')
    method = models.ForeignKey(Method, on_delete=models.PROTECT, related_name='auto_inclusions')



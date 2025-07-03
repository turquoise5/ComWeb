from django.contrib import admin
from .models import Class, Machine, MachineMode, MachineType, ProblemType, ResourceBound, Method, ManualMTG, MMG, ManualMMG, MTG, ManualInclusion, Inclusion

admin.site.register(MachineMode)
admin.site.register(MachineType)
admin.site.register(Machine)
admin.site.register(ProblemType)
admin.site.register(ResourceBound)
admin.site.register(Class)
admin.site.register(Method)
admin.site.register(MTG)
admin.site.register(ManualMTG)
admin.site.register(MMG)
admin.site.register(ManualMMG)
admin.site.register(ManualInclusion)
admin.site.register(Inclusion)


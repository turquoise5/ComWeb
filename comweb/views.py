from django.shortcuts import render
from comweb.models import *
def home(request): 
    context = {
        "modes": [x.NA for x in MachineMode.objects.all()],
        "machine_types": [x.NA for x in MachineType.objects.all()],
        "machines": [x.NA for x in Machine.objects.all()],
        "resources": [x.NA for x in Resource.objects.all()],
        "problem_types": [x.NA for x in ProblemType.objects.all()],
        "bounds": [x.NA for x in ResourceBound.objects.all()],
        "classes": [x.NA for x in Class.objects.all()], 
        "methods": [x.NA for x in Method.objects.all()],
        "inclusions": [x.NA for x in AutoInclusion.objects.all()],
        "manual_mtgs": [x for x in ManualMTG.objects.all()],
        "mtgs": [x for x in MTG.objects.all()],
        "manual_mmgs": [x for x in ManualMMG.objects.all()],
        "mmgs": [x for x in MMG.objects.all()],
    }
    return render(request, "comweb/home.html", context)


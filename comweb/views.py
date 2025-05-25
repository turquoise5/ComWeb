from django.shortcuts import render
from comweb.models import *
def home(request): 
    context = {
        "modes": [x.NA for x in Mode.objects.all()],
        "machine_types": [x.NA for x in MachineType.objects.all()],
        "machines": [x.NA for x in Machine.objects.all()],
        "resources": [x.NA for x in Resource.objects.all()],
        "problem_types": [x.NA for x in ProblemType.objects.all()],
        "bounds": [x.NA for x in Bound.objects.all()],
        "classes": [x.NA for x in Class.objects.all()]
    }
    return render(request, "comweb/home.html", context)


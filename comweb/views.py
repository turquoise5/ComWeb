from django.shortcuts import render
from django.http import JsonResponse
from comweb.models import *

def home(request): 
    return render(request, "comweb/home.html")

def get_list(request):  
    list_type = request.GET.get('type') 
    data = []
    if list_type == 'modesList':
        data = [x.NA for x in MachineMode.objects.all()] 
    elif list_type == 'typesList':
        data = [{
            "name": x.NA,
            "AB": x.AB
        } for x in MachineType.objects.all()  
    ]   
    elif list_type == 'resourcesList':
        data = [x.NA for x in Resource.objects.all()]
    elif list_type == 'problemTypesList':
        data = [x.NA for x in ProblemType.objects.all()]
    elif list_type == 'boundsList':
        data = [x.NA for x in ResourceBound.objects.all()]
    elif list_type == 'classesList':
        data = [{
            "name": x.NA,
            "AB": x.AB
        } for x in Class.objects.all() 
    ]        
    elif list_type == 'inclusionsList':
        data = [
            {
                'lower': x.lower.AB if hasattr(x.lower, 'AB') else '',
                'upper': x.upper.AB if hasattr(x.upper, 'AB') else ''
            }
            for x in AutoInclusion.objects.all()
        ]
    elif list_type == 'methodsList':
        data = [
            {'name': x.NA, 'description': getattr(x, 'description', '')}
            for x in Method.objects.all()
        ]
    elif list_type == 'manualMTGList':
        data = [
            {
                'lower': x.lower.NA if hasattr(x.lower, 'NA') else '',
                'upper': x.upper.NA if hasattr(x.upper, 'NA') else '',
                'justification': x.justification
            }
            for x in ManualMTG.objects.all()
        ]
    elif list_type == 'MTGList':
        data = [
            {
                'lower': x.lower.NA if hasattr(x.lower, 'NA') else '',
                'upper': x.upper.NA if hasattr(x.upper, 'NA') else ''
            }
            for x in MTG.objects.all()
        ]
    elif list_type == 'manualMMGList':
        data = [
            {
                'lower': x.lower.NA if hasattr(x.lower, 'NA') else '',
                'upper': x.upper.NA if hasattr(x.upper, 'NA') else '',
                'justification': x.justification
            }
            for x in ManualMMG.objects.all()
        ]
    elif list_type == 'MMGList':
        data = [
            {
                'lower': x.lower.NA if hasattr(x.lower, 'NA') else '',
                'upper': x.upper.NA if hasattr(x.upper, 'NA') else ''
            }
            for x in MMG.objects.all()
        ]
    
    return JsonResponse({'data': data})


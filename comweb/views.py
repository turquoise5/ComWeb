from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    elif list_type == 'machinesList':
        data = [{
            "name": x.NA,
            "AB": x.AB
        } for x in Machine.objects.all()] 
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
        data = [{
            'lower': mtg.lower.NA,
            'upper': mtg.upper.NA,
            'method': mtg.method,
            'row1': {
                'lower': mtg.row1.lower.NA if mtg.row1 else None,
                'upper': mtg.row1.upper.NA if mtg.row1 else None
            } if mtg.row1 else None,
            'row2': {
                'lower': mtg.row2.lower.NA if mtg.row2 else None,
                'upper': mtg.row2.upper.NA if mtg.row2 else None
            } if mtg.row2 else None
        } for mtg in MTG.objects.select_related(
            'lower', 'upper', 
            'row1__lower', 'row1__upper',
            'row2__lower', 'row2__upper'
        )]
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
        data = [{
            'lower': mmg.lower.NA,
            'upper': mmg.upper.NA,
            'method': mmg.method,
            'row1': {
                'lower': mmg.row1.lower.NA if mmg.row1 else None,
                'upper': mmg.row1.upper.NA if mmg.row1 else None
            } if mmg.row1 else None,
            'row2': {
                'lower': mmg.row2.lower.NA if mmg.row2 else None,
                'upper': mmg.row2.upper.NA if mmg.row2 else None
            } if mmg.row2 else None
        } for mmg in MMG.objects.select_related(
            'lower', 'upper',
            'row1__lower', 'row1__upper',
            'row2__lower', 'row2__upper'
        )]
    
    return JsonResponse({'data': data})


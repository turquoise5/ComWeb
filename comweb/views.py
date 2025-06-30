from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from comweb.models import *
from django.core.paginator import Paginator

def home(request): 
    return render(request, "comweb/home.html")

def machine_info_view(request):
    types = MachineType.objects.all()
    modes = MachineMode.objects.all()
    machines = Machine.objects.select_related('mode', 'type').all()
    context = {
        'types': types,
        'modes': modes,
        'machines': machines
    }
    return render(request, "comweb/machine_info.html", context)

def complexity_info_view(request):
    bounds = ResourceBound.objects.all()
    problem_types = ProblemType.objects.all()
    classes = Class.objects.select_related(
        'problem_type', 
        'machine',
        'time_bound',
        'space_bound',
        'alternations_bound'
    ).all()
    context = {
        'bounds': bounds,
        'problem_types': problem_types,
        'classes': classes
    }
    return render(request, "comweb/complexity_info.html", context)

def inclusions_view(request):
    manual_inclusions = ManualInclusion.objects.select_related(
        'lower', 
        'upper'
    ).prefetch_related('references').order_by('id')
    auto_inclusions = AutoInclusion.objects.select_related(
        'lower', 
        'upper',
        'method'
    ).order_by('id')
    all_inclusions = Inclusion.objects.select_related(
        'lower', 
        'upper',
        'method'
    ).order_by('id')

    # Paginate each list (50 per page)
    manual_page_number = request.GET.get('manual_page', 1)
    auto_page_number = request.GET.get('auto_page', 1)
    all_page_number = request.GET.get('all_page', 1)

    manual_paginator = Paginator(manual_inclusions, 50)
    auto_paginator = Paginator(auto_inclusions, 50)
    all_paginator = Paginator(all_inclusions, 50)

    context = {
        'manual_inclusions_page': manual_paginator.get_page(manual_page_number),
        'auto_inclusions_page': auto_paginator.get_page(auto_page_number),
        'all_inclusions_page': all_paginator.get_page(all_page_number),
    }
    return render(request, "comweb/inclusions.html", context)

def mtg_view(request):
    manual_mtgs = ManualMTG.objects.select_related(
        'lower', 
        'upper'
    ).all()
    mtgs = MTG.objects.select_related(
        'lower', 'upper',
        'row1__lower', 'row1__upper',
        'row2__lower', 'row2__upper'
    ).all()
    context = {'mtgs': mtgs, "manual_mtgs": manual_mtgs}
    return render(request, "comweb/mtg.html", context)

def mmg_view(request):
    manual_mmgs = ManualMMG.objects.select_related(
        'lower', 
        'upper'
    ).all()
    mmgs = MMG.objects.select_related(
        'lower', 'upper',
        'row1__lower', 'row1__upper',
        'row2__lower', 'row2__upper'
    ).all()
    context = {'mmgs': mmgs, "manual_mmgs": manual_mmgs}
    return render(request, "comweb/mmg.html", context)
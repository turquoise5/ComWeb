from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from comweb.models import *

def home(request): 
    return render(request, "comweb/home.html")

def machine_info_view(request):
    types = MachineType.objects.all()[:50]
    modes = MachineMode.objects.all()[:50]
    machines = Machine.objects.select_related('mode', 'type').all()[:50]
    context = {
        'types': types,
        'modes': modes,
        'machines': machines
    }
    return render(request, "comweb/machine_info.html", context)

def complexity_info_view(request):
    bounds = ResourceBound.objects.all()[:50]
    problem_types = ProblemType.objects.all()[:50]
    classes = Class.objects.select_related(
        'problem_type', 
        'machine',
        'time_bound',
        'space_bound',
        'alternations_bound'
    ).all()[:50]
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
    ).prefetch_related('references').all()
    auto_inclusions = AutoInclusion.objects.select_related(
        'lower', 
        'upper',
        'method'
    ).all()[:50]
    all_inclusions = Inclusion.objects.select_related(
        'lower', 
        'upper',
        'method'
    ).all()[:100]
    context = {
        'manual_inclusions': manual_inclusions,
        'auto_inclusions': auto_inclusions, 
        'all_inclusions': all_inclusions
    }
    return render(request, "comweb/inclusions.html", context)

def mtg_view(request):
    manual_mtgs = ManualMTG.objects.select_related(
        'lower', 
        'upper'
    ).all()[:50]
    mtgs = MTG.objects.select_related(
        'lower', 'upper',
        'row1__lower', 'row1__upper',
        'row2__lower', 'row2__upper'
    ).all()[:50]
    context = {'mtgs': mtgs, "manual_mtgs": manual_mtgs}
    return render(request, "comweb/mtg.html", context)

def mmg_view(request):
    manual_mmgs = ManualMMG.objects.select_related(
        'lower', 
        'upper'
    ).all()[:50]
    mmgs = MMG.objects.select_related(
        'lower', 'upper',
        'row1__lower', 'row1__upper',
        'row2__lower', 'row2__upper'
    ).all()[:50]
    context = {'mmgs': mmgs, "manual_mmgs": manual_mmgs}
    return render(request, "comweb/mmg.html", context)
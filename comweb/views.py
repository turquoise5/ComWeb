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
    ).order_by('AB')
    co_map = {c.id: c.co_class for c in classes if not c.co}
    ordered_classes =[]
    for c in classes:
        if not c.co: 
            ordered_classes.append(c)
            ordered_classes.append(co_map[c.id])


    context = {
        'bounds': bounds,
        'problem_types': problem_types,
        'classes': ordered_classes
    }
    return render(request, "comweb/complexity_info.html", context)

def inclusions_view(request):
    manual_inclusions = ManualInclusion.objects.select_related(
        'lower', 
        'upper'
    ).prefetch_related('references').order_by('id')
    all_inclusions = Inclusion.objects.select_related(
        'lower', 
        'upper',
        'method'
    ).order_by('id')

    # Paginate each list (50 per page)
    manual_page_number = request.GET.get('manual_page', 1)
    all_page_number = request.GET.get('all_page', 1)

    manual_paginator = Paginator(manual_inclusions, 50)
    all_paginator = Paginator(all_inclusions, 50)

    manual_just_map = {
        (m.lower_id, m.upper_id): m.justification
        for m in ManualInclusion.objects.all()
    }
    for inc in all_inclusions:
        if inc.method and inc.method.AB == 'manual':
            inc.manual_justification = manual_just_map.get((inc.lower_id, inc.upper_id), '')

    manual_refs_map = {
        (m.lower_id, m.upper_id): list(m.references.all())
        for m in ManualInclusion.objects.prefetch_related('references')
    }
    for inc in all_inclusions:
        if inc.method and inc.method.AB == 'manual':
            inc.manual_references = manual_refs_map.get((inc.lower_id, inc.upper_id), [])

    context = {
        'manual_inclusions_page': manual_paginator.get_page(manual_page_number),
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

def problems_view(request):
    problems = Problem.objects.select_related('TY').all().order_by('NA')
    return render(request, "comweb/problems.html", {"problems": problems})


def memberships_view(request):
    manual_memberships = ManualMembership.objects.select_related('problem', 'com_class').prefetch_related('references').all()
    memberships = Membership.objects.select_related('problem', 'com_class', 'method', 'row1', 'row2').all()
    return render(request, "comweb/memberships.html", {
        "manual_memberships": manual_memberships,
        "memberships": memberships,
    })

def nonmemberships_view(request):
    manual_nonmemberships = ManualNonMembership.objects.select_related('problem', 'com_class').prefetch_related('references').all()
    nonmemberships = NonMembership.objects.select_related('problem', 'com_class', 'method', 'row1', 'row2').all()
    return render(request, "comweb/nonmemberships.html", {
        "manual_nonmemberships": manual_nonmemberships,
        "nonmemberships": nonmemberships,
    })

def noninclusions_view(request):
    manual_noninclusions = ManualNonInclusion.objects.select_related('upper', 'lower').prefetch_related('references').all()
    noninclusions = NonInclusion.objects.select_related('upper', 'lower').all()
    return render(request, "comweb/noninclusions.html", {
        "manual_noninclusions": manual_noninclusions,
        "noninclusions": noninclusions,
    })
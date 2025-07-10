from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from comweb.models import *
from django.core.paginator import Paginator
from django.db.models import Q

# JANA ADD PAGINATION TO EVERY VIEW


def home(request): 
    return render(request, "comweb/home.html")

def find_witness_problems(a, b): 
    """Find witness problems for non-inclusion between classes a and b."""
    witness_problems = Problem.objects.filter(
        memberships__com_class=a,
        non_memberships__com_class=b
    ).distinct()
    return witness_problems

def construct_non_inclusion_string(a, b, all_non_inclusions): 
    ni_obj = NonInclusion.objects.select_related('method', 'not_superset', 'not_subset', 'interm').get(not_superset=a, not_subset=b)
    if ni_obj.method == "witness":
        witness_problems = find_witness_problems(ni_obj.not_superset, ni_obj.not_subset)
        if witness_problems.exists():
            return f"NO: {ni_obj.not_superset.AB} is not a subset of {ni_obj.not_subset.AB} (Witness Problem: {', '.join([wp.AB for wp in witness_problems])})"
        else:
            return f"NO: {ni_obj.not_superset.AB} is not a subset of {ni_obj.not_subset.AB} (Witness Problem: None)"
    elif ni_obj.method.AB == "manual":
        return f"NO: {ni_obj.not_superset.AB} is not a subset of {ni_obj.not_subset.AB} (Manual Justification: {ni_obj.manual_justification}; see {', '.join([f'#{ref.id}' for ref in ni_obj.manual_references])})"
    elif ni_obj.method.AB == "trans": 
        return f"NO: {ni_obj.not_superset.AB} is not a subset of {ni_obj.not_subset.AB} (Transitive Justification: {ni_obj.interm.AB})"
    
    return ""


def class_search(request):
    term = request.GET.get('q', '')
    results = []

    if term:
        queryset = Class.objects.filter(Q(AB__icontains=term) | Q(NA__icontains=term)).order_by('AB')[:20]
        results = [
            {"id": c.id, "text": f"{c.AB} - {c.NA}"} for c in queryset
        ]

    return JsonResponse({"results": results})


def problem_search(request):
    term = request.GET.get('q', '')
    results = []

    if term:
        problems = Problem.objects.filter(Q(AB__icontains=term) | Q(NA__icontains=term)).order_by('AB')[:20]
        results = [{"id": p.id, "text": f"{p.AB} - {p.NA}"} for p in problems]

    return JsonResponse({"results": results})

def query_inclusion_view(request):
    classes = Class.objects.all().order_by('AB')
    result_type = None  # "yes", "no", or "unspecified"
    inc_obj = None
    ni_obj = None

    if request.method == "POST":
        a_id = request.POST.get("class_a")
        b_id = request.POST.get("class_b")

        try:
            a = Class.objects.get(id=a_id)
            b = Class.objects.get(id=b_id)
        except Class.DoesNotExist:
            result_type = "invalid"
        else:
            if Inclusion.objects.filter(lower=a, upper=b).exists():
                inc_obj = Inclusion.objects.select_related('method', 'lower', 'upper', 'interm').get(lower=a, upper=b)
                all_inclusions = Inclusion.objects.select_related('lower', 'upper', 'method').order_by('id')
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

                result_type = "yes"
            elif NonInclusion.objects.filter(not_superset=a, not_subset=b).exists():
                all_non_inclusions = NonInclusion.objects.select_related(
                    'not_superset', 'not_subset', 'method', 'interm'
                ).order_by('id')
                manual_just_map = {
                    (m.upper_id, m.lower_id): m.justification
                    for m in ManualNonInclusion.objects.all()
                }
                for non_inc in all_non_inclusions:
                    if non_inc.method and non_inc.method.AB == 'manual':
                        non_inc.manual_justification = manual_just_map.get((non_inc.lower_id, non_inc.upper_id), '')

                manual_refs_map = {
                    (m.upper_id, m.lower_id): list(m.references.all())
                    for m in ManualNonInclusion.objects.prefetch_related('references')
                }

                for non_inc in all_non_inclusions:
                    if non_inc.method and non_inc.method.AB == 'manual':
                        non_inc.manual_references = manual_refs_map.get((non_inc.lower_id, non_inc.upper_id), [])

                result_type = "no"
                result = construct_non_inclusion_string(a, b, all_non_inclusions)
            else:
                result_type = "unspecified"

    return render(request, "comweb/home.html", {
        "inclusion_result": True,
        "classes": classes,
        "result_type": result_type,
        "inc": inc_obj,
        "ni": ni_obj,
        "result": result if 'result' in locals() else None
    })


def query_membership(request):
    classes = Class.objects.all().order_by('AB')
    result_type = None  # "yes", "no", or "unspecified"
    membership_obj = None

    if request.method == "POST":
        problem_id = request.POST.get("problem")
        class_id = request.POST.get("class")

        try:
            problem = Problem.objects.get(id=problem_id)
            com_class = Class.objects.get(id=class_id)
        except (Problem.DoesNotExist, Class.DoesNotExist):  
            result_type = "invalid"
        else:
            if Membership.objects.filter(problem=problem, com_class=com_class).exists():
                membership_obj = Membership.objects.select_related(
                    'problem', 'com_class', 'method', 'row1', 'row2'
                ).get(problem=problem, com_class=com_class)
                result_type = "yes"
            elif NonMembership.objects.filter(problem=problem, com_class=com_class).exists():
                result_type = "no"
            else:
                result_type = "unspecified"
        
    return render(request, "comweb/home.html", {
        "membership_result": True,
        "classes": classes,
        "result_type": result_type,
        "membership": membership_obj,
        "problems": Problem.objects.all().order_by('AB')
    })

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
    problems = Problem.objects.select_related('TY').all()
    
    co_map = {p.id: p.co_problem for p in problems if not p.co}
    ordered_problems = []
    for p in problems:
        if not p.co: 
            ordered_problems.append(p)
            ordered_problems.append(co_map[p.id])

    return render(request, "comweb/problems.html", {"problems": ordered_problems})


def memberships_view(request):
    manual_memberships = ManualMembership.objects.select_related('problem', 'com_class').prefetch_related('references').all().order_by('id')
    memberships = Membership.objects.select_related('problem', 'com_class', 'method', 'row1', 'row2').all().order_by('id')
    # ADD PAGINATION

    manual_page_number = request.GET.get('manual_page', 1)
    all_page_number = request.GET.get('all_page', 1)
    manual_paginator = Paginator(manual_memberships, 50)
    all_paginator = Paginator(memberships, 50)
    manual_memberships_page = manual_paginator.get_page(manual_page_number)
    memberships_page = all_paginator.get_page(all_page_number)
    

    return render(request, "comweb/memberships.html", {
        "manual_memberships": manual_memberships_page,
        "memberships": memberships_page,
    })

def nonmemberships_view(request):
    # add pagination
    manual_nonmemberships = ManualNonMembership.objects.select_related('problem', 'com_class').prefetch_related('references').all().order_by('id')
    nonmemberships = NonMembership.objects.select_related('problem', 'com_class', 'method', 'row1', 'row2').all().order_by('id')

    manual_page_number = request.GET.get('manusal_page', 1)
    all_page_number = request.GET.get('all_page', 1)
    manual_paginator = Paginator(manual_nonmemberships, 50)
    all_paginator = Paginator(nonmemberships, 50)
    manual_nonmemberships_page = manual_paginator.get_page(manual_page_number)
    nonmemberships_page = all_paginator.get_page(all_page_number)

    return render(request, "comweb/nonmemberships.html", {
        "manual_nonmemberships": manual_nonmemberships_page,
        "nonmemberships": nonmemberships_page,
    })

def noninclusions_view(request):
    manual_noninclusions = ManualNonInclusion.objects.select_related('upper', 'lower').prefetch_related('references').all().order_by('id')
    noninclusions = NonInclusion.objects.select_related('not_superset', 'not_subset', 'interm').all().order_by('id')
    # PAGINATION
    manual_page_number = request.GET.get('manual_page', 1)
    all_page_number = request.GET.get('all_page', 1)
    manual_paginator = Paginator(manual_noninclusions, 50)
    all_paginator = Paginator(noninclusions, 50)
    manual_noninclusions_page = manual_paginator.get_page(manual_page_number)
    noninclusions_page = all_paginator.get_page(all_page_number)

    # Add manual justifications and references to noninclusions
    manual_just_map = {
        (m.not_superset_id, m.not_subset_id): m.justification
        for m in ManualNonInclusion.objects.all()
    }
    for ni in noninclusions:
        if ni.method and ni.method.AB == 'manual':
            ni.manual_justification = manual_just_map.get((ni.not_superset_id, ni.not_subset_id), '')
    manual_refs_map = {
        (m.not_superset_id, m.not_subset_id): list(m.references.all())
        for m in ManualNonInclusion.objects.prefetch_related('references')
    }
    for ni in noninclusions:
        ni.manual_references = manual_refs_map.get((ni.not_superset_id, ni.not_subset_id), [])

    return render(request, "comweb/noninclusions.html", {
        "manual_noninclusions": manual_noninclusions_page,
        "noninclusions": noninclusions_page,
    })
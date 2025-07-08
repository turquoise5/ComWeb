from comweb.models import (
    ManualNonInclusion, NonInclusion, Inclusion, Membership, NonMembership, Method, Class, Problem
)

def populate_non_inclusions():
    # Get method objects
    manual_method = Method.objects.get(AB="manual")
    witness_method = Method.objects.get(AB="witness")
    trans_method = Method.objects.get(AB="trans")

    # 1. Add all rows from MANUAL-NONINCLUSION (combine justification & references)
    for mni in ManualNonInclusion.objects.prefetch_related('references', 'upper', 'lower'):
        NonInclusion.objects.create(
            upper=mni.upper,
            lower=mni.lower,
            method=manual_method,
        )

    # 2. Generate all non-inclusions of the form A not-subset-of B, for all A and B such that
    # there exists problem X with X in A in (MEMBERSHIP) & X not in B in (NONMEMBERSHIP). Use method "witness"
    memberships = Membership.objects.all().values_list('problem_id', 'com_class_id')
    nonmemberships = NonMembership.objects.all().values_list('problem_id', 'com_class_id')
    membership_map = {}
    for prob_id, class_id in memberships:
        membership_map.setdefault(prob_id, set()).add(class_id)
    nonmembership_map = {}
    for prob_id, class_id in nonmemberships:
        nonmembership_map.setdefault(prob_id, set()).add(class_id)
    witness_pairs = set()
    for prob_id in membership_map:
        if prob_id in nonmembership_map:
            for a in membership_map[prob_id]:
                for b in nonmembership_map[prob_id]:
                    NonInclusion.objects.get_or_create(
                        upper=Class.objects.get(id=b),
                        lower=Class.objects.get(id=a),
                        method=witness_method,
                        witness_problem=Problem.objects.get(id=prob_id)
                    )
                    # witness_pairs.add((a, b))

    # for a_id, b_id in witness_pairs:
    #     NonInclusion.objects.get_or_create(
    #         upper=Class.objects.get(id=b_id),
    #         lower=Class.objects.get(id=a_id),
    #         method=witness_method,
    #     )

    # 3. Add every pair (A,C) such that (A,B) in NONINCLUSION and (C,B) in INCLUSION
    noninclusions = list(NonInclusion.objects.all())
    inclusions = list(Inclusion.objects.all())
    for ni in noninclusions:
        for inc in inclusions:
            # VERY CONFUSING: fix naming of upper/lower in NonInclusion and Inclusion
            # Here, we assume that ni.upper is the class A and ni.lower is the class B
            # and inc.upper is the class C and inc.lower is the class B
            if inc.upper_id == ni.lower_id:
                if not NonInclusion.objects.filter(upper=ni.upper, lower=inc.lower).exists():
                    # Create NonInclusion only if it doesn't already exist, avoids duplicates
                    NonInclusion.objects.get_or_create(
                        upper=ni.upper,
                        lower=inc.lower,
                    )

    # 4. Add every pair (D,B) such that (A,B) in NONINCLUSION and (A,D) in INCLUSION
    for ni in noninclusions:
        for inc in inclusions:
            if inc.lower_id == ni.lower_id:
                if not NonInclusion.objects.filter(upper=ni.upper, lower=inc.upper).exists():
                    # Create NonInclusion only if it doesn't already exist, avoids duplicates
                    NonInclusion.objects.get_or_create(
                        upper=ni.upper,
                        lower=inc.upper,
                    )
from sys import stdout
from comweb.models import (
    ManualNonInclusion, NonInclusion, Inclusion, Membership, NonMembership, Method, Class, Problem
)

def populate_non_inclusions():
    from collections import defaultdict

    manual_method = Method.objects.get(AB="manual")
    witness_method = Method.objects.get(AB="witness")
    trans_method = Method.objects.get(AB="trans")

    # Cache Class and Problem objects
    class_map = {c.id: c for c in Class.objects.all()}
    problem_map = {p.id: p for p in Problem.objects.all()}

    # 1. Manual non-inclusions
    NonInclusion.objects.bulk_create([
        NonInclusion(
            upper=mni.upper,
            lower=mni.lower,
            method=manual_method
        )
        for mni in ManualNonInclusion.objects.select_related('upper', 'lower')
    ])

    # 2. Witness-based non-inclusions
    memberships = Membership.objects.all().values_list('problem_id', 'com_class_id')
    nonmemberships = NonMembership.objects.all().values_list('problem_id', 'com_class_id')

    membership_map = defaultdict(set)
    for pid, cid in memberships:
        membership_map[pid].add(cid)

    nonmembership_map = defaultdict(set)
    for pid, cid in nonmemberships:
        # for each problem, add all classes it is not a member of
        nonmembership_map[pid].add(cid)

    witness_rows = []
    for pid in membership_map:
        if pid in nonmembership_map:
            # for each problem, create non_inclusions for the classes it is a witness for
            for a_id in membership_map[pid]:
                for b_id in nonmembership_map[pid]:
                    witness_rows.append(NonInclusion(
                        not_superset=class_map[b_id],
                        not_subset=class_map[a_id],
                        method=witness_method,
                    ))

    NonInclusion.objects.bulk_create(witness_rows, ignore_conflicts=True)

    # 3. Transitive non-inclusions
    noninclusions = list(NonInclusion.objects.all().select_related('not_superset', 'not_subset'))
    inclusions = list(Inclusion.objects.all())

    existing_non_inclusions = set(
        (ni.not_superset_id, ni.not_subset_id) for ni in NonInclusion.objects.all().only('not_superset_id', 'not_subset_id')
    )

    transitive_rows = []
    for ni in noninclusions:
        for inc in inclusions:
            # (A,B) in non_inclusion, (C,B) in inclusion → (A,C) in non_inclusion
            if inc.upper_id == ni.not_subset_id:
                if (ni.not_superset_id, inc.lower_id) not in existing_non_inclusions:
                    transitive_rows.append(NonInclusion(
                        not_superset=ni.not_superset,
                        not_subset=inc.lower,
                        method=trans_method, 
                        interm=inc.upper
                    ))
                    # stdout.write(f"1 Adding transitive non-inclusion: {ni.not_superset.AB} not subset of {inc.lower.AB} by {inc.upper.AB}\n")
                    existing_non_inclusions.add((ni.not_superset_id, inc.lower_id))

            # (A,B) in non_inclusion, (A,D) in inclusion → (D,B) in non_inclusion
            if inc.lower_id == ni.not_superset_id:
                if (inc.upper_id, ni.not_subset_id) not in existing_non_inclusions:
                    transitive_rows.append(NonInclusion(
                        not_superset=inc.upper,
                        not_subset=ni.not_subset,
                        method=trans_method,
                        interm=inc.lower
                    ))
                    # stdout.write(f"2 Adding transitive non-inclusion: {inc.upper.AB} not subset of {ni.not_superset.AB} by {inc.lower.AB}\n")
                    existing_non_inclusions.add((inc.upper_id, ni.not_subset_id))

    # stdout.write(f"Adding {len(transitive_rows)} transitive non-inclusions.\n")
    NonInclusion.objects.bulk_create(transitive_rows, ignore_conflicts=True)



# def populate_non_inclusions():
#     # Get method objects
#     manual_method = Method.objects.get(AB="manual")
#     witness_method = Method.objects.get(AB="witness")
#     trans_method = Method.objects.get(AB="trans")

#     # 1. Add all rows from MANUAL-NONINCLUSION (combine justification & references)
#     for mni in ManualNonInclusion.objects.prefetch_related('references', 'upper', 'lower'):
#         NonInclusion.objects.create(
#             upper=mni.upper,
#             lower=mni.lower,
#             method=manual_method,
#         )

#     # 2. Generate all non-inclusions of the form A not-subset-of B, for all A and B such that
#     # there exists problem X with X in A in (MEMBERSHIP) & X not in B in (NONMEMBERSHIP). Use method "witness"
#     memberships = Membership.objects.all().values_list('problem_id', 'com_class_id')
#     nonmemberships = NonMembership.objects.all().values_list('problem_id', 'com_class_id')
#     membership_map = {}
#     for prob_id, class_id in memberships:
#         membership_map.setdefault(prob_id, set()).add(class_id)
#     nonmembership_map = {}
#     for prob_id, class_id in nonmemberships:
#         nonmembership_map.setdefault(prob_id, set()).add(class_id)
#     witness_pairs = set()
#     for prob_id in membership_map:
#         if prob_id in nonmembership_map:
#             for a in membership_map[prob_id]:
#                 for b in nonmembership_map[prob_id]:
#                     NonInclusion.objects.get_or_create(
#                         upper=Class.objects.get(id=b),
#                         lower=Class.objects.get(id=a),
#                         method=witness_method,
#                         witness_problem=Problem.objects.get(id=prob_id)
#                     )
#                     # witness_pairs.add((a, b))

#     # for a_id, b_id in witness_pairs:
#     #     NonInclusion.objects.get_or_create(
#     #         upper=Class.objects.get(id=b_id),
#     #         lower=Class.objects.get(id=a_id),
#     #         method=witness_method,
#     #     )

#     # 3. Add every pair (A,C) such that (A,B) in NONINCLUSION and (C,B) in INCLUSION
#     noninclusions = list(NonInclusion.objects.all())
#     inclusions s= list(Inclusion.objects.all())
#     for ni in noninclusions:
#         for inc in inclusions:
#             # VERY CONFUSING: fix naming of upper/lower in NonInclusion and Inclusion
#             # Here, we assume that ni.upper is the class A and ni.lower is the class B
#             # and inc.upper is the class C and inc.lower is the class B
#             if inc.upper_id == ni.lower_id:
#                 if not NonInclusion.objects.filter(upper=ni.upper, lower=inc.lower).exists():
#                     # Create NonInclusion only if it doesn't already exist, avoids duplicates
#                     NonInclusion.objects.get_or_create(
#                         upper=ni.upper,
#                         lower=inc.lower,
#                     )

#     # 4. Add every pair (D,B) such that (A,B) in NONINCLUSION and (A,D) in INCLUSION
#     for ni in noninclusions:
#         for inc in inclusions:
#             if inc.lower_id == ni.lower_id:
#                 if not NonInclusion.objects.filter(upper=ni.upper, lower=inc.upper).exists():
#                     # Create NonInclusion only if it doesn't already exist, avoids duplicates
#                     NonInclusion.objects.get_or_create(
#                         upper=ni.upper,
#                         lower=inc.upper,
#                     )
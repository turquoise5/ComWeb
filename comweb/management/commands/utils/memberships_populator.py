from sys import stdout
from comweb.models import Inclusion, Membership, NonMembership
from collections import defaultdict, deque

def populate_memberships(manual_membership, methods):
    # manual_membership: list of (problem, class)
    # inclusion: list of (class_from, class_to)
    # Returns: set of (problem, class) for MEMBERSHIP

    inclusion = Inclusion.objects.all().select_related('upper', 'lower')

    # Build inclusion map: lower -> set of upper
    inclusion_map = defaultdict(set)
    for inc in inclusion:
        try:       
            inclusion_map[inc.lower.AB].add(inc.upper)
        except Inclusion.DoesNotExist:
            stdout.write(f"Warning: Inclusion not found for ({inc.lower}, {inc.upper}). Skipping.\n")
            continue
    # inclusion_map = {c.lower.AB: set(c.upper.AB for c in Inclusion.objects.filter(lower=c.lower)) for c in inclusion}
    # stdout.write(f"Inclusion map {inclusion_map} entries.\n")

    # Step 1: Copy all rows from MANUAL_MEMBERSHIP
    Membership.objects.bulk_create([Membership(
        problem=data["problem"],
        com_class=data["com_class"],
        method=methods['manual']
    ) for data in manual_membership])

    # For each (problem, class) in membership, propagate via inclusion
    # We'll use a queue to process new (problem, class) pairs
    membership = set((d["problem"], d["com_class"]) for d in manual_membership)
    queue = deque(membership)
    seen = membership

    while queue:
        problem, c_prime = queue.popleft()
        try: 
            row1 = Membership.objects.get(problem=problem, com_class=c_prime)
        except Membership.DoesNotExist:
            stdout.write(f"Warning: Membership not found for ({problem.AB}, {c_prime.AB}). Skipping.\n")
            continue
        
        for c in inclusion_map.get(c_prime.AB, []):
            if (problem, c) not in seen:
                try: 
                    row2 = Inclusion.objects.get(lower=c_prime, upper=c)
                    membership.add((problem, c))
                    queue.append((problem, c))
                    seen.add((problem, c))
                    Membership.objects.get_or_create(
                        problem=problem,
                        com_class=c,
                        method=methods['trans'],
                        row1=row1,
                        row2=row2
                    )
                except Inclusion.DoesNotExist:
                    stdout.write(f"Warning: Inclusion not found for ({c_prime}, {c}) in problem {problem}. Skipping.\n")
                    continue

    return {(m.problem, m.com_class): m for m in Membership.objects.all()}


def populate_non_memberships(manual_non_membership, methods):
    NonMembership.objects.bulk_create([NonMembership(
        problem=data["problem"],
        com_class=data["com_class"],
        method=methods['manual']
    ) for data in manual_non_membership])

    inclusion = Inclusion.objects.all().select_related('upper', 'lower')
    reverse_inclusion_map = defaultdict(set)
    # Build inclusion map: upper -> set of lower
    # This is the reverse of the inclusion map used in populate_memberships
    for inc in inclusion:
        try:
            reverse_inclusion_map[inc.upper.AB].add(inc.lower)
        except Inclusion.DoesNotExist:
            stdout.write(f"Warning: Inclusion not found for ({inc.lower}, {inc.upper}). Skipping.\n")
            continue

    # Step 1: Copy all rows from MANUAL NONMEMBERSHIP
    non_membership = set((d["problem"], d["com_class"]) for d in manual_non_membership)
    queue = deque(non_membership)
    seen = set(non_membership)

    # Step 2: Propagate via reverse inclusion
    while queue:
        problem, c_prime = queue.popleft()
        try: 
            row1 = NonMembership.objects.get(problem=problem, com_class=c_prime)
        except NonMembership.DoesNotExist:
            stdout.write(f"Warning: NonMembership not found for ({problem}, {c_prime}). Skipping.\n")
            continue
        for c in reverse_inclusion_map.get(c_prime.AB, []):
            if (problem, c) not in seen:
                try:
                    row2 = Inclusion.objects.get(lower=c, upper=c_prime)
                    non_membership.add((problem, c))
                    queue.append((problem, c))
                    NonMembership.objects.get_or_create(
                        problem=problem,
                        com_class=c,
                        method=methods['trans'],
                        row1=row1,
                        row2=row2
                    )
                except Inclusion.DoesNotExist:
                    stdout.write(f"Warning: Inclusion not found for ({c}, {c_prime}) in problem {problem}. Skipping.\n")
                    continue
                seen.add((problem, c))

    return {(m.problem, m.com_class): m for m in NonMembership.objects.all()}


from django.db import connection
from comweb.models import MMG, MTG, AutoInclusion, Class, Inclusion, ManualInclusion, Method

def populate_methods(method_data):
    """Populate the Method table with predefined methods."""
    Method.objects.bulk_create([Method(**data) for data in method_data])

def machine_mode_le(mode1, mode2, mmg_pairs):
    """Check if mode1 is less than or equal to mode2."""
    if mode1.id == mode2.id:
        return True
    return (mode1.id, mode2.id) in mmg_pairs

def machine_type_le(type1, type2, mtg_pairs):
    """Check if type1 is less than or equal to type2."""
    if type1.id == type2.id:
        return True
    return (type1.id, type2.id) in mtg_pairs
    

def populate_inclusions(manual_inclusions): 
    all_classes = list(Class.objects.select_related(
        'problem_type', 
        'machine', 
        'machine__mode', 
        'machine__type',
        'time_bound', 
        'space_bound', 
        'alternations_bound'
    ))

    # Build lookup tables for MMG and MTG
    mmg_pairs = set((mmg.lower_id, mmg.upper_id) for mmg in MMG.objects.all())
    mtg_pairs = set((mtg.lower_id, mtg.upper_id) for mtg in MTG.objects.all())
    methods = {m.AB: m for m in Method.objects.all()}

    def get_method(c1, c2, mmg_pairs, mtg_pairs, methods): 
        """Determine the method based on the generalization type."""
        if (c1.machine.mode_id, c2.machine.mode_id) in mmg_pairs:
            return methods.get("MMG")
        elif (c1.machine.type_id, c2.machine.type_id) in mtg_pairs:
            return methods.get("MTG")
        return methods.get("RBG")

    for c1 in all_classes: 
        for c2 in all_classes: 
            if c1 == c2 or c1.co_class == c2: 
                continue  # Skip self-comparisons and co-class comparisons
            try:
                mode_le = machine_mode_le(c1.machine.mode, c2.machine.mode, mmg_pairs)
                type_le = machine_type_le(c1.machine.type, c2.machine.type, mtg_pairs)
                time_bound_le = (c1.time_bound is None or c2.time_bound is None or 
                               c1.time_bound.order <= c2.time_bound.order)
                space_bound_le = (c1.space_bound.order <= c2.space_bound.order)
                alternations_bound_le = (c1.alternations_bound.order <= c2.alternations_bound.order)
                
                le = (c1.problem_type_id == c2.problem_type_id and
                     mode_le and type_le and
                     time_bound_le and space_bound_le and alternations_bound_le)

                if le: # ensure c1, c2 are not co-classes
                    auto_inc = AutoInclusion.objects.get_or_create(
                        lower=c1,
                        upper=c2,
                        method=get_method(c1, c2, mmg_pairs, mtg_pairs, methods)
                    )[0]
                    # Also create an Inclusion for each AutoInclusion
                    Inclusion.objects.get_or_create(
                        lower=c1,
                        upper=c2,
                        method=get_method(c1, c2, mmg_pairs, mtg_pairs, methods)
                    )
            except AttributeError as e:
                print(f"Error processing classes {c1.AB} and {c2.AB}: {e}")

    populate_manual_inclusions(manual_inclusions)
    # Add manual inclusions to the Inclusion table
    for manual_inc in manual_inclusions:
        Inclusion.objects.get_or_create(
            lower=manual_inc["lower"],
            upper=manual_inc["upper"],
            method=methods.get("manual"),
        )    
    
    # Get all classes and create an adjacency matrix
    classes = list(Class.objects.all())
    n = len(classes)
    class_to_idx = {c.id: i for i, c in enumerate(classes)}
    idx_to_class = {i: c for i, c in enumerate(classes)}
    
    # Initialize adjacency matrix and path reconstruction matrix
    adj_matrix = [[False] * n for _ in range(n)]
    path = [[None] * n for _ in range(n)]  # Store the intermediate paths
    
    # Fill the adjacency matrix with existing inclusions
    inclusions = list(Inclusion.objects.all())
    for inc in inclusions:
        i = class_to_idx[inc.lower_id]
        j = class_to_idx[inc.upper_id]
        if inc.lower.co_class.id == inc.upper_id:
            # If co-C ⊆ C, then add C ⊆ co-C
            adj_matrix[j][i] = True
            path[j][i] = inc
            new_inclusion = Inclusion.objects.create(
                lower=inc.upper,
                upper=inc.lower,
                method= methods.get("comp"),
            )
        adj_matrix[i][j] = True
        path[i][j] = inc
    
    # Floyd-Warshall algorithm for transitive closure
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not adj_matrix[i][j] and adj_matrix[i][k] and adj_matrix[k][j] and i != j:
                    # Found a new transitive relationship
                    adj_matrix[i][j] = True
                    
                    # Create new inclusion using transitivity
                    new_inclusion = Inclusion.objects.create(
                        lower=idx_to_class[i],
                        upper=idx_to_class[j],
                        method=methods.get("trans"),
                        row1=path[i][k],  # First inclusion used
                        row2=path[k][j]   # Second inclusion used
                    )
                    path[i][j] = new_inclusion
    
    # if co-C ⊆  C then add C ⊆ co-C and vice versa

    

# def populate_manual_inclusions(manual_inclusion_data):
#     ManualInclusion.objects.bulk_create([ManualInclusion(**data) for data in manual_inclusion_data])

def populate_manual_inclusions(manual_inclusion_data):
    # Remove references from the dicts for bulk_create
    manual_inclusion_objs = []
    references_map = []
    for data in manual_inclusion_data:
        refs = data.pop('references', None)
        manual_inclusion_objs.append(ManualInclusion(**data))
        references_map.append(refs)

    # Bulk create ManualInclusion objects
    created_objs = ManualInclusion.objects.bulk_create(manual_inclusion_objs)

    # Set references for each created object
    for obj, refs in zip(created_objs, references_map):
        if refs:
            # refs is a tuple (object, created), so use refs[0]
            obj.references.set([refs[0]])
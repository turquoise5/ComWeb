from comweb.models import MMG, MTG, AutoInclusion, Class, Method

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
    

def populate_auto_inclusions(): 
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

                if le and c1 != c2:
                    AutoInclusion.objects.get_or_create(
                        lower=c1,
                        upper=c2,
                        method=get_method(c1, c2, mmg_pairs, mtg_pairs, methods)
                    )
            except AttributeError as e:
                print(f"Error processing classes {c1.AB} and {c2.AB}: {e}")



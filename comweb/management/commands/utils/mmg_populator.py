from django.db import connection
from comweb.models import MMG, ManualMMG
from comweb.management.commands.mmg_mtg_data import get_manual_mmg

def populate_mmg():
    # Create manual entries
    manual_mmg_data = get_manual_mmg()
    ManualMMG.objects.bulk_create([ManualMMG(**data) for data in manual_mmg_data])

    MMG.objects.bulk_create([
        MMG(
            lower_id=data['lower'].id,
            upper_id=data['upper'].id,
            method="manual",
            row1=None,  
            row2=None   
        ) for data in manual_mmg_data
    ])

    # Compute closure while tracking sources
    while True:
        new_pairs = []
        existing = set(
            (mmg.lower_id, mmg.upper_id) 
            for mmg in MMG.objects.all()
        )
        
        # For each pair of existing MMG relationships
        all_mmgs = list(MMG.objects.all())
        for mmg1 in all_mmgs:
            for mmg2 in all_mmgs:
                # If upper of first matches lower of second
                if mmg1.upper_id == mmg2.lower_id:
                    new_pair = (mmg1.lower_id, mmg2.upper_id)
                    
                    # If this is a new transitive relationship
                    if new_pair not in existing and new_pair[0] != new_pair[1]:
                        new_pairs.append({
                            'lower_id': new_pair[0],
                            'upper_id': new_pair[1],
                            'row1': mmg1,  # Track the source relationships
                            'row2': mmg2
                        })

        # If no new pairs found, we're done
        if not new_pairs:
            break

        MMG.objects.bulk_create([
            MMG(
                lower_id=pair['lower_id'],
                upper_id=pair['upper_id'],
                method="transitivity",
                row1=pair['row1'],
                row2=pair['row2']
            ) for pair in new_pairs
        ])
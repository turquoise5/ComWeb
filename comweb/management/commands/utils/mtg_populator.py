from django.db import connection
from comweb.models import MTG, ManualMTG
from comweb.management.commands.data.mmg_mtg_data import get_manual_mtg

def populate_mtg():
    # Create manual entries
    manual_mtg_data = get_manual_mtg()
    ManualMTG.objects.bulk_create([ManualMTG(**data) for data in manual_mtg_data])

    # Create initial MTG entries from manual ones
    MTG.objects.bulk_create([
        MTG(
            lower_id=data['lower'].id,
            upper_id=data['upper'].id,
            method=data['justification'],
            row1=None,
            row2=None
        ) for data in manual_mtg_data
    ])

    # Compute closure while tracking sources
    while True:
        new_pairs = []
        existing = set(
            (mtg.lower_id, mtg.upper_id) 
            for mtg in MTG.objects.all()
        )
        
        # For each pair of existing MTG relationships
        all_mtgs = list(MTG.objects.all())
        for mtg1 in all_mtgs:
            for mtg2 in all_mtgs:
                # If upper of first matches lower of second
                if mtg1.upper_id == mtg2.lower_id:
                    new_pair = (mtg1.lower_id, mtg2.upper_id)
                    
                    # If this is a new transitive relationship
                    if new_pair not in existing and new_pair[0] != new_pair[1]:
                        new_pairs.append({
                            'lower_id': new_pair[0],
                            'upper_id': new_pair[1],
                            'row1': mtg1,  # Track the source relationships
                            'row2': mtg2
                        })

        # If no new pairs found, we're done
        if not new_pairs:
            break

        MTG.objects.bulk_create([
            MTG(
                lower_id=pair['lower_id'],
                upper_id=pair['upper_id'],
                method="transitivity",
                row1=pair['row1'],
                row2=pair['row2']
            ) for pair in new_pairs
        ])
from comweb.models import Machine, MachineType, MachineMode
    
def populate_machines(modes_data, types_data):    
    # Create basic types
    MachineType.objects.bulk_create([MachineType(**data) for data in types_data])
    MachineMode.objects.bulk_create([MachineMode(**data) for data in modes_data])
    
    # Cache lookups
    mode_objs = {m.NA: m for m in MachineMode.objects.all()}
    type_objs = {t.NA: t for t in MachineType.objects.all()}
    
    # Create machines (all combinations of modes and types)
    machines_data = []
    for mode in modes_data:
        for typ in types_data:
            # Ensure SO is two digits, since mode SO goes up to 9 and type SO goes up to 2
            mode_so = str(mode['SO']).zfill(2)
            type_so = str(typ['SO']).zfill(2)
                
            machines_data.append({
                "NA": f"{mode['NA']} {typ['NA']}" if mode['NA'] != "general" else typ['NA'],
                "AB": f"{mode['AB']}{typ['AB']}" if mode['AB'] != "*" else typ['AB'],
                "SO": int(f"{type_so}{mode_so}"),
                "mode": mode_objs[mode['NA']],
                "type": type_objs[typ['NA']]
            })
    
    Machine.objects.bulk_create([Machine(**data) for data in machines_data])
    return {m.NA: m for m in Machine.objects.all()}    
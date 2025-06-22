from comweb.models import Class, ProblemType, ResourceBound
from comweb.management.commands.data.class_data import get_class_data

def populate_classes(problem_type_data, bounds_data, machines):
    # Create basic types
    ProblemType.objects.bulk_create([ProblemType(**data) for data in problem_type_data])
    ResourceBound.objects.bulk_create([ResourceBound(**data) for data in bounds_data])

    # Cache lookups
    problem_types = {pt.NA: pt for pt in ProblemType.objects.all()}
    bounds = {b.AB: b for b in ResourceBound.objects.all()}

    class_data = get_class_data(problem_types, bounds, machines)
    Class.objects.bulk_create([Class(**data) for data in class_data])
    Class.objects.bulk_create([Class(
        NA="co-" + data['NA'],
        AB="co-" +data['AB'],
        problem_type=data['problem_type'],
        machine=data['machine'],
        co=True,
        co_class=Class.objects.get(AB=data['AB']),
        time_bound=data.get('time_bound', bounds['inf']),
        space_bound=data.get('space_bound', bounds['inf']),
        alternations_bound=data.get('alternations_bound', bounds['inf'])
    ) for data in class_data])

    for c in Class.objects.all():
        if not c.co:
            c.co_class = Class.objects.get(AB="co-" + c.AB)
            c.save()

    return {c.AB: c for c in Class.objects.all()}
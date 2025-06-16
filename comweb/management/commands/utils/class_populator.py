from comweb.models import Class, ProblemType, ResourceBound
from comweb.management.commands.class_data import get_class_data

def populate_classes(problem_type_data, bounds_data, machines):
    # Create basic types
    ProblemType.objects.bulk_create([ProblemType(**data) for data in problem_type_data])
    ResourceBound.objects.bulk_create([ResourceBound(**data) for data in bounds_data])

    # Cache lookups
    problem_types = {pt.NA: pt for pt in ProblemType.objects.all()}
    bounds = {b.AB: b for b in ResourceBound.objects.all()}

    class_data = get_class_data(problem_types, bounds, machines)
    Class.objects.bulk_create([Class(**data) for data in class_data])
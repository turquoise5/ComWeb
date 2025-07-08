from comweb.models import Problem

def populate_problems(problems): 
    Problem.objects.bulk_create([Problem(**problem) for problem in problems])
    Problem.objects.bulk_create([Problem(
        NA="co-" + problem['NA'], 
        AB="co-" + problem['AB'], 
        TY=problem['TY'],
        DE="Complement of the problem: " + problem['DE'], 
        co=True, 
        co_problem=Problem.objects.get(AB=problem['AB'])
    ) for problem in problems])

    for p in Problem.objects.all():
        if not p.co:
            p.co_problem = Problem.objects.get(AB="co-" + p.AB)
            p.save()

    return {p.AB: p for p in Problem.objects.all()}
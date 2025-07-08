from django.core.management.base import BaseCommand
from django.db import connection
from comweb.management.commands.data.manual_inclusions_data import get_manual_inclusions
from comweb.management.commands.data import memberships_data, references_data
from comweb.management.commands.data.problem_data import get_problem_data
from comweb.management.commands.utils.class_populator import populate_classes
from comweb.management.commands.utils.inclusion_populator import populate_inclusions, populate_methods
from comweb.management.commands.utils.machine_populator import populate_machines
from comweb.management.commands.utils.memberships_populator import populate_memberships, populate_non_memberships
from comweb.management.commands.utils.mmg_populator import populate_mmg
from comweb.management.commands.utils.mtg_populator import populate_mtg
from comweb.management.commands.utils.non_inclusions_populator import populate_non_inclusions
from comweb.management.commands.utils.problem_populator import populate_problems
from comweb.models import *
from comweb.management.commands.data.static_data import types_data, modes_data, problem_type_data, bounds_data, method_data

class Command(BaseCommand):
    help = 'Deletes and repopulates the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting...'))
        
        # delete everything
        MachineMode.objects.all().delete()
        MachineType.objects.all().delete()
        Machine.objects.all().delete()
        ProblemType.objects.all().delete()
        ResourceBound.objects.all().delete()
        Class.objects.all().delete()
        ManualMTG.objects.all().delete()
        ManualMMG.objects.all().delete()
        MTG.objects.all().delete()
        MMG.objects.all().delete()
        Method.objects.all().delete()
        Reference.objects.all().delete()
        ManualInclusion.objects.all().delete()
        Inclusion.objects.all().delete()
        Problem.objects.all().delete()
        ManualMembership.objects.all().delete()
        Membership.objects.all().delete()
        ManualNonMembership.objects.all().delete()
        NonMembership.objects.all().delete()
        ManualNonInclusion.objects.all().delete()
        NonInclusion.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Database reset successfully.'))
        
        machines = populate_machines(modes_data, types_data)
        classes_dict = populate_classes(problem_type_data, bounds_data, machines)
        populate_mmg()
        populate_mtg()
        populate_methods(method_data)
        
        # Reference.objects.bulk_create([Reference(**data) for data in references_data])
        # references_dict = {r.DE: r for r in Reference.objects.all()}
        # FIX Reference IMPLEMENTATION
        manual_inclusions = get_manual_inclusions(classes_dict) 
        all_inclusions = populate_inclusions(manual_inclusions) 
        
        problem_type_dict = {pt.NA: pt for pt in ProblemType.objects.all()}
        problems = get_problem_data(problem_type_dict)
        populate_problems(problems)   
        problem_dict = {p.AB: p for p in Problem.objects.all()}                
        
        methods_dict = {m.AB: m for m in Method.objects.all()}
        memberships = memberships_data.get_manual_memberships(problem_dict, classes_dict)
        non_memberships = memberships_data.get_manual_non_memberships(problem_dict, classes_dict)
        ManualMembership.objects.bulk_create([ManualMembership(**data) for data in memberships])
        ManualNonMembership.objects.bulk_create([ManualNonMembership(**data) for data in non_memberships])
        
        # do transitive closure of non/memberships
        memberships = populate_memberships(manual_memberships, methods_dict)
        non_memberships = populate_non_memberships(manual_non_memberships, methods_dict)
        populate_non_inclusions()

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
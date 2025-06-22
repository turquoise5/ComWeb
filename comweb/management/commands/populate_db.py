from django.core.management.base import BaseCommand
from django.db import connection
from comweb.management.commands.data.manual_inclusions_data import get_manual_inclusions
from comweb.management.commands.utils.class_populator import populate_classes
from comweb.management.commands.utils.inclusion_populator import populate_inclusions, populate_methods
from comweb.management.commands.utils.machine_populator import populate_machines
from comweb.management.commands.utils.mmg_populator import populate_mmg
from comweb.management.commands.utils.mtg_populator import populate_mtg
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
        AutoInclusion.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Database reset successfully.'))
        
        machines = populate_machines(modes_data, types_data)
        classes = populate_classes(problem_type_data, bounds_data, machines)
        populate_mmg()
        populate_mtg()
        populate_methods(method_data)
        manual_inclusions = get_manual_inclusions(classes)
        populate_inclusions(manual_inclusions)                    
        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
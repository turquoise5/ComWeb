from django.core.management.base import BaseCommand
from comweb.models import MachineMode, MachineType, Machine, Resource, ResourceBound, ProblemType, Class

class Command(BaseCommand):
    help = 'Deletes and repopulates the database'

    def handle(self, *args, **options):
        modes_data = [
            {"NA": "deterministic", "AB": "D", "SO": 0},
            {"NA": "non-deterministic", "AB": "N", "SO": 1},
            {"NA": "alternating", "AB": "A", "SO": 2},
            {"NA": "lasvegas", "AB": "P0", "SO": 3}, 
            {"NA": "montecarlo", "AB": "P1", "SO": 4},
            {"NA": "bounded error", "AB": "P2", "SO": 5},
            {"NA": "probabilistic", "AB": "P", "SO": 6},
            {"NA": "quantum", "AB": "Q", "SO": 7},
            {"NA": "general", "AB": "*", "SO": 9},
        ]
        types_data = [
            {"NA": "Turing machine", "AB": "TM", "SO": 2},
            {"NA": "finite automata", "AB": "FA", "SO": 0},
            {"NA": "pushdown automata", "AB": "PA", "SO": 1}
        ]

        # Clear existing data
        MachineMode.objects.all().delete()
        MachineType.objects.all().delete()
        Machine.objects.all().delete()

        # Insert new data
        MachineType.objects.bulk_create([MachineType(**data) for data in types_data])
        MachineMode.objects.bulk_create([MachineMode(**data) for data in modes_data])

        machines_data = []
        # Create all combinations of modes and types to get machines
        for mode in modes_data:
            for typ in types_data:
                machines_data.append(
                    {
                        "NA": f"{mode['NA']} {typ['NA']}",
                        "AB": f"{mode['AB']}-{typ['AB']}",
                        "SO": mode["SO"] + typ["SO"],
                        "mode": MachineMode.objects.get(NA=mode['NA']),
                        "machine_type": MachineType.objects.get(NA=typ['NA'])
                    }
                )

        Machine.objects.bulk_create([Machine(**data) for data in machines_data])

        resource_data = [
            {'NA': 'time', 'SO': 0},
            {'NA': 'space', 'SO': 1},
            {'NA': '# of alternations', 'SO': 2},
            {'NA': '# of states', 'SO': 3},
            {'NA': 'size', 'SO': 4}
        ]

        problem_type_data = [
            {'NA': 'decision problem', 'SO': 0},
            {'NA': 'function problem', 'SO': 1},
            {'NA': 'search problem', 'SO': 2},
            {'NA': 'counting problem', 'SO': 3}
        ]
        
        bounds_data = [
            {'NA': 'infinity', 'AB': 'inf', 'SO': '14', 'order': '14'}, 
            {'NA': 'recursive', 'AB': 'rec', 'SO': '13', 'order': '13'},
            {'NA': 'elementary', 'AB': 'elem', 'SO': '12', 'order': '12'},
            {'NA': 'doubly exponential', 'AB': '2-exp', 'SO': '11', 'order': '11'},
            {'NA': 'exponential', 'AB': 'exp', 'SO': '10', 'order': '10'}, 
            {'NA': 'polynomial', 'AB': 'poly', 'SO': '9', 'order': '9'},
            {'NA': 'linear', 'AB': 'lin', 'SO': '8', 'order': '8'},            
            {'NA': 'poly logarithmic', 'AB': 'polylog', 'SO': '7', 'order': '7'}, 
            {'NA': 'logarthmic', 'AB': 'log', 'SO': '6', 'order': '6'},
            {'NA': 'log-logarthmic', 'AB': 'loglog', 'SO': '5', 'order': '5'},
            {'NA': 'constant', 'AB': 'const', 'SO': '4', 'order': '4'}, 
            {'NA': 'three', 'AB': '3', 'SO': '3', 'order': '3'}, 
            {'NA': 'two', 'AB': '2', 'SO': '2', 'order': '2'}, 
            {'NA': 'one', 'AB': '1', 'SO': '1', 'order': '1'},
            {'NA': 'zero', 'AB': '0', 'SO': '0', 'order': '0'} 
        ]

        Resource.objects.all().delete()
        ProblemType.objects.all().delete()
        ResourceBound.objects.all().delete()

        Resource.objects.bulk_create([Resource(**data) for data in resource_data])
        ProblemType.objects.bulk_create([ProblemType(**data) for data in problem_type_data])
        ResourceBound.objects.bulk_create([ResourceBound(**data) for data in bounds_data])

        class_data = [
            {
                'NA': 'Deterministic Regular',
                'AB': 'D-REGULAR',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic finite automata'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(NA='linear')
            },
            {
                'NA': 'Non-deterministic Regular',
                'AB': 'N-REGULAR',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic finite automata'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(NA='linear')
            },
            {
                'NA': 'Deterministic Context-Free',
                'AB': 'D-CONTEXT-FREE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic pushdown automata'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='lin'),
            },
            {
                'NA': 'Non-deterministic Context-Free',
                'AB': 'N-CONTEXT-FREE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic pushdown automata'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='lin'),
            },
            {
                'NA': 'Decidable',
                'AB': 'DECIDABLE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='rec'),
            },
            {
                'NA': 'Recognizable',
                'AB': 'RECOGNIZABLE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='inf'),
            },
            
            {
                'NA': 'Deterministic Polynomial Time',
                'AB': 'P',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'Nondeterministic Polynomial Time',
                'AB': 'NP',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'First Level Polynomial Hierarchy',
                'AB': 'Sigma_1^P',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='alternating Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
                'resource2': Resource.objects.get(NA='# of alternations'),
                'bound2': ResourceBound.objects.get(AB='1')
            },
            {
                'NA': 'Second Level Polynomial Hierarchy',
                'AB': 'Sigma_2^P',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='alternating Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
                'resource2': Resource.objects.get(NA='# of alternations'),
                'bound2': ResourceBound.objects.get(AB='2')
            },
            {
                'NA': 'Alternating Polynomial Time',
                'AB': 'AP',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='alternating Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'Deterministic Exponential Time',
                'AB': 'EXP',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='exp'),
            },
            {
                'NA': 'Nondeterministic Exponential Time',
                'AB': 'NEXP',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='exp'),
            },  
            {
                'NA': 'Deterministic Logarithmic Space',
                'AB': 'L',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='log'),
            },
            {
                'NA': 'Nondeterministic Logarithmic Space',
                'AB': 'NL',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='log'),
            },
            {
                'NA': 'Alternating Log Space',
                'AB': 'AL',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='alternating Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='log'),
            },
            {
                'NA': 'Polynomial Space',
                'AB': 'PSPACE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'Nondeterministic Polynomial Space',
                'AB': 'NPSPACE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'Alternating Polynomial Space',
                'AB': 'APSPACE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='alternating Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'Deterministic Exponential Space',
                'AB': 'EXPSPACE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='exp'),
            },
            {
                'NA': 'Nondeterministic Exponential Space',
                'AB': 'NEXPSPACE',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='non-deterministic Turing machine'),
                'resource1': Resource.objects.get(NA='space'),
                'bound1': ResourceBound.objects.get(AB='exp'),
            },
            {
                'NA': 'Bounded-error Probabilistic Polynomial Time',
                'AB': 'BPP',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='probabilistic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'Randomized Polynomial Time',
                'AB': 'RP',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='probabilistic Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
            {
                'NA': 'Quantum Polynomial Time',
                'AB': 'BQP',
                'problem_type': ProblemType.objects.get(NA='decision problem'),
                'machine': Machine.objects.get(NA='quantum Turing machine'),
                'resource1': Resource.objects.get(NA='time'),
                'bound1': ResourceBound.objects.get(AB='poly'),
            },
        ]

        Class.objects.all().delete()
        Class.objects.bulk_create([Class(**data) for data in class_data])


        self.stdout.write(self.style.SUCCESS('Database has been reset and populated.'))
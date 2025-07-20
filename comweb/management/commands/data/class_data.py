def get_class_data(problem_types, bounds, machines): 
    return ([
            #################################################################
            ########## COMPUTABILITY ########################################
            #################################################################
            {
                'NA': 'Deterministic Regular',
                'AB': 'D-REGULAR',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic finite automaton'],
                'time_bound': bounds['inf'],
            },
            {
                'NA': 'Non-deterministic Regular',
                'AB': 'N-REGULAR',
                'problem_type': problem_types['decision problem'],
                'machine': machines['non-deterministic finite automaton'],
                'time_bound': bounds['inf'],
            },
            {
                'NA': 'Deterministic Context-Free',
                'AB': 'D-CONTEXT-FREE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic pushdown automaton'],
                'time_bound': bounds['inf'],
            },
            {
                'NA': 'Non-deterministic Context-Free',
                'AB': 'N-CONTEXT-FREE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['non-deterministic pushdown automaton'],
                'time_bound': bounds['inf'],
            },
            {
                'NA': 'Decidable',
                'AB': 'DECIDABLE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic Turing machine'],
                'time_bound': bounds['finite'],
            },
            {
                'NA': 'Recognizable',
                'AB': 'RECOGNIZABLE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic Turing machine'],
                'time_bound': bounds['inf'],
            },
            #################################################################
            ########## COMPLEXITY ###########################################
            #################################################################
            {
                'NA': 'Deterministic Polynomial Time',
                'AB': 'P',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic Turing machine'],
                'time_bound': bounds['poly'],
            },
            {
                'NA': 'Nondeterministic Polynomial Time',
                'AB': 'NP',
                'problem_type': problem_types['decision problem'],
                'machine': machines['non-deterministic Turing machine'],
                'time_bound': bounds['poly'],
            },
            {
                'NA': 'First Level Polynomial Hierarchy',
                'AB': 'Sigma_1^P',
                'problem_type': problem_types['decision problem'],
                'machine': machines['alternating Turing machine'],
                'time_bound': bounds['poly'],
                'alternations_bound': bounds['1']                
            },
            {
                'NA': 'Second Level Polynomial Hierarchy',
                'AB': 'Sigma_2^P',
                'problem_type': problem_types['decision problem'],
                'machine': machines['alternating Turing machine'],
                'time_bound': bounds['poly'],
                'alternations_bound': bounds['2']
            },
            {
                'NA': 'Alternating Polynomial Time',
                'AB': 'AP',
                'problem_type': problem_types['decision problem'],
                'machine': machines['alternating Turing machine'],
                'time_bound': bounds['poly'],
                'alternations_bound': bounds['finite']
            },
            {
                'NA': 'Deterministic Exponential Time',
                'AB': 'EXP',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic Turing machine'],
                'time_bound': bounds['exp'],

            },
            {
                'NA': 'Nondeterministic Exponential Time',
                'AB': 'NEXP',
                'problem_type': problem_types['decision problem'],
                'machine': machines['non-deterministic Turing machine'],
                'time_bound': bounds['exp'],
            },
            {
                'NA': 'Deterministic Logarithmic Space',
                'AB': 'L',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic Turing machine'],
                'space_bound': bounds['log'],
            },
            {
                'NA': 'Nondeterministic Logarithmic Space',
                'AB': 'NL',
                'problem_type': problem_types['decision problem'],
                'machine': machines['non-deterministic Turing machine'],
                'space_bound': bounds['log'],
            },
            {
                'NA': 'Alternating Log Space',
                'AB': 'AL',
                'problem_type': problem_types['decision problem'],
                'machine': machines['alternating Turing machine'],
                'space_bound': bounds['log'],
            },
            {
                'NA': 'Polynomial Space',
                'AB': 'PSPACE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic Turing machine'],
                'space_bound': bounds['poly'],
            },
            {
                'NA': 'Nondeterministic Polynomial Space',
                'AB': 'NPSPACE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['non-deterministic Turing machine'],
                'space_bound': bounds['poly'],
            },
            {
                'NA': 'Alternating Polynomial Space',
                'AB': 'APSPACE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['alternating Turing machine'],
                'space_bound': bounds['poly'],
            },
            {
                'NA': 'Deterministic Exponential Space',
                'AB': 'EXPSPACE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['deterministic Turing machine'],
                'space_bound': bounds['exp'],
            },
            {
                'NA': 'Nondeterministic Exponential Space',
                'AB': 'NEXPSPACE',
                'problem_type': problem_types['decision problem'],
                'machine': machines['non-deterministic Turing machine'],
                'space_bound': bounds['exp'],
            },
            {
                'NA': 'Bounded-error Probabilistic Polynomial Time',
                'AB': 'BPP',
                'problem_type': problem_types['decision problem'],
                'machine': machines['probabilistic Turing machine'],
                'time_bound': bounds['poly'],
            },
            {
                'NA': 'Randomized Polynomial Time',
                'AB': 'RP',
                'problem_type': problem_types['decision problem'],
                'machine': machines['probabilistic Turing machine'],
                'time_bound': bounds['poly'],
            },
            {
                'NA': 'Quantum Polynomial Time',
                'AB': 'BQP',
                'problem_type': problem_types['decision problem'],
                'machine': machines['quantum Turing machine'],
                'time_bound': bounds['poly'],
            },
        ])

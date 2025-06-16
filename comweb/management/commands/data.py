# defines data to be inserted into the database
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
            {"NA": "finite automaton", "AB": "FA", "SO": 0},
            {"NA": "pushdown automaton", "AB": "PA", "SO": 1},
            {"NA": "linear bounded automaton", "AB": "LBA", "SO": 1}
        ]

problem_type_data = [
            {'NA': 'decision problem', 'SO': 0, "order": 0},
            {'NA': 'function problem', 'SO': 1, "order": 1},
            {'NA': 'search problem', 'SO': 2, "order": 3},
            {'NA': 'counting problem', 'SO': 3, "order": 2},
        ]

bounds_data = [
            {'NA': 'infinity', 'AB': 'inf', 'SO': '15', 'order': '15'}, 
            {'NA': 'finite', 'AB': 'finite', 'SO': '14', 'order': '14'}, 
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

method_data = [
            {
                "NA": "machine-mode generalization",
                "AB": "MMG",
                "SO": 0,
                "DE": "Proving inclusion by generalizing the machine mode (e.g., deterministic to non-deterministic: DTM < NTM)."
            },
            {
                "NA": "resource-bound generalization",
                "AB": "RBG",
                "SO": 1,
                "DE": "Proving inclusion by relaxing the resource bound (e.g., polynomial to exponential time)."
            },
            {
                "NA": "problem-type generalization",
                "AB": "PTG",
                "SO": 2,
                "DE": "Proving inclusion by generalizing the problem type (e.g., decision to search)."
            },
            {
                "NA": "machine-type generalization",
                "AB": "MTG",
                "SO": 3,
                "DE": "Proving inclusion by generalizing the machine type (e.g., finite automaton to Turing machine)."
            },
        ]
        

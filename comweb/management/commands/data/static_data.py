# defines data to be inserted into the database
types_data = [
            { "AB": "FA",   "NA": "finite automaton",          "SO": 0 },
            { "AB": "PDA",  "NA": "pushdown automaton",        "SO": 1 },
            { "AB": "LBA",  "NA": "linear bounded automaton",  "SO": 2 },
            { "AB": "TM",   "NA": "Turing machine",            "SO": 3 }
        ]

modes_data = [
            { "AB": "D",   "NA": "deterministic",     "SO": 10 },
            { "AB": "N",   "NA": "nondeterministic",  "SO": 21 },
            { "AB": "A",   "NA": "alternating",       "SO": 22 },
            { "AB": "P0",  "NA": "Las Vegas",         "SO": 31 }, 
            { "AB": "P1",  "NA": "Monte Carlo",       "SO": 32 },
            { "AB": "P2",  "NA": "bounded-error",     "SO": 33 },
            { "AB": "P",   "NA": "probabilistic",     "SO": 34 },
            { "AB": "Q",   "NA": "quantum",           "SO": 41 },
            { "AB": "*",   "NA": "general",           "SO": 99 },
        ]

problem_type_data = [
            {"NA": "decision", "SO": 0, "order": 0},
            {"NA": "function", "SO": 1, "order": 1},
            {"NA": "search", "SO": 2, "order": 3},
            {"NA": "counting", "SO": 3, "order": 2},
        ]

bounds_data = [
            {"NA": "infinity", "AB": "inf", "SO": "15", "order": "15"}, 
            {"NA": "finite", "AB": "finite", "SO": "14", "order": "14"}, 
            {"NA": "recursive", "AB": "rec", "SO": "13", "order": "13"},
            {"NA": "elementary", "AB": "elem", "SO": "12", "order": "12"},
            {"NA": "doubly exponential", "AB": "2-exp", "SO": "11", "order": "11"},
            {"NA": "exponential", "AB": "exp", "SO": "10", "order": "10"}, 
            {"NA": "polynomial", "AB": "poly", "SO": "9", "order": "9"},
            {"NA": "linear", "AB": "lin", "SO": "8", "order": "8"},            
            {"NA": "poly logarithmic", "AB": "polylog", "SO": "7", "order": "7"}, 
            {"NA": "logarthmic", "AB": "log", "SO": "6", "order": "6"},
            {"NA": "log-logarthmic", "AB": "loglog", "SO": "5", "order": "5"},
            {"NA": "constant", "AB": "const", "SO": "4", "order": "4"}, 
            {"NA": "three", "AB": "3", "SO": "3", "order": "3"}, 
            {"NA": "two", "AB": "2", "SO": "2", "order": "2"}, 
            {"NA": "one", "AB": "1", "SO": "1", "order": "1"},
            {"NA": "zero", "AB": "0", "SO": "0", "order": "0"} 
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
            {
                "NA": "transitivity", 
                "AB": "trans",
                "SO": 4,
                "DE": "Proving inclusion by transitivity (e.g., if A ⊆ B and B ⊆ C, then A ⊆ C)."
            },
            {
                "NA": "manual",
                "AB": "manual",
                "SO": 5,
                "DE": "Inclusion added manually (a theorem; see references)."
            },
            {
                "NA": "Complementation Closure", 
                "AB": "comp", 
                "SO": 6, 
                "DE": "co-C is in C hence C is in co-C"
            }, 
            {
                "NA": "witness",
                "AB": "witness",
                "SO": 7, 
                "DE": "Witness problem non-inclusion"
            }
        ]

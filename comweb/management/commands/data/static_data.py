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
            { "NA": "decision", "SO": 10, "order": 10 },
            { "NA": "function", "SO": 20, "order": 20 },
            { "NA": "search",   "SO": 30, "order": 30 },
            { "NA": "counting", "SO": 50, "order": 21 },
        ]

bounds_data = [
            { "AB": "∞",       "NA": "unrestricted",       "SO": "99", "order": "99"}, 
            { "AB": "fin",     "NA": "finite",             "SO": "42", "order": "42"}, 
            { "AB": "rec",     "NA": "recursive",          "SO": "41", "order": "41"},
            { "AB": "elem",    "NA": "elementary",         "SO": "40", "order": "40"},
            { "AB": "2-exp",   "NA": "doubly-exponential", "SO": "31", "order": "31"},
            { "AB": "exp",     "NA": "exponential",        "SO": "30", "order": "30"}, 
            { "AB": "poly",    "NA": "polynomial",         "SO": "29", "order": "29"},
            { "AB": "cub",     "NA": "cubic",              "SO": "22", "order": "22"},            
            { "AB": "quad",    "NA": "quadratic",          "SO": "21", "order": "21"},            
            { "AB": "lin",     "NA": "linear",             "SO": "20", "order": "20"},            
            { "AB": "polylog", "NA": "polylogarithmic",    "SO": "12", "order": "12"}, 
            { "AB": "log",     "NA": "logarthmic",         "SO": "11", "order": "11"},
            { "AB": "loglog",  "NA": "log-logarthmic",     "SO": "10", "order": "10"},
            { "AB": "const",   "NA": "constant",           "SO":  "9", "order":  "9"}, 
            { "AB": "3",       "NA": "3",                  "SO":  "3", "order":  "3"}, 
            { "AB": "2",       "NA": "2",                  "SO":  "2", "order":  "2"}, 
            { "AB": "1",       "NA": "1",                  "SO":  "1", "order":  "1"},
            { "AB": "0",       "NA":  "0",                 "SO":  "0", "order":  "0"} 
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

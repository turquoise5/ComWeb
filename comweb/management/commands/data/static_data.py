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
                "AB": "manual",
                "NA": "manual",
                "DE": "This fact has been added manually.",
                "SO": 0,
            },
            {
                "AB": "MTG",
                "NA": "machine-type generalization",
                "DE": "A ⊆ B because the *machine type* for class B generalizes the one for class A.",
                "SO": 1,
            },
            {
                "AB": "MMG",
                "NA": "machine-mode generalization",
                "DE": "A ⊆ B because the *machine mode* for class B generalizes the one for class A.",
                "SO": 1,
            },
            {
                "AB": "RBG",
                "NA": "resource-bounds generalization",
                "DE": "A ⊆ B because the *resource bounds* for class B generalize the ones for class A.",
                "SO": 1,
            },
            {
                "AB": "PTG",
                "NA": "problem-type generalization",
                "DE": "A ⊆ B because the *problem type* for class B generalizes the one for class A.",
                "SO": 1,
            },
            {
                "AB": "INCL-X",
                "NA": "transitivity for inclusion", 
                "DE": "A ⊆ B because A ⊆ C & C ⊆ B for some intermediate class C.",
                "SO": 2,
            },
            {
                "AB": "MEMB-X",
                "NA": "transitivity for membership", 
                "DE": "X ∈ A because X ∈ C & C ⊆ A for some intermediate class C.",
                "SO": 2,
            },
            {
                "AB": "INCL-CO", 
                "NA": "complementation closure", 
                "DE": "A ⊆ co-A because co-A ⊆ A",
                "SO": 3, 
            }, 
            {
                "AB": "WTNSS",
                "NA": "witness",
                "DE": "A ⊈ B because X ∈ A & X ∉ B for some problem X.",
                "SO": 4, 
            }
        ]

def get_class_data(problem_types, bounds, machines): 
    return ([
            #################################################################
            ########## COMPUTABILITY 
            #################################################################
            {
                "AB"           : "REG",
                "NA"           : "(deterministic) regular",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["deterministic finite automaton"],
            },
            {
                "AB"           : "NREG",
                "NA"           : "nondeterministic regular",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["nondeterministic finite automaton"],
            },
            {
                "AB"           : "DCFL",
                "NA"           : "deterministic context-free",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["deterministic pushdown automaton"],
            },
            {
                "AB"           : "CFL",
                "NA"           : "(nondeterministic) context-free",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["nondeterministic pushdown automaton"],
            },
            {
                "AB"           : "R",
                "NA"           : "recursive / decidable",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["deterministic Turing machine"],
                "time_bound"   : bounds["finite"],
            },
            {
                "AB"           : "RE",
                "NA"           : "recursively enumerable / semidecidable",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["deterministic Turing machine"],
            },
            #################################################################
            ########## COMPLEXITY - time - deterministic 
            ################################################################# 
            {
                "AB"           : "P",
                "NA"           : "deterministic polynomial time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["deterministic Turing machine"],
                "time_bound"   : bounds["polynomial"],
            },
            {
                "AB"           : "EXP",
                "NA"           : "deterministic exponential time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["deterministic Turing machine"],
                "time_bound"   : bounds["exponential"],

            },            
            #################################################################
            ########## COMPLEXITY - time - alternating 
            ################################################################# 
            {
                "AB"           : "NP",
                "NA"           : "nondeterministic polynomial time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["nondeterministic Turing machine"],
                "time_bound"   : bounds["polynomial"],
            },
            {
                "AB"                 : "Σ_1^P",
                "NA"                 : "existential polynomial time",
                "problem_type"       : problem_types["decision"],
                "machine"            : machines["alternating Turing machine"],
                "time_bound"         : bounds["polynomial"],
                "alternations_bound" : bounds["1"]                
            },

            {
                "AB"                 : "Π_1^P",
                "NA"                 : "universal polynomial time",
                "problem_type"       : problem_types["decision"],
                "machine"            : machines["alternating Turing machine"],
                "time_bound"         : bounds["polynomial"],
                "alternations_bound" : bounds["1"]                
            },
            {
                "AB"                 : "Σ_2^P",
                "NA"                 : "existential-universal polynomial time",
                "problem_type"       : problem_types["decision"],
                "machine"            : machines["alternating Turing machine"],
                "time_bound"         : bounds["polynomial"],
                "alternations_bound" : bounds["2"]
            },
            {
                "AB"                 : "Π_2^P",
                "NA"                 : "universal-existential polynomial time",
                "problem_type"       : problem_types["decision"],
                "machine"            : machines["alternating Turing machine"],
                "time_bound"         : bounds["polynomial"],
                "alternations_bound" : bounds["2"]
            },
            {
                "AB"                 : "PH",
                "NA"                 : "polynomial hierarchy",
                "problem_type"       : problem_types["decision"],
                "machine"            : machines["alternating Turing machine"],
                "time_bound"         : bounds["polynomial"],
                "alternations_bound" : bounds["const"]
            },
            {
                "AB"                 : "AP",
                "NA"                 : "alternating polynomial time",
                "problem_type"       : problem_types["decision"],
                "machine"            : machines["alternating Turing machine"],
                "time_bound"         : bounds["polynomial"],
            },
            {
                "AB"           : "NEXP",
                "NA"           : "nondeterministic exponential time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["nondeterministic Turing machine"],
                "time_bound"   : bounds["exponential"],
            },
            #################################################################
            ########## COMPLEXITY - time - probabilistic 
            ################################################################# 
            {
                "AB"           : "ZPP",
                "NA"           : "zero-error probabilistic polynomial time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["probabilistic Turing machine"],
                "time_bound"   : bounds["polynomial"],
            },
            {
                "AB"           : "RP",
                "NA"           : "randomized polynomial time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["probabilistic Turing machine"],
                "time_bound"   : bounds["polynomial"],
            },
            {
                "AB"           : "BPP",
                "NA"           : "bounded-error probabilistic polynomial time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["probabilistic Turing machine"],
                "time_bound"   : bounds["polynomial"],
            },
            #################################################################
            ########## COMPLEXITY - time - quantum 
            ################################################################# 
            {
                "AB"           : "BQP",
                "NA"           : "quantum polynomial time",
                "problem_type" : problem_types["decision"],
                "machine"      : machines["quantum Turing machine"],
                "time_bound"   : bounds["polynomial"],
            },
            #################################################################
            ########## COMPLEXITY - space - deterministic 
            ################################################################# 
            {
                "AB": "L",
                "NA": "deterministic logarithmic space",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "space_bound": bounds["logarithmic"],
            },
            {
                "AB": "PSPACE",
                "NA": "deterministic polynomial space",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "space_bound": bounds["polynomial"],
            },
            {
                "AB": "EXPSPACE",
                "NA": "deterministic exponential space",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "space_bound": bounds["exponential"],
            },
            #################################################################
            ########## COMPLEXITY - space - alternating 
            ################################################################# 
            {
                "AB": "NL",
                "NA": "nondeterministic logarithmic space",
                "problem_type": problem_types["decision"],
                "machine": machines["nondeterministic Turing machine"],
                "space_bound": bounds["logarithmic"],
            },
            {
                "AB": "AL",
                "NA": "alternating logarithmic space",
                "problem_type": problem_types["decision"],
                "machine": machines["alternating Turing machine"],
                "space_bound": bounds["logarithmic"],
            },
            {
                "AB": "NPSPACE",
                "NA": "nondeterministic polynomial space",
                "problem_type": problem_types["decision"],
                "machine": machines["nondeterministic Turing machine"],
                "space_bound": bounds["polynomial"],
            },
            {
                "AB": "APSPACE",
                "NA": "alternating polynomial space",
                "problem_type": problem_types["decision"],
                "machine": machines["alternating Turing machine"],
                "space_bound": bounds["polynomial"],
            },
            {
                "AB": "NEXPSPACE",
                "NA": "nondeterministic exponential space",
                "problem_type": problem_types["decision"],
                "machine": machines["nondeterministic Turing machine"],
                "space_bound": bounds["exponential"],
            },
            #################################################################
            ########## COMPLEXITY - space - probabilistic ###################
            ################################################################# 
	    #
            #################################################################
            ########## COMPLEXITY - space - quantum #########################
            ################################################################# 
	    #
        ])

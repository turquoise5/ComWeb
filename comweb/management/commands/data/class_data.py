def get_class_data(problem_types, bounds, machines): 
    return ([
            #################################################################
            ########## COMPUTABILITY ########################################
            #################################################################
            {
                "AB"            : "D-REGULAR",
                "NA"            : "regular",
                "problem_type"  : problem_types["decision"],
                "machine"       : machines["deterministic finite automaton"],
                "time_bound"    : bounds["inf"],
            },
            {
                "AB": "N-REGULAR",
                "NA": "Non-deterministic Regular",
                "problem_type": problem_types["decision"],
                "machine": machines["non-deterministic finite automaton"],
                "time_bound": bounds["inf"],
            },
            {
                "AB": "D-CONTEXT-FREE",
                "NA": "Deterministic Context-Free",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic pushdown automaton"],
                "time_bound": bounds["inf"],
            },
            {
                "AB": "N-CONTEXT-FREE",
                "NA": "Non-deterministic Context-Free",
                "problem_type": problem_types["decision"],
                "machine": machines["non-deterministic pushdown automaton"],
                "time_bound": bounds["inf"],
            },
            {
                "AB": "DECIDABLE",
                "NA": "Decidable",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "time_bound": bounds["finite"],
            },
            {
                "AB": "RECOGNIZABLE",
                "NA": "Recognizable",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "time_bound": bounds["inf"],
            },
            #################################################################
            ########## COMPLEXITY - time - deterministic ####################
            ################################################################# 
            {
                "AB": "P",
                "NA": "Deterministic Polynomial Time",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "time_bound": bounds["poly"],
            },
            {
                "AB": "EXP",
                "NA": "Deterministic Exponential Time",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "time_bound": bounds["exp"],

            },            
            #################################################################
            ########## COMPLEXITY - time - alternating ######################
            ################################################################# 
            {
                "AB": "NP",
                "NA": "Nondeterministic Polynomial Time",
                "problem_type": problem_types["decision"],
                "machine": machines["non-deterministic Turing machine"],
                "time_bound": bounds["poly"],
            },
            {
                "AB": "Sigma_1^P",
                "NA": "First Level Polynomial Hierarchy",
                "problem_type": problem_types["decision"],
                "machine": machines["alternating Turing machine"],
                "time_bound": bounds["poly"],
                "alternations_bound": bounds["1"]                
            },
            {
                "AB": "Sigma_2^P",
                "NA": "Second Level Polynomial Hierarchy",
                "problem_type": problem_types["decision"],
                "machine": machines["alternating Turing machine"],
                "time_bound": bounds["poly"],
                "alternations_bound": bounds["2"]
            },
            {
                "AB": "AP",
                "NA": "Alternating Polynomial Time",
                "problem_type": problem_types["decision"],
                "machine": machines["alternating Turing machine"],
                "time_bound": bounds["poly"],
                "alternations_bound": bounds["finite"]
            },
            {
                "AB": "NEXP",
                "NA": "Nondeterministic Exponential Time",
                "problem_type": problem_types["decision"],
                "machine": machines["non-deterministic Turing machine"],
                "time_bound": bounds["exp"],
            },
            #################################################################
            ########## COMPLEXITY - time - probabilistic ####################
            ################################################################# 
            {
                "AB": "RP",
                "NA": "Randomized Polynomial Time",
                "problem_type": problem_types["decision"],
                "machine": machines["probabilistic Turing machine"],
                "time_bound": bounds["poly"],
            },
            {
                "AB": "BPP",
                "NA": "Bounded-error Probabilistic Polynomial Time",
                "problem_type": problem_types["decision"],
                "machine": machines["probabilistic Turing machine"],
                "time_bound": bounds["poly"],
            },
            #################################################################
            ########## COMPLEXITY - time - quantum ##########################
            ################################################################# 
            {
                "AB": "BQP",
                "NA": "Quantum Polynomial Time",
                "problem_type": problem_types["decision"],
                "machine": machines["quantum Turing machine"],
                "time_bound": bounds["poly"],
            },
            #################################################################
            ########## COMPLEXITY - space - deterministic ###################
            ################################################################# 
            {
                "AB": "L",
                "NA": "Deterministic Logarithmic Space",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "space_bound": bounds["log"],
            },
            {
                "AB": "PSPACE",
                "NA": "Polynomial Space",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "space_bound": bounds["poly"],
            },
            {
                "AB": "EXPSPACE",
                "NA": "Deterministic Exponential Space",
                "problem_type": problem_types["decision"],
                "machine": machines["deterministic Turing machine"],
                "space_bound": bounds["exp"],
            },
            #################################################################
            ########## COMPLEXITY - space - alternating #####################
            ################################################################# 
            {
                "AB": "NL",
                "NA": "Nondeterministic Logarithmic Space",
                "problem_type": problem_types["decision"],
                "machine": machines["non-deterministic Turing machine"],
                "space_bound": bounds["log"],
            },
            {
                "AB": "AL",
                "NA": "Alternating Log Space",
                "problem_type": problem_types["decision"],
                "machine": machines["alternating Turing machine"],
                "space_bound": bounds["log"],
            },
            {
                "AB": "NPSPACE",
                "NA": "Nondeterministic Polynomial Space",
                "problem_type": problem_types["decision"],
                "machine": machines["non-deterministic Turing machine"],
                "space_bound": bounds["poly"],
            },
            {
                "AB": "APSPACE",
                "NA": "Alternating Polynomial Space",
                "problem_type": problem_types["decision"],
                "machine": machines["alternating Turing machine"],
                "space_bound": bounds["poly"],
            },
            {
                "AB": "NEXPSPACE",
                "NA": "Nondeterministic Exponential Space",
                "problem_type": problem_types["decision"],
                "machine": machines["non-deterministic Turing machine"],
                "space_bound": bounds["exp"],
            },
            #################################################################
            ########## COMPLEXITY - space - probabilistic ###################
            ################################################################# 
        ])

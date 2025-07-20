def get_problem_data(problem_type_data): 
    problems = [
        {
            "AB": "ORDERED EQ_01", 
            "NA": "ordered equality of 0s and 1s", 
            "DE": "Given a binary string, check that it consists of some 0's followed by equally many 1's.", 
            "TY": problem_type_data["decision"],          
        }, 
        {
            "AB": "EQ_REX↑",
            "NA": "equivalence of regular expressions with exponentiation",
            "DE": "Given two regular expressions with exponentiation, check that they generate the same strings.",
            "TY": problem_type_data["decision"],
        },
        {
            "AB": "A_TM",
            "NA": "acceptance of Turing machines",
            "DE": "Given a Turing machine M and an input w, check that M accepts w.",
            "TY": problem_type_data["decision"],
        }, 
        {
            "AB": "HALT_ΤΜ",
            "NA": "termination of Turing machines (the Halting Problem)",
            "DE": "Given a Turing machine M and an input w, check that M halts on input w.",
            "TY": problem_type_data["decision"],
        },
        {
            "AB": "SAT",
            "NA": "satisfiability of Boolean formulas",
            "DE": "Given a boolean formula φ, check that there exists an assignment of truth values to the variables that makes φ true.",
            "TY": problem_type_data["decision"],
        },
        {
            "AB": "TQBF",
            "NA": "true quantified Boolean formulas",
            "DE": "Given a quantified Boolean formula φ, check that φ is true.",
            "TY": problem_type_data["decision"],
        },
    ]

    return problems

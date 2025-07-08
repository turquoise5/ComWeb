def get_problem_data(problem_type_data): 
    problems = [
        {
            "NA": "UNBOUNDED BINARY EQUALITY", 
            "AB": "UNBOUNDED BINARY EQUALITY", 
            "TY": problem_type_data["decision problem"], 
            "DE": "Decide whether there's an equal number of 0s and 1s in a string of the form 0^n1^n", 
        }, 
        {
            "NA": "Halting problem for a Turing machine",
            "AB": "HALTING",
            "TY": problem_type_data["decision problem"],
            "DE": "Given a Turing machine M and input w, decide whether M halts on w.",
        },
        {
            "NA": "Satisfiability of a boolean formula",
            "AB": "SAT",
            "TY": problem_type_data["decision problem"],
            "DE": "Given a boolean formula, decide whether there exists an assignment of variables that makes it true.",
        },
        {
            "NA": "True Quantified Boolean Formula",
            "AB": "TQBF",
            "TY": problem_type_data["decision problem"],
            "DE": "Decide whether a fully quantified boolean formula (with ∃ and ∀ quantifiers) is true.",
        },
        {
            "NA": "Acceptance problem for Turing Machines",
            "AB": "A_TM",
            "TY": problem_type_data["decision problem"],
            "DE": "Given a Turing machine M and input w, decide whether M accepts w.",
        }, 
        {
            "NA": "Equivalence of Regular Expressions",
            "AB": "EQ-REG-EXP",
            "TY": problem_type_data["decision problem"],
            "DE": "Given two regular expressions, decide whether they define the same language.",
        },
    ]

    return problems
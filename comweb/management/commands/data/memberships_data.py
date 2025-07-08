def get_manual_memberships(problem_data, class_data): 
    memberships = [
        {
            "problem": problem_data["SAT"],
            "com_class": class_data["NP"],
        },
        {
            "problem": problem_data["TQBF"],
            "com_class": class_data["PSPACE"],
        },
        # UNBOUNDED BINARY EQUALITY (0^n1^n|n>1)    in    D-CONTEXT-FREE
        {
            "problem": problem_data["UNBOUNDED BINARY EQUALITY"],
            "com_class": class_data["D-CONTEXT-FREE"],
        }, 
        # UNBOUNDED BINARY EQUALITY (0^n1^n|n>1)    in    P
        {
            "problem": problem_data["UNBOUNDED BINARY EQUALITY"],
            "com_class": class_data["P"],
        },
        # EQ-REG-EXP   in    EXPSPACE
        {
            "problem": problem_data["EQ-REG-EXP"],
            "com_class": class_data["EXPSPACE"],
        }, 
        # HALTING    in    RECOGNIZABLE
        {
            "problem": problem_data["HALTING"],
            "com_class": class_data["RECOGNIZABLE"],
        },
        # A_TM    in   RECOGNIZABLE
        {
            "problem": problem_data["A_TM"],
            "com_class": class_data["RECOGNIZABLE"],
        },
    ]

    return memberships
    
def get_manual_non_memberships(problem_data, class_data):
    non_memberships = [
        {
            "problem": problem_data["UNBOUNDED BINARY EQUALITY"],
            "com_class": class_data["D-REGULAR"],
        },
        {
            "problem": problem_data["EQ-REG-EXP"],
            "com_class": class_data["PSPACE"],
        },
        {
            "problem": problem_data["HALTING"],
            "com_class": class_data["DECIDABLE"],
        },
        # TQBF   not in    L
        {
            "problem": problem_data["TQBF"],
            "com_class": class_data["L"],
        }, 
        {
            "problem": problem_data["A_TM"],
            "com_class": class_data["DECIDABLE"],
        },
    ]

    return non_memberships
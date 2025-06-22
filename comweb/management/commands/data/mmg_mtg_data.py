from comweb.models import MachineType, MachineMode

def get_manual_mtg():
    machine_types = {mt.NA: mt for mt in MachineType.objects.all()}
    return [
            {
                "lower": machine_types["finite automaton"],
                "upper": machine_types["pushdown automaton"],
                "justification": "pushdown automaton generalize finite automaton by adding a stack (memory), but can simulate finite automaton by simply not using the stack.",
            },       
            {
                "lower": machine_types["pushdown automaton"],
                "upper": machine_types["Turing machine"],
                "justification": "Turing machines generalize pushdown automaton by providing an infinite tape instead of a stack, allowing them to simulate any pushdown automaton.",
            },
            {
                "lower": machine_types["finite automaton"],
                "upper": machine_types["linear bounded automaton"],
                "justification": "Linear bounded automaton generalize finite automaton by providing a tape of linear size, so any computation by a finite automaton can be simulated by a linear bounded automaton.",
            },
            {
                "lower": machine_types["linear bounded automaton"],
                "upper": machine_types["Turing machine"],
                "justification": "Turing machines generalize linear bounded automaton by allowing an unbounded tape, so any computation by a linear bounded automaton can be simulated by a Turing machine.",
            }

            ]

def get_manual_mmg(): 
    machine_modes = {mm.NA: mm for mm in MachineMode.objects.all()}
    return  [
            {
                "lower": machine_modes["deterministic"],
                "upper": machine_modes["non-deterministic"],
                "justification": "Deterministic machines can be seen as a special case of non-deterministic machines where the number of choices at each step is exactly one.",
            },
            {
                "lower": machine_modes["non-deterministic"],
                "upper": machine_modes["alternating"],
                "justification": "Non-deterministic machines can be seen as a special case of alternating machines where the number of alternations is zero.",
            }, 
        ]
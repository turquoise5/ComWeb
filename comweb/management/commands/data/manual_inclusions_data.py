from comweb.models import Reference

def get_manual_inclusions(classes):
    return ([
            {
                "lower": classes['co-D-REGULAR'], 
                "upper": classes['D-REGULAR'],
                "justification": "Closed under complementation",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                "lower": classes['co-N-REGULAR'],
                "upper": classes['N-REGULAR'],
                "justification": "Closed under complementation",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            },
            {
                "lower": classes['N-REGULAR'],
                "upper": classes['D-REGULAR'],
                "justification": "Every NFA can be converted to an equivalent DFA using the subset construction",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book", 
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Theorem 1.39"
                )
            },
            {
                "lower": classes["co-D-CONTEXT-FREE"],
                "upper": classes["D-CONTEXT-FREE"],
                "justification": "Closed under complementation",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book", 
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Theorem 2.42"
                )
            }, 
            {
                "lower": classes["D-CONTEXT-FREE"], 
                "upper": classes["DECIDABLE"],
                "justification": "Every context-free language is decidable",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book",
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Theorem 4.9"
                )
            }, 
            {
                "lower": classes["N-CONTEXT-FREE"],
                "upper": classes["DECIDABLE"],
                "justification": "Every context-free language is decidable",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book", 
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Theorem 4.9"
                )
            }, 
            {
                "lower": classes["N-CONTEXT-FREE"],
                "upper": classes["P"],
                "justification": "Every context-free language is a member of P",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book", 
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Theorem 7.16"
                )
            },
            {
                "lower": classes["D-CONTEXT-FREE"],
                "upper": classes["P"],
                "justification": "Every context-free language is a member of P",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book", 
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Theorem 7.16"
                )
            },
            {
                "lower": classes["N-REGULAR"],
                "upper": classes["N-CONTEXT-FREE"],
                "justification": "Every regular language is context-free",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book", 
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Theorem 2.1"
                )
            },
            {
                "lower": classes["NL"],
                "upper": classes["P"],
                "justification": "PATH is NL-complete, and PATH is in P",
                "references": Reference.objects.get_or_create(
                    DE="Sipser's Book", 
                    doi="https://dl.acm.org/doi/10.5555/524279",
                    locator="Corollary 8.26"
                )
            }, 
            {
                "lower": classes["P"],
                "upper": classes["PSPACE"],
                "justification": "time upper bounds space",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # NP in PSPACE
                "lower": classes["NP"],
                "upper": classes["PSPACE"],
                "justification": "Given an efficient verifier for an NP problem, we can build a DTM that simulates the verifier and uses polynomial space",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # coNP in PSPACE
                "lower": classes["co-NP"],
                "upper": classes["PSPACE"],
                "justification": "given an efficient co-verifier for a co-NP problem, we can build a DTM that simulates the co-verifier and uses polynomial space",
                "references": Reference.objects.get_or_create(
                    doi="", 
                    locator=""
                )
            }, 
            {
                # ap in PSPACE
                "lower": classes["AP"],
                "upper": classes["PSPACE"],
                "justification": "post-order traversal of the computation tree of a PSPACE problem can be done in polynomial space",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # PSAPCE in EXP
                "lower": classes["PSPACE"],
                "upper": classes["EXP"],
                "justification": "If a DTM uses polynomial space, it must be in exp time; because of the DTM is a decider that doesn't repeat configurations",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
               # AP in EXP
                "lower": classes["AP"],
                "upper": classes["EXP"],
                "justification": "Using TQBF in AP, given a efficient alternating decider, we can build a DTM by generating computation tree (top to bottom) and evaluating nodes bottom up",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                ) 
            }, 
            {
                # NPSPACE in EXP
                "lower": classes["NPSPACE"],
                "upper": classes["EXP"],
                "justification": "We can simulate a NTM by building a configuration graph and running decider for PATH to see if there is a path from the start configuration to an accepting configuration",
                "references": Reference.objects.get_or_create(  
                    doi="",
                    locator=""
                )
            }, 
            {
                #apspace in exp 
                "lower": classes["APSPACE"],
                "upper": classes["EXP"],
                "justification": "Simulate an ATM by generating configuration graph and running PATH",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # npspace in pspace
                "lower": classes["NPSPACE"],
                "upper": classes["PSPACE"],
                "justification": "Given a NTM, we can build a DTM thats simulates it by checking PATH in the configuration graph using Savitch's idea",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # npspace in ap 
                "lower": classes["NPSPACE"],
                "upper": classes["AP"],
                "justification": "We build an ATM that simulates the NTM and uses alternating quantifiers to find accepting path in configuration graph",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # exp in apspace 
                "lower": classes["EXP"],
                "upper": classes["APSPACE"],
                "justification": "We build an ATM that simulates the DTM by simulating the circuit of the machine",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # l in P 
                "lower": classes["L"],
                "upper": classes["P"],
                "justification": "If a DTM uses logarithmic space, it must also be in polynomial time",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # NL in NP
                "lower": classes["NL"],
                "upper": classes["NP"],
                "justification": "corollary of L in P",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # AL in AP
                "lower": classes["AL"],
                "upper": classes["AP"],
                "justification": "Corollary of L in P",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # NL in P 
                "lower": classes["NL"],
                "upper": classes["P"],
                "justification": "We can build a DTM that simulates the NTM and uses logarithmic space to store the configuration graph, and run decider for PATH",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # AL in P
                "lower": classes["AL"],
                "upper": classes["P"],
                "justification": "Simulate an ATM by generating configuration graph and running PATH",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            },
            {
                # P in AL
                "lower": classes["P"],
                "upper": classes["AL"],
                "justification": "Simulate the DTM by generating configuration graph and running PATH, using Svaitch's idea",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
            {
                # co-NL in P
                "lower": classes["co-NL"],
                "upper": classes["P"],
                "justification": "Using the fact that NL in P, and P is closed under complementation",
                "references": Reference.objects.get_or_create(  
                    doi="",
                    locator=""
                )
            }, 
            {
                # co-NL in NL
                "lower": classes["co-NL"],
                "upper": classes["NL"],
                "justification": "A corollary of complement of PATH is in NL",
                "references": Reference.objects.get_or_create(
                    doi="",
                    locator=""
                )
            }, 
        ])

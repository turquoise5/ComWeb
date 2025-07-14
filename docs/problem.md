# `Problem` Table

The `Problem` table represents computational problems that are either members or non-members of complexity classes. Each problem has a (co-) problem.

## Fields

| Field        | Type                        | Description                                                                |
| ------------ | --------------------------- | -------------------------------------------------------------------------- |
| `id`         | `int`                 | Auto-generated ID.                                                         |
| `NA`         | `string`  | Full name of the problem (e.g., SAT, PRIMES).                              |
| `AB`         | `string`  | Abbreviation or symbol used to identify the problem.                       |
| `TY`         | `ProblemType id`   | The type of the problem (e.g., decision, function, promise).               |
| `DE`         | `string` | A brief description of the problem.                                        |
| `co`         | `boolean`              | Indicates whether this is a co-problem.                                    |
| `co_problem` | `Problem id`        | Links to the (co-) problem. |

## Related Tables
* [`ProblemType`](problem_type.md)

`Problem` is used to define: 
* [`Membership`](membership.md), [`NonMembership`](nonmembership.md)
* [`ManualMembership`](manualmembership.md), [`ManualNonMembership`](manualnonmembership.md)

## Example

```json
{
  "NA": "Boolean satisfiability",
  "AB": "SAT",
  "TY": "decision",
  "DE": "Given a Boolean formula, determine if it is satisfiable.",
  "co": false,
  "co_problem": co-SAT
}
```

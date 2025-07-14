# Problem-Related Tables

This document describes the schema and purpose of the tables related to problem representation in the ComWeb database. The tables are `Problem` and `ProblemType`.

---

## `Problem` Table

The `Problem` table represents computational problems that are either members or non-members of complexity classes. Each problem has a (co-) problem.

### Fields

| Field        | Type                        | Description                                                                |
| ------------ | --------------------------- | -------------------------------------------------------------------------- |
| `id`         | `int`                 | Auto-generated ID.                                                         |
| `NA`         | `string`  | Full name of the problem (e.g., SAT, PRIMES).                              |
| `AB`         | `string`  | Abbreviation or symbol used to identify the problem.                       |
| `TY`         | `ProblemType id`   | The type of the problem (e.g., decision, function, promise).               |
| `DE`         | `string` | A brief description of the problem.                                        |
| `co`         | `boolean`              | Indicates whether this is a co-problem.                                    |
| `co_problem` | `Problem id`        | Links to the (co-) problem. |

### Related Tables
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

## `ProblemType` Table

Defines the nature of problems (e.g., decision, function, promise).

### Fields

| Field   | Type                        | Description                                        |
| ------- | --------------------------- | -------------------------------------------------- |
| `id`    | `int`                 | Auto-generated ID.                                 |
| `NA`    | `string` | Name of the problem type (e.g., Decision Problem). |
| `SO`    | `int`              | Sort order for displaying.                         |
| `order` | `int`              | Relative logical or structural ordering.           |

### Notes

* Referenced by the [`Problem`](#problem-table) table and [`Class`](class.md).

### Example

```json
{
  "NA": "Decision Problem",
  "SO": 1,
  "order": 1
}
```

# Tables for problems

This document describes the schema and purpose of the tables related to problems.

---

## `ProblemType`

Contains the various _types_ of problems (e.g., decision, search). 

### Fields

| Field   | Type     | Description                        |
| ------- | -------- | ---------------------------------- |
| `id`    | `int`    | Auto-generated unique identifier.  |
| `NA`    | `string` | Full name (e.g., `decision`).      |
| `SO`    | `int`    | Sort order (used for UI ordering). |
| `order` | `int`    | Conceptual ordering of the type.   |

### Example

```json
{
  "NA"    : "decision",
  "SO"    : 1,
  "order" : 1
}
```

### Usage

Used in `Problem` and [`Class`](class.md).

---

## `Problem`

Contains computational _problems_ (e.g., satisfiability, factoring). For every problem in the table, the complement is also in the table.

### Fields

| Field        | Type             | Description                                                        |
| ------------ | ---------------- | ------------------------------------------------------------------ |
| `id`         | `int`            | Auto-generated unique identifier.                                  |
| `AB`         | `string`         | Abbreviation (e.g., `SAT`).                                        |
| `NA`         | `string`         | Full name (e.g., `Satisfiability`).                                |
| `DE`         | `string`         | A brief description of the problem.                                |
| `TY`         | `ProblemType id` | The type of the problem (e.g., `decision`).                        |
| `co`         | `boolean`        | Indicates whether this is the complement of the described problem. |
| `co_problem` | `Problem id`     | Link to the complementary problem.                                 |

### Example

```json
{
  "AB"         : "SAT",
  "NA"         : "Satisfiability",
  "DE"         : "Given a Boolean formula, check that there exists an assignment of truth values that makes it true.",
  "TY"         : "⟶ decision",
  "co"         : false,
  "co_problem" : "⟶ complement of SAT"
}
```

### Usage

Used in `ManualMembership` & `Membership` ([see](membership.md)) and `ManualNonMembership` & `NonMembership` ([see](nonmembership.md))

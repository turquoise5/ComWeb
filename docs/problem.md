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
  "SO"    : 10,
  "order" : 10
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
| `co`         | `boolean`        | If `TY`=`decision`: Whether this is _the complement_ of `DE`.      |
| `co_problem` | `Problem id`     | If `TY`=`decision`: Link to the complementary problem.             |

### Example

```json
{
  "AB"         : "SAT",
  "NA"         : "satisfiability of Boolean formulas",
  "DE"         : "Given a boolean formula φ, check that there exists an truth assignment that makes φ true.",
  "TY"         : "⟶ decision",
  "co"         : false,
  "co_problem" : "⟶ complement of SAT"
}
```

### Usage

Used in `ManualMembership` & `Membership` ([see](membership.md)) and `ManualNonMembership` & `NonMembership` ([see](nonmembership.md))

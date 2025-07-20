# Tables for classes

This document describes the schema and purpose of the tables related to classes.

---

## `ResourceBound`

Contains the various _bounds_ for computational resources (e.g., polynomial, exponential).

### Fields

| Field   | Type     | Description                        |
| ------- | -------- | ---------------------------------- |
| `id`    | `int`    | Auto-generated unique identifier.  |
| `AB`    | `string` | Abbreviation (e.g., `poly`).       |
| `NA`    | `string` | Full name (e.g., `polynomial`).    |
| `SO`    | `int`    | Sort order (used for UI ordering). |
| `order` | `int`    | Conceptual order.                  |

### Example

```json
{
  "AB"    : "poly",
  "NA"    : "polynomial",
  "SO"    :  29,
  "order" :  29
}
```

### Usage

Used in `Class`. Its entries feed the fields `time_bound`, `space_bound`, `alternations_bound`, etc.

-------------

## `Class`

Contains the various computability and complexity _classes_ (e.g., P, NP). For every class _C_ in the table, the class _coC_ is also in the table.

### Fields

| Field                | Type               | Description                                                                          |
| -------------------- | ------------------ | ------------------------------------------------------------------------------------ |
| `id`                 | `int`              | Auto-generated unique identifier.                                                    |
| `AB`                 | `string`           | Abbreviation (e.g., `P`).                                                            |
| `NA`                 | `string`           | Full name (e.g., `deterministic polynomial time`).                                   |
| `problem_type`       | `ProblemType id`   | The type of the class problems (e.g., `decision`).                                   |
| `machine`            | `Machine id`       | The machine solving the class problems (e.g., `deterministic Turing machine`).       |
| `co`                 | `boolean`          | If `problem_type`=`decision`: Whether this is the class of _complementary_ problems. |
| `co_class`           | `Class id`         | If `problem_type`=`decision`: Link to the class of complementary problems.           |
| `time_bound`         | `ResourceBound id` | The bound for time, if any (e.g., `poly`). Defaults to `∞`.                          |
| `space_bound`        | `ResourceBound id` | The bound for space, if any (e.g., `poly`). Defaults to `∞`.                         |
| `alternations_bound` | `ResourceBound id` | The bound for the number of alternations. Defaults to `∞`.                           |

### Example

```json
{
  "AB"                 : "P",
  "NA"                 : "deterministic polynomial time",
  "problem_type"       : "⟶ decision",
  "machine"            : "⟶ deterministic Turing machine",
  "co"                 : false,
  "co_class"           : "⟶ co-P"
  "time_bound"         : "⟶ polynomial",
  "space_bound"        : "⟶ ∞",
  "alternations_bound" : "⟶ ∞"
}
```

### Usage

Used in `ManualMembership` & `Membership` ([see](membership.md)), `Manual NonMemebrship` & `NonMembership` ([see](non_membership.md)), `ManualInclusion` & `Inclusion` ([see](inclusion.md)), `ManualNonInclusion` & `NonInclusion` ([see](non_inclusion.md)).

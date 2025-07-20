# Tables for reasoning 
This document describes the schema and purpose of the tables related to reasoning.

---

## `Method`

Contains the various _methods_ (e.g., manual, transitivity) by which a fact (e.g., inclusion, membership) may be deduced into the database.

### Fields

| Field | Type     | Description                        |
| ----- | -------- | ---------------------------------- |
| `id`  | `id`     | Auto-generated unique identifier.  |
| `AB`  | `string` | Abbreviation (e.g., `manual`)      |
| `NA`  | `string` | Full name (e.g., `manual`).        |
| `DE`  | `string` | A brief description of the method. |
| `SO`  | `int`    |Sort order (used for UI ordering).  |

### Example

```json
{
  "NA" : "manual",
  "AB" : "manual",
  "DE" : "This fact has been added manually."
  "SO" : 0,
}
```
### Usage

Used in [`Inclusion`](inclusion.md), [`NonInclusion`](non_inclusion.md), [`Membership`](membership.md), [`NonMembership`](non_membership.md).

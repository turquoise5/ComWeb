# Tables for reasoning 
This document describes the schema and purpose of the tables related to reasoning.

---

## `Method`

Contains the various _methods_ (e.g., manual, transitivity) by which a given fact (e.g., inclusion, membership) is established.

### Fields

| Field | Type     | Description                        |
| ----- | -------- | ---------------------------------- |
| `id`  | `id`     | Auto-generated unique identifier.  |
| `AB`  | `string` | Abbreviation (e.g., `manual`)      |
| `NA`  | `string` | Full name (e.g., `manual`).        |
| `SO`  | `int`    |Sort order (used for UI ordering).  |
| `DE`  | `string` | A brief description of the method. |

### Example

```json
{
  "NA" : "manual",
  "AB" : "manual",
  "SO" : 0,
  "DE" : "This fact has been added manually."
}
```
### Usage

Used in [`Inclusion`](inclusion.md), [`NonInclusion`](non_inclusion.md), [`Membership`](membership.md), [`NonMembership`](non_membership.md).

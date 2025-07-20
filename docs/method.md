# Tables for reasoning 
This document describes the schema and purpose of the tables related to reasoning.

---

## `Method`

Contains the various _methods_ by which a given fact (e.g., inclusion, membership) is established.

### Fields

| Field | Type                        | Description                                                     |
| ----- | --------------------------- | --------------------------------------------------------------- |
| `id`  | `id`                 | Auto-generated unique identifier.                               |
| `NA`  | `string` | Full name of the method (e.g., "Manual", "Transitivity"). |
| `AB`  | `string` | Abbreviation             |
| `SO`  | `int`              | Sort order used for display and query organization.             |
| `DE`  | `string` | A brief textual description of the method.                      |

### Example

```json
{
  "NA": "Transitive Closure",
  "AB": "TRANS",
  "SO": 2,
  "DE": "This fact was inferred via the transitive property of inclusions or memberships."
}
```

## Related Tables

* [`Inclusion`](inclusion.md)
* [`NonInclusion`](non_inclusion.md)
* [`Membership`](membership.md)
* [`NonMembership`](non_membership.md)

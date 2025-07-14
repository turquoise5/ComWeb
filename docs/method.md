# `Method` Table

The `Method` table stores metadata about how a given fact (e.g., an inclusion, membership, or non-membership) is established. This includes whether it is asserted manually, inferred through transitivity, or derived using some other technique.

## Fields

| Field | Type                        | Description                                                     |
| ----- | --------------------------- | --------------------------------------------------------------- |
| `id`  | `id`                 | Auto-generated unique identifier.                               |
| `NA`  | `string` | Full name of the method (e.g., "Manual", "Transitivity"). |
| `AB`  | `string` | Abbreviation             |
| `SO`  | `int`              | Sort order used for display and query organization.             |
| `DE`  | `string` | A brief textual description of the method.                      |

## Example

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
* [`NonInclusion`](noninclusion.md)
* [`Membership`](membership.md)
* [`NonMembership`](non_membership.md)

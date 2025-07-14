# `Inclusion` Table

The `Inclusion` table represents a derived or proven subset relationship between two complexity classes. For example, `P ⊆ NP`.

## Fields

| Field    | Type                 | Description                                                                                      |
| -------- | -------------------- | ------------------------------------------------------------------------------------------------ |
| `id`     | `int`          | Auto-generated unique ID.                                                                        |
| `lower`  | `Class id`  | The smaller class in the inclusion (i.e., the subset).                                           |
| `upper`  | `Class id`  | The larger class in the inclusion (i.e., the superset).                                          |
| `method` | `Method id` | How this inclusion was derived (e.g., manually asserted, transitive closure)          |
| `interm` | `Class id`  | Optional intermediate class used in transitive closure, e.g., `A ⊆ C` via `A ⊆ B ⊆ C`. Nullable. |

## Related Tables

* [`Class`](class.md): Both `lower` and `upper` refer to class instances.
* [`Method`](method.md): Describes whether the inclusion is manual, derived, or inferred.
* See also: [`ManualInclusion`](manualinclusion.md) for manually asserted inclusions with citations.
  
## Notes

* All inclusions in this table are either manually inserted or inferred logically.
* If `interm` is provided, it shows that this inclusion is not direct but follows from chaining others.
* If `method` is `null`, this fact may be considered a base (or axiomatic) inclusion.

## Example

```json
{
  "lower": "P",
  "upper": "NP",
  "method": "manual",
  "interm": null
}
```



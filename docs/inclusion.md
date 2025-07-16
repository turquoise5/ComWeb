# `ManualInclusion` Table

The `ManualInclusion` table captures explicitly asserted inclusion facts between complexity classes, supported by one or more references.

## Fields

| Field           | Type                         | Description                                                   |
| --------------- | ---------------------------- | ------------------------------------------------------------- |
| `id`            | `int`                  | Auto-generated ID.                                            |
| `lower`         | `Class id`          | The class on the left of the inclusion (i.e., the subset).    |
| `upper`         | `Class id`          | The class on the right of the inclusion (i.e., the superset). |
| `justification` | `string`  | A brief textual justification of the inclusion.               |
| `references`    | `Reference id` | List of references supporting the inclusion.                  |


## Notes

* This is the manually curated input to the `Inclusion` table.
* References may point to books, papers, or other credible sources.
* These records may be used to derive new inclusions through transitivity.

## Related Tables

* [`Class`](class.md)
* [`Reference`](reference.md)
* [`Inclusion`](inclusion.md)

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
* See also: [`ManualInclusion`] for manually asserted inclusions with citations.
  
## Notes

* All inclusions in this table are either manually inserted or inferred logically.
* If `interm` is provided, it shows that this inclusion is not direct but follows from chaining others.



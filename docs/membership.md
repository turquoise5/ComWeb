# `Membership` Table

The `Membership` table records derived facts about whether a specific problem is a member of a given complexity class.

## Fields

| Field       | Type                    | Description                                                                                                 |
| ----------- | ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| `id`        | `int`             | Auto-generated unique ID.                                                                                   |
| `problem`   | `Problem id`   | The problem that is in the class.                                                                           |
| `com_class` | `Class id`     | The class to which the problem belongs.                                                                     |
| `method`    | `Method id`    | How the membership was derived — manual, transitive, etc.                                                   |
| `row1`      | `Membership id`    | Optional: a previously established membership that, together with an inclusion, implies this one. Nullable. |
| `row2`      | `Inclusion id` | Optional: inclusion used in combination with `row1` to derive this result. Nullable.                        |

## Related Tables

* [`Problem`](problem.md)
* [`Class`](class.md)
* [`Method`](method.md)
* [`Inclusion`](inclusion.md)  used in transitive memberships.

## Notes

* Used to represent results like `SAT ∈ NP`, `PRIMES ∈ P`, etc.
* If `row1` and `row2` are set, this entry is transitive (e.g., `SAT ∈ NP` and `NP ⊆ PSPACE` implies `SAT ∈ PSPACE`).

## Example

```json
{
  "problem": "SAT",
  "com_class": "NP",
  "method": "manual",
  "row1": null,
  "row2": null
}
```

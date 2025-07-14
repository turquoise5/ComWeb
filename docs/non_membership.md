
# `ManualNonMembership` Table

The `ManualNonMembership` table records authoritative claims that a specific problem does *not* belong to a particular class, backed by one or more references.

## Fields

| Field        | Type                         | Description                                           |
| ------------ | ---------------------------- | ----------------------------------------------------- |
| `id`         | `int`                  | Auto-generated ID.                                    |
| `problem`    | `Problem id`        | The problem for which non-membership is asserted.     |
| `com_class`  | `Class id`          | The complexity class the problem does not belong to.  |
| `references` | `Reference id` | Citations that support this non-membership assertion. |

## Notes

* Used to store well-documented non-memberships from research papers or books.
* Can be a source for derived entries in the `NonMembership` table.

## Example

```json
{
  "problem": "UNARY-EQ",
  "com_class": "D-REGULAR",
  "references": ["Sipser, Section 1.5"]
}
```

## Related Tables

* [`Problem`](problem.md)
* [`Class`](class.md)
* [`Reference`](reference.md)

-------

# `NonMembership` Table

The `NonMembership` table represents derived facts asserting that a particular problem is *not* a member of a specific complexity class.

## Fields

| Field       | Type                    | Description                                                                       |
| ----------- | ----------------------- | --------------------------------------------------------------------------------- |
| `id`        | `int`             | Auto-generated primary key.                                                       |
| `problem`   | `Problem id`   | The problem that is not in the class.                                             |
| `com_class` | `Class id`     | The class from which the problem is excluded.                                     |
| `method`    | `Method id`    | The method used to derive this non-membership (manual  derived).                |
| `row1`      | `NonMembership id`    | Optional pointer to prior non-membership used in a transitive argument. Nullable. |
| `row2`      | `Inclusion id` | Optional pointer to inclusion used in a transitive derivation. Nullable.          |



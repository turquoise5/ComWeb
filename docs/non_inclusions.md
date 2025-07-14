# Non-Inclusion Tables

These models represent non-inclusions between complexity classes—statements of the form "Class A is not included in Class B." These are stored either manually (`ManualNonInclusion`) or inferred (`NonInclusion`).

---

## `ManualNonInclusion`

Captures manually asserted non-inclusions between two complexity classes.

### Fields

| Field           | Type                         | Description                                                             |
| --------------- | ---------------------------- | ----------------------------------------------------------------------- |
| `not_superset`         | `Class id`          | The class that is **not** a subset (e.g., NP ⊄ P → NP is `upper`).      |
| `not_subset`         | `Class id`          | The class that is **not** a superset (e.g., NP ⊄ P → P is `lower`).     |
| `justification` | `string`  | A short reason for the non-inclusion (e.g., "space lower bounds time"). |
| `references`    | `ManyToManyField(Reference)` | List of references or citations that support the non-inclusion.         |

---

## `NonInclusion`

Represents either manually or computationally inferred non-inclusions.

### Fields

| Field          | Type                 | Description                                                                 |
| -------------- | -------------------- | --------------------------------------------------------------------------- |
| `not_superset` | `Class id`  | The class that is **not** a superset.                                       |
| `not_subset`   | `Class id`  | The class that is **not** a subset.                                         |
| `method`       | `Method id` | How the non-inclusion was derived (manual or transitive). Optional.         |
| `interm`       | `Class id`  | Intermediate class used to prove non-inclusion by contradiction (optional). |

### Notes

* This table may be derived from `ManualNonInclusion` or inferred via witnesses and transitivity.
---

## Related Tables

* [`Class`](class.md)
* [`Reference`](reference.md)
* [`Method`](method.md)

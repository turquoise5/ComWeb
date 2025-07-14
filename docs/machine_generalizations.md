# Machine Generalization Tables

This document describes the models that represent generalization relationships between machine types and machine modes.

---

## `MTG` (Machine Type Generalization)

The `MTG` table captures inferred generalizations between `MachineType` entries. These are either entered manually or computed through transitive closure from other MTG entries.

### Fields

| Field    | Type                        | Description                                                |
| -------- | --------------------------- | ---------------------------------------------------------- |
| `lower`  | `ForeignKey(MachineType)`   | The more specific machine type.                            |
| `upper`  | `ForeignKey(MachineType)`   | The more general machine type.                             |
| `method` | `CharField(max_length=500)` | Notes whether the entry is "manual" or inferred.           |
| `row1`   | `ForeignKey('self')`        | First MTG entry used in a transitive deduction. Nullable.  |
| `row2`   | `ForeignKey('self')`        | Second MTG entry used in a transitive deduction. Nullable. |

### Notes

* Used to derive more general machine type hierarchies.
* Automatically computed relationships reference their source entries.

---

## `ManualMTG`

The `ManualMTG` table stores manually asserted generalizations between `MachineType` entries.

### Fields

| Field           | Type                        | Description                         |
| --------------- | --------------------------- | ----------------------------------- |
| `lower`         | `ForeignKey(MachineType)`   | The specific machine type.          |
| `upper`         | `ForeignKey(MachineType)`   | The more general machine type.      |
| `justification` | `CharField(max_length=500)` | Explanation for the generalization. |

### Notes

* Serves as the authoritative source for initial MTG population.
* Justifications can be theoretical or citation-based.

---

## `MMG` (Machine Mode Generalization)

The `MMG` table represents inferred generalizations between `MachineMode` entries.

### Fields

| Field    | Type                        | Description                                    |
| -------- | --------------------------- | ---------------------------------------------- |
| `lower`  | `ForeignKey(MachineMode)`   | The more specific machine mode.                |
| `upper`  | `ForeignKey(MachineMode)`   | The more general machine mode.                 |
| `method` | `CharField(max_length=500)` | Method of derivation (manual/transitive).      |
| `row1`   | `ForeignKey('self')`        | First MMG entry used for inference. Nullable.  |
| `row2`   | `ForeignKey('self')`        | Second MMG entry used for inference. Nullable. |

### Notes

* Parallels the MTG structure, but for machine modes (e.g., deterministic, nondeterministic).

---

## `ManualMMG`

The `ManualMMG` table contains manually entered generalizations between machine modes.

### Fields

| Field           | Type                        | Description                              |
| --------------- | --------------------------- | ---------------------------------------- |
| `lower`         | `ForeignKey(MachineMode)`   | The more specific machine mode.          |
| `upper`         | `ForeignKey(MachineMode)`   | The more general machine mode.           |
| `justification` | `CharField(max_length=500)` | Explanation or source for the assertion. |

### Notes

* These entries guide the generation of the `MMG` table.

---

## Related Tables

* [`MachineType`](machine_tables.md)
* [`MachineMode`](machine_tables.md)
* [`Method`](method.md) (for tracking how generalizations were derived)

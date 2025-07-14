# Machine Generalization Tables

This document describes the models that represent generalization relationships between machine types and machine modes.

---

## `MTG` (Machine Type Generalization)

The `MTG` table captures inferred generalizations between `MachineType` entries. These are either entered manually or computed through transitive closure from other MTG entries.

### Fields

| Field    | Type                        | Description                                                |
| -------- | --------------------------- | ---------------------------------------------------------- |
| `lower`  | `MachineType id`   | The more specific machine type.                            |
| `upper`  | `MachineType id`   | The more general machine type.                             |
| `method` | `string` | Notes whether the entry is "manual" or inferred.           |
| `row1`   | `MTG id`        | First MTG entry used in a transitive deduction. Nullable.  |
| `row2`   | `MTG id`        | Second MTG entry used in a transitive deduction. Nullable. |

### Notes

* Used to derive more general machine type hierarchies.
* Automatically computed relationships reference their source entries.

---

## `ManualMTG`

The `ManualMTG` table stores manually asserted generalizations between `MachineType` entries.

### Fields

| Field           | Type                        | Description                         |
| --------------- | --------------------------- | ----------------------------------- |
| `lower`         | `MachineType id`   | The specific machine type.          |
| `upper`         | `MachineType id`   | The more general machine type.      |
| `justification` | `string` | Explanation for the generalization. |

### Notes

* Serves as the authoritative source for initial MTG population.
* Justifications can be theoretical or citation-based.

---

## `MMG` (Machine Mode Generalization)

The `MMG` table represents inferred generalizations between `MachineMode` entries.

### Fields

| Field    | Type                        | Description                                    |
| -------- | --------------------------- | ---------------------------------------------- |
| `lower`  | `MachineMode id`   | The more specific machine mode.                |
| `upper`  | `MachineMode id`   | The more general machine mode.                 |
| `method` | `string` | Method of derivation (manual/transitive).      |
| `row1`   | `MMG id`        | First MMG entry used for inference. Nullable.  |
| `row2`   | `MMG id`        | Second MMG entry used for inference. Nullable. |

### Notes

* Parallels the MTG structure, but for machine modes (e.g., deterministic, nondeterministic).

---

## `ManualMMG`

The `ManualMMG` table contains manually entered generalizations between machine modes.

### Fields

| Field           | Type                        | Description                              |
| --------------- | --------------------------- | ---------------------------------------- |
| `lower`         | `MachineMode id`   | The more specific machine mode.          |
| `upper`         | `MachineMode id`   | The more general machine mode.           |
| `justification` | `string` | Explanation or source for the assertion. |

---

## Related Tables

* [`MachineType`](machine_tables.md)
* [`MachineMode`](machine_tables.md)
* [`Method`](method.md) (for tracking how generalizations were derived)

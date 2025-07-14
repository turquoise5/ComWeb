# Machine-Related Tables

This document describes the schema and purpose of the tables related to machines, machine types, and modes in the ComWeb database.

---

## `MachineMode` Table

Represents different modes of machine operation (e.g., deterministic, nondeterministic).

### Fields

| Field | Type                        | Description                                                    |
| ----- | --------------------------- | -------------------------------------------------------------- |
| `id`  | `int`                 | Auto-generated unique identifier.                              |
| `AB`  | `string` | Abbreviation (e.g., `D`, `ND`, `A`).                           |
| `NA`  | `string` | Full name of the mode (e.g., Deterministic, Nondeterministic). |
| `SO`  | `int`              | Sort order (used for UI ordering).                             |

---

## `MachineType` Table

Represents the type of the machine (e.g., Turing machine, DFA, PDA).

### Fields

| Field | Type                        | Description                                   |
| ----- | --------------------------- | --------------------------------------------- |
| `id`  | `int`                 | Auto-generated unique identifier.             |
| `AB`  | `string` | Abbreviation (e.g., `TM`, `DFA`).             |
| `NA`  | `string` | Full name of the type (e.g., Turing Machine). |
| `SO`  | `int`              | Sort order (used for UI ordering).            |

---

## `Machine` Table

Combines a machine mode and type into a specific machine entity used to define complexity classes.

### Fields

| Field  | Type                        | Description                                                      |
| ------ | --------------------------- | ---------------------------------------------------------------- |
| `id`   | `id`                 | Auto-generated unique identifier.                                |
| `AB`   | `string` | Abbreviation of the machine (e.g., `DTM`, `NFA`).                |
| `NA`   | `string` | Full name of the machine (e.g., Deterministic Turing Machine).   |
| `SO`   | `int`              | Sort order (for display purposes).                               |
| `mode` | `MachineMode id`   | The mode of the machine (deterministic, nondeterministic, etc.). |
| `type` | `MachineType id`   | The structural type of the machine (e.g., TM, DFA).              |

---

## Related Tables

* [`Class`](class.md): references `Machine` to define complexity classes.
* [`MTG` & `ManualMTG`](machine_generalizations.md): define generalization relationships between `MachineType` entries.
* [`MMG` & `ManualMMG`](machine_generalizations.md): define generalization relationships between `MachineMode` entries.

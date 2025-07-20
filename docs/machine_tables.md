# Tables for machines

This document describes the schema and purpose of the tables related to machines.

---

## `MachineType` 

Contains the various _types_ of machines (e.g., Turing machine, finite automaton).

### Fields

| Field | Type     | Description                         |
| ----- | -------- | ----------------------------------- |
| `id`  | `int`    | Auto-generated unique identifier.   |
| `AB`  | `string` | Abbreviation (e.g., `TM`).          |
| `NA`  | `string` | Full name (e.g., `Turing machine`). |
| `SO`  | `int`    | Sort order (used for UI ordering).  |

### Example

```json
{
  "AB"    : "TM",
  "NA"    : "Turing machine",
  "SO"    : 3,
}
```

### Usage

Used in `Machine`.

---

## `MachineMode` 

Contains the various _modes_ of machines (e.g., deterministic, nondeterministic).

### Fields

| Field | Type     | Description                        |
| ----- | -------- | ---------------------------------- |
| `id`  | `int`    | Auto-generated unique identifier.  |
| `AB`  | `string` | Abbreviation (e.g., `D`).          |
| `NA`  | `string` | Full name (e.g., `deterministic`). |
| `SO`  | `int`    | Sort order (used for UI ordering). |

### Example

```json
{
  "AB"    : "D",
  "NA"    : "deterministic",
  "SO"    : 10,
}
```

### Usage

Used in `Machine`.

---

## `Machine` 

Contains the various _machines_ (e.g., deterministic Turing machine, nondeterministic finite automaton), each combining a _mode_ (e.g., deterministic, nondeterministic) and a _type_ (e.g., Turing machine, finite automaton).

### Fields

| Field  | Type             | Description                                       |
| ------ | ---------------- | ------------------------------------------------- |
| `id`   | `id`             | Auto-generated unique identifier.                 |
| `AB`   | `string`         | Abbreviation (e.g., `DTM`).                       |
| `NA`   | `string`         | Full name (e.g., `deterministic Turing machine`). |
| `SO`   | `int`            | Sort order (used for UI ordering).                |
| `mode` | `MachineMode id` | The mode of the machine.                          |
| `type` | `MachineType id` | The type of the machine.                          |

### Example

```json
{
  "AB"    : "DTM",
  "NA"    : "deterministic Turing machine",
  "SO"    : 310,
  "mode"  : "⟶ deterministic",
  "type"  : "⟶ Turing machine"
}
```

### Usage

Used in [`Class`](class.md).

---

## Related tables

* [`Class`](class.md): Uses `Machine` to define complexity classes.
* [`ManualMTG` & `MTG`](machine_generalizations.md): Defines generalization relationships between `MachineType`s.
* [`ManualMMG` & `MMG`](machine_generalizations.md): Defines generalization relationships between `MachineMode`s.

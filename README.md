# ComWeb

## Overview

**ComWeb** is a web platform for querying and visualizing relationships between complexity classes, problems, machine models, and resource bounds. It provides:

- A structured **database** of complexity-theoretic facts.
- A web interface for answering questions like:
  - “Is class A included in class B?”
  - “Is problem X a member of class Y?”
- Support for **manual and derived** inclusions, non-inclusions, and memberships.

> If you're working in computational complexity, ComWeb helps you reason formally about known results, open problems, and supporting justifications.

---

## Structure of this README

- [Database](#database)
- [Populating the Database](#populating-the-database)
- [Frontend](#️frontend)
- [Deployment](#deployment)
- [Future Directions](#future-directions)

---

## Database
> Below is an explaination of tables and how they're populated. If you're contributing to ComWeb or reviewing how facts are inferred, this documentation is the best place to start.

### Table Descriptions

Below is a list of core database tables used in ComWeb. Each links to a detailed explanation of its schema and population logic, found in the `docs/` directory.

| Table | Description | Docs |
| ---| --- | --- |
| `MachineType` | Contains the various _types_ of formal machines (e.g. Turing machine, finite automaton). Used to define _machines_. | [docs/machine\_tables.md](docs/machine_tables.md) |
| `MachineMode` | Contains the various _modes_ of computation (e.g. deterministic, nondeterministic). Used to define _machines_. | [docs/machine\_tables.md](docs/machine_tables.md) |
| `Machine` | Contains the various formal _machines_ (e.g., deterministic Turing machine, nondeterministic finite automaton), as combinations of _type_ (from `MachineType`) and _mode_ (from `MachineMode`). Used to define _classes_. | [docs/machine\_tables.md](docs/machine_tables.md) |
| `ProblemType` | Contains the various _types_ of computational problems (e.g., decision, search). Used to define _problems_ and _classes_. | [docs/problem.md](docs/problem.md) |
| `Problem` | Contains the various computational _problems_. | [docs/problem.md](docs/problem.md) |
| `ResourceBound` | Contains the various _bounds_ (e.g., polynomial, exponential) for computational resources (e.g., time, space). Used to define _classes_. | [docs/class.md](docs/class.md) |
| `Class` | Contains the various complexity _classes_. | [docs/class.md](docs/class.md) |
| `Method`                               | Describes how a fact (e.g., inclusion) was derived i.e. manually, by transitivity, etc.             | [docs/method.md](docs/method.md)                  |
| `MTG`, `ManualMTG`                     | Generalization relations between machine types. Used to derive machine inclusions.               | [docs/machine\_generalizations.md](docs/machine_generalizations.md)                        |
| `MMG`, `ManualMMG`                     | Generalization relations between machine modes. Used to derive machine inclusions.               | [docs/machine\_generalizations.md](docs/machine\_generalizations.md)                        |
| `Reference`                            | Bibliographic sources (e.g., papers, books) with locator fields. Used in manual entries.    | [docs/reference.md](docs/reference.md)            |
| `Inclusion`, `ManualInclusion`         | Asserts that one complexity class is included in another, manually or via closure.               | [docs/inclusion.md](docs/inclusion.md)            |
| `NonInclusion`, `ManualNonInclusion`   | Asserts a separation between two classes, through witness problems, chaining, or mnaual entry.                      | [docs/non\_inclusion.md](docs/non_inclusion.md)      |
| `Membership`, `ManualMembership`       | Asserts that a problem is in a class (derived or cited).                                         | [docs/membership.md](docs/membership.md)          |
| `NonMembership`, `ManualNonMembership` | Asserts that a problem is *not* in a class.                                                      | [docs/non\_membership.md](docs/non_membership.md)    |

---

### Table Generation Logic

Each database table in ComWeb is populated according to specific logic—sometimes manually, sometimes computed via transitive closure, reference chains, or intermediate derivations.

To better understand how each table is populated, refer to the relevant manual data files and populator scripts:

| Table                                     | Logic Description                                                      | Relevant Docs                                                      |
| ----------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| `MachineMode` / `MachineType` / `ProblemType`/ `ResourceBound` / `Method` / `Reference` | Populated from manual arrays.             | [data here](comweb/management/commands/data/static_data.py)               |
| `Machine`        | Created from cross-product of `MachineType` + `MachineMode `                | [populator](comweb/management/commands/utils/machine_populator.py)                   | 
| `Class`                                   | Populated from manual arrays, then adds a co-class for each class         | [manual data], (comweb/management/commands/data/class_data.py) [populator](comweb/management/commands/utils/class_populator.py)                     |
| `MTG` / `MMG`                             | Constructed from Manual entries + inferred via closure.                | [manual data](comweb/management/commands/data/mmg_mtg_data.py), [MMG populator](comweb/management/commands/utils/mmg_populator.py), [MTG populator](comweb/management/commands/utils/mtg_populator.py) |
| `Inclusion` / `ManualInclusion` | `ManualInclusion` entries are added directly with justifications and references. `Inclusion` entries are generated automatically using based on generalizations of machine type, machine mode, and resource bound generalizations (i.e. P ⊆ NP as a result of machine mode generlization) + extended using transitive closure. | [manual data](comweb/management/commands/data/manual_inclusions_data.py), [populator](comweb/management/commands/utils/inclusion_populator.py) |
| `NonInclusion` / `ManualNonInclusion` | `ManualNonInclusion` is entered with justifications and references. `NonInclusion` is expanded by: (1) importing manual assertions, (2) using witness problems—if problem X ∈ A and X ∉ B, infer A ⊄ B, (3) applying transitive rules such as: if A ⊄ B and C ⊆ B, then A ⊄ C; or if A ⊄ B and A ⊆ D, then D ⊄ B. | [data](), [populator](comweb/management/commands/utils/non_inclusions_populator.py) |
| `Problem`                                   | Populated from manual arrays, then adds a co-problem for each problem         | [manual data](comweb/management/commands/data/problem_data.py), [populator](comweb/management/commands/utils/problem_populator.py)                     |
| `Membership` / `ManualMembership` | `ManualMembership` is manually added with citations. `Membership` is expanded automatically: if a problem X is in class C′ and C′ ⊆ C (via `Inclusion`), then X ∈ C by transitivity. | [manual data](comweb/management/commands/data/memberships_data.py), [populator](comweb/management/commands/utils/memberships_populator.py) |
| `NonMembership` / `ManualNonMembership` | `ManualNonMembership` is entered directly. `NonMembership` is inferred: if a problem X ∉ C′ and C ⊆ C′, then X ∉ C by transitivity. | [manual data](comweb/management/commands/data/memberships_data.py), [populator](comweb/management/commands/utils/memberships_populator.py) |


## Populating the Database

You can populate the database manually or via GitHub Actions.

### Local Setup

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db
```
### Remote (via GitHub Actions)

1. Go to the **Actions** tab in this GitHub repo.
2. Run the `populate_db` workflow.

> Running the GitHub Action will populate the **remote PostgreSQL database**. To work with a **local SQLite3 instance**, modify the `DATABASES` setting in `settings.py`.

### Data Sources and Flow

- Manual data: Stored in `comweb/management/commands/data`
- Population logic: `comweb/management/commands/utils/`
- Population script: `comweb/management/commands/populate_db.py`

Some tables must be populated in a specific order (e.g., MachineModes before Machines).

---

## Frontend

The frontend is built using Django templates and views:

- **Templates**: `comweb/templates/`
- **Views**: `views.py`
- **Routes**: `urls.py`

It allows users to:
- Query for class inclusions or non-inclusions
- Query for problem memberships
- View different tables 

---

## Deployment

- **Backend**: Django app
- **Database**: PostgreSQL hosted on [Railway](https://railway.app)
- **Frontend**: Automatically deployed via [Vercel](https://com-web-teal.vercel.app/)

### Remote Deployment

- Every `git push` to `main` triggers an automatic deploy.

### Local Development

1. Set up a virtual environment
2. Install dependencies
3. Configure `settings.py` for a local SQLite database
4. Run the server:

```bash
python manage.py runserver
```

---

## Future Directions

ComWeb is under active development. Some potential improvements:

- **Add structure** to existing facts:
  - Track open problems, reductions, hardness, and completeness.
- **Expand** the database:
  - Import facts from standard texts (e.g., Papadimitriou's *Computational Complexity*).
- **Improve the frontend**:
  - Enhanced filtering, visualizations, and citations.
----
## Contributions

We welcome contributions to **ComWeb**! You;re welcome to contribute through flagging issues and mistakes, fixing bugs, improving documentation, or helping with inference logic, here's how to get started:

### Ways to Contribute

- **Fix or improve existing features** — Check [issues](https://github.com/turquoise5/issues)
- **Add data** — Use the manual tables (e.g., `ManualInclusion`, `ManualMembership`) to input more manual facts, with citations.
- **Write inference rules** — Help improve how we automatically deduce new facts (e.g., transitivity, witness logic).
  
### Getting Started

1. Fork the repository
2. Create a new branch (`git checkout -b your-feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin your-feature-name`)
5. Open a Pull Request

### Guidelines

- Follow existing code style and naming conventions.
- Make sure any new inference logic has tests or examples.
- Add documentation if your contribution affects core logic or tables.

For questions or discussion, feel free to open an issue or start a discussion thread, or reach out to `jabdelma@andrew.cmu.edu` 


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

- [Database](##-Database)
- [Populating the Database](#-populating-the-database)
- [Frontend](#️-frontend)
- [Deployment](#-deployment)
- [Future Directions](#-future-directions)

---

## Database
> Below is an explaination of tables and how they're populated. If you're contributing to ComWeb or reviewing how facts are inferred, this documentation is the best place to start.

### Table Descriptions

Below is a list of core database tables used in ComWeb. Each links to a detailed explanation of its schema and population logic, found in the `docs/` directory.

| Table                                  | Description                                                                                      | Docs                                              |
| -------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| `MachineMode`                          | Represents modes of computation (e.g. deterministic, nondeterministic). Used to define machines. | [docs/machine\_tables.md](docs/machine_tables.md)     |
| `MachineType`                          | Represents types of abstract machines (e.g. Turing Machine, DFA). Used to define machines.       | [docs/machine\_tables.md](docs/machine_tables.md)     |
| `Machine`                              | A combination of `MachineType` and `MachineMode`. Used to define complexity classes.             | [docs/machine\_tables.md](docs/machine_tables.md)                |
| `ProblemType`                          | High-level category for problems (e.g., language, promise problem). Used to define classes.      | [docs/problem.md](docs/problem.md)     |
| `ResourceBound`                        | Describes computational resource limits (e.g. polynomial time). Used to parameterize classes.    | [docs/class.md](docs/class.md) |
| `Class`                                | Represents a complexity class defined by machine, problem type, and resource bounds.             | [docs/class.md](docs/class.md)                    |
| `Method`                               | Describes how a fact (e.g., inclusion) was derived — manually, by transitivity, etc.             | [docs/method.md](docs/method.md)                  |
| `MTG`, `ManualMTG`                     | Generalization relations between machine types. Used to derive machine inclusions.               | [docs/machine\_generalizations.md](docs/machine_generalizations.md)                        |
| `MMG`, `ManualMMG`                     | Generalization relations between machine modes. Used to derive machine inclusions.               | [docs/machine\_generalizations.md](docs/machine\_generalizations.md)                        |
| `Reference`                            | Bibliographic sources (e.g., papers, books) with locator fields. Cited in factual assertions.    | [docs/reference.md](docs/reference.md)            |
| `Inclusion`, `ManualInclusion`         | Asserts that one complexity class is included in another, manually or via closure.               | [docs/inclusion.md](docs/inclusion.md)            |
| `NonInclusion`, `ManualNonInclusion`   | Asserts a separation between two classes, with or without witness problems.                      | [docs/non\_inclusion.md](docs/non_inclusion.md)      |
| `Problem`                              | Represents decision/computational problems. May have co-problems (e.g., SAT and UNSAT).          | [docs/problem.md](docs/problem.md)                |
| `Membership`, `ManualMembership`       | Asserts that a problem is in a class (derived or cited).                                         | [docs/membership.md](docs/membership.md)          |
| `NonMembership`, `ManualNonMembership` | Asserts that a problem is *not* in a class.                                                      | [docs/non\_membership.md](docs/non_membership.md)    |

---

### Table Generation Logic

Each database table in ComWeb is populated according to specific logic—sometimes manually, sometimes computed via transitive closure, reference chains, or intermediate derivations.

To better understand how each table is populated and interconnected, refer to the logic files in the [`docs/`](docs/) directory:

| Table                                     | Logic Description                                                      | Logic Docs                                                      |
| ----------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| `MachineMode` / `MachineType` / `Machine` | Populated from manual CSVs, required for class generation.             | [docs/logic\_machines.md](docs/logic_machines.md)               |
| `ProblemType` / `ResourceBound`           | Loaded from static lists to define foundational schema.                | [docs/logic\_static.md](docs/logic_static.md)                   |
| `Class`                                   | Created from cross-product of machine + problem type + bounds.         | [docs/logic\_class.md](docs/logic_class.md)                     |
| `Reference` / `Method`                    | Parsed manually from citation CSVs.                                    | [docs/logic\_references.md](docs/logic_references.md)           |
| `Inclusion` / `ManualInclusion`           | Populated manually and extended using transitive closure.              | [docs/logic\_inclusions.md](docs/logic_inclusions.md)           |
| `NonInclusion` / `ManualNonInclusion`     | Loaded from manual assertions with logic for witness and transitivity. | [docs/logic\_noninclusions.md](docs/logic_noninclusions.md)     |
| `Membership` / `ManualMembership`         | Derived via direct citation or transitive inclusion of problems.       | [docs/logic\_memberships.md](docs/logic_memberships.md)         |
| `NonMembership` / `ManualNonMembership`   | Similar to Membership logic, but for exclusion.                        | [docs/logic\_nonmemberships.md](docs/logic_nonmemberships.md)   |
| `MTG` / `MMG`                             | Constructed from Manual entries + inferred via closure.                | [docs/logic\_generalizations.md](docs/logic_generalizations.md) |


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

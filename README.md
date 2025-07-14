# ComWeb

## Overview

**ComWeb** is a web platform for querying and visualizing relationships between complexity classes, problems, machine models, and resource bounds. It provides:

- A structured **database** of complexity-theoretic facts.
- A web interface for answering questions like:
  - “Is class A included in class B?”
  - “Is problem X a member of class Y?”
- Support for **manual and derived** inclusions, non-inclusions, and memberships.

> If you're working in computational complexity, ComWeb helps you reason formally and collaboratively about known results, open problems, and supporting justifications.

---

## Structure of this README

- [Database](#-database)
- [Populating the Database](#-populating-the-database)
- [Frontend](#️-frontend)
- [Deployment](#-deployment)
- [Future Directions](#-future-directions)

---

## Database

The core of ComWeb is its **relational schema**, implemented in `comweb/models.py`. Key entities include:

- `Class`: Represents a complexity class (e.g., NP, PSPACE).
- `Problem`: Represents a decision or computational problem (e.g., SAT).
- `Inclusion`, `NonInclusion`: Track inclusion and separation between classes.
- `Membership`, `NonMembership`: Represent whether a problem belongs to a class.
- `Machine`, `MachineType`, `MachineMode`: Represent computational models of a machine (Machine is defined by its type (e.g Turing Mschine) and mode (e.g. Determinstic).
- `ResourceBound`: Time/space/alternations bounds (e.g., linear, polynomial).
- `Reference`: Stores citations supporting any of the above relationships.

### Relationships Example

A `Class` is defined by:
- A `ProblemType` (e.g. language, function, search),
- A `Machine` (itself defined by its `Mode` and `Type`),
- Resource bounds (time, space, alternations),
- Co flag which describes if it's a co class (eg. co-NP).

---

### Table Descriptions

> Each model includes fields like name (`NA`), abbreviation (`AB`), sort order (`SO`), and various foreign keys.

| Table | Description |
|-------|-------------|
| `MachineType`, `MachineMode` | Categories like TM/DFA or deterministic/non-deterministic |
| `Machine` | Specific combinations of type and mode |
| `Class` | A complexity class, built from a machine and resource bounds |
| `Problem` | A computational problem |
| `Inclusion`, `NonInclusion` | Facts about class relationships |
| `Membership`, `NonMembership` | Facts about whether a problem is in a class |
| `Reference` | Source material that supports any of the above |
| `Method` | Describes how a fact was derived (eg. manual, transitive) |

---

## Populating the Database

You can populate the database manually or via GitHub Actions.

### Local Setup

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db

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
- Search for class inclusions or non-inclusions
- Explore problem memberships
- Navigate generalizations between machine types/modes

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

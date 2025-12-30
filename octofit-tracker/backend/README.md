# OctoFit Backend

This folder holds the Django backend for OctoFit.

Quick start:

1. Create the Python virtual environment:

```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

2. Run migrations and start the server (after adding DB settings):

```bash
python manage.py migrate
python manage.py runserver
```

Note: Follow `.github/instructions` files for project-specific guidelines.

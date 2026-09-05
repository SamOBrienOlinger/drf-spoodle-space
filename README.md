# SpoodleSpace · Backend API

The Django REST Framework backend for SpoodleSpace, a social platform for dog owners.

**Python · Django · Django REST Framework**

[Getting started](#getting-started) · [Repository guide](#repository-guide) · [Checks](#checks-and-review) · [Credits](#credits-and-reuse)

## What you can explore

- Member profiles, posts, comments, likes and following.
- Serializers, permissions and API views built with Django REST Framework.
- Authentication and Cloudinary media configuration.
- Dog profiles, health posts and danger reports.

## Getting started

Requires Python, pip and a virtual environment. The repository records `3.10` in [.python-version](.python-version). Dependency pins in older projects may need a compatible Python environment; this README does not upgrade them.

```bash
git clone https://github.com/SamOBrienOlinger/drf-spoodle-space.git
cd drf-spoodle-space
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` instead.

After resolving the project notes and configuring the local environment, use:

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000). Stop the server with **Ctrl+C**. Use `python manage.py createsuperuser` in the same project directory if you need access to Django admin.

## Configuration

Settings are defined in [spoodle_space/settings.py](spoodle_space/settings.py). Set the values used by your chosen local configuration before running Django. A `.env` file is only read when the project explicitly loads it; most of these projects read the process environment or an optional `env.py`.

| Variable | Purpose |
| --- | --- |
| `ALLOWED_HOST` | An additional hostname accepted by Django, without a scheme. |
| `CLIENT_ORIGIN` | Frontend origin allowed by the backend, including scheme and port. |
| `CLIENT_ORIGIN_DEV` | Development frontend origin; check the settings logic before using a cloud-workspace URL. |
| `CLOUDINARY_URL` | Cloudinary connection URL used for media storage. Keep the value private. |
| `DATABASE_URL` | Connection URL for your own development database. Required where settings parse it without a fallback. |
| `DEV` | Development-mode switch. Inspect whether the settings test its presence or its value. |
| `REACT_FRONTEND_PROD_URL` | Frontend production origin used for cross-origin and CSRF configuration. |
| `SECRET_KEY` | Django signing key. Use a locally generated value and keep it out of Git. |

Use a disposable development database for migrations and tests. Keep service credentials and local configuration out of commits.

## Repository guide

| Path | Purpose |
| --- | --- |
| [spoodle_space/settings.py](spoodle_space/settings.py) | Django configuration |
| [requirements.txt](requirements.txt) | Python dependency versions |
| [manage.py](manage.py) | Django management commands |

## Checks and review

From the directory containing `manage.py`, run `python manage.py check` and `python manage.py test` after configuring an isolated development database. Inspect the test modules: scaffold `tests.py` files may contain no actual tests.

Generate fresh results from the revision you are working on; historical test reports describe earlier runs.

## Deployment

Hosting entry points are recorded in [Procfile](Procfile). Configure the runtime, database, allowed origins and static/media handling for the chosen host. Historical deployment records may describe services that are no longer available.

## Credits and reuse

Design decisions, original feature notes, historical testing evidence and detailed acknowledgements remain available in the preserved project record:

- [README.md · original project record](https://github.com/SamOBrienOlinger/drf-spoodle-space/blob/47cd7ab367a54787b9116e04e4bd6a4afd90fe9f/README.md)

Learning resources and starter material: [Code Institute](https://codeinstitute.net/).

No repository-level licence file is present in this snapshot. This README does not grant additional reuse permissions. Check with the relevant rights holders before reusing code, written content or assets.

## Support

Repository maintained in [Sam O’Brien-Olinger’s GitHub account](https://github.com/SamOBrienOlinger). For a problem or suggested improvement, [open an issue](https://github.com/SamOBrienOlinger/drf-spoodle-space/issues) with the affected page or command, steps to reproduce, and expected behaviour.

[Back to top](#spoodlespace--backend-api)

# SpoodleSpace · Backend API

The Django REST Framework backend for SpoodleSpace, a social platform for dog owners.

**Python · Django · Django REST Framework**

[Getting started](#getting-started) · [Repository guide](#repository-guide) · [Checks](#checks-and-review) · [Credits](#credits-and-reuse)

**Paired frontend:** [spoodle-space-pp5](https://github.com/SamOBrienOlinger/spoodle-space-pp5).

## What you can explore

- Member profiles, posts, comments, likes and following.
- Serializers, permissions and API views built with Django REST Framework.
- Authentication and Cloudinary media configuration.
- Dog profiles, health posts and danger reports.

## Getting started

Requires Git, Python `3.10`, pip and a virtual environment. The Python version is recorded in [.python-version](.python-version).

```bash
git clone https://github.com/SamOBrienOlinger/drf-spoodle-space.git
cd drf-spoodle-space
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `py -3.10 -m venv .venv` and activate with `.venv\Scripts\Activate.ps1`. Keep the pinned dependency versions when reproducing this revision. If pip needs to build `psycopg2` or Pillow from source, install the compiler, Python development headers and the corresponding PostgreSQL/image-library development packages for your operating system first.

If startup fails with `ModuleNotFoundError: No module named 'pkg_resources'`, install `setuptools==80.9.0` in this virtual environment with `python -m pip install setuptools==80.9.0`. The pinned SimpleJWT version imports `pkg_resources`, which was absent with setuptools `84.0.0` during the September 6, 2026 local check.

### Isolated local setup

Use a separate local SQLite database for development instead of the committed `db.sqlite3` or a hosted database. The following override applies only when explicitly selected with `--settings=local_settings`.

Add these paths to this checkout's `.git/info/exclude` so the local files cannot be included accidentally by an ordinary `git add`:

```text
/local_settings.py
/local-development.sqlite3
```

In the repository root, create `local_settings.py` with:

```python
import os

from spoodle_space.settings import *

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "local-development.sqlite3",
    }
}
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]
CORS_ALLOW_CREDENTIALS = True

# Local HTTP development only; production keeps its secure-cookie settings.
JWT_AUTH_SECURE = False
JWT_AUTH_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"
```

Set a local signing key and the exact development flag in the same terminal. Keep that terminal open so the key remains stable during the session.

```bash
export SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
export DEV=True
```

PowerShell equivalent:

```powershell
$env:SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
$env:DEV = "True"
```

Before running the API, set `CLOUDINARY_URL` to the connection URL from a development Cloudinary account you control. This is required for account responses as well as uploads: the user serializer includes a profile-image URL. In this revision, registration without configured media storage returned HTTP 500 even though the system check and migrations passed. Supply the value privately through your local environment; do not commit it.

Then run:

```bash
python manage.py check --settings=local_settings
python manage.py migrate --settings=local_settings
python manage.py runserver localhost:8000 --settings=local_settings
```

Open [localhost:8000](http://localhost:8000), and follow the frontend's [local API instructions](https://github.com/SamOBrienOlinger/spoodle-space-pp5#run-with-a-local-api). Use the same `localhost` hostname on both ports. Stop the server with **Ctrl+C**. To create an admin user, run `python manage.py createsuperuser --settings=local_settings` in the configured terminal.

The local override and frontend development URL are not deployment settings. The production entry point continues to use `spoodle_space.settings`. A fresh end-to-end authentication run is still required before treating a local or hosted setup as verified.

## Configuration

Production settings are in [spoodle_space/settings.py](spoodle_space/settings.py). They read process environment variables and optionally import an `env.py` file from the project root. They do not automatically load a `.env` file.

| Variable | Actual use in this revision |
| --- | --- |
| `SECRET_KEY` | Required Django signing key; supply your own value. |
| `DEV` | Must equal the literal string `True` to enable debug mode and the browsable API. Other values, including `true` and `False`, do not enable them. |
| `DATABASE_URL` | Optional. If absent, base settings use the repository's `db.sqlite3`; the local override above instead selects `local-development.sqlite3`. |
| `CLOUDINARY_URL` | Development Cloudinary connection URL required by the default media storage, including profile-image URLs in authentication responses and uploaded media. Do not use production credentials for local tests. |
| `ALLOWED_HOST` | Additional accepted backend hostname, without scheme or path. |
| `CLIENT_ORIGIN` | Additional frontend origin, including scheme and port. |
| `CLIENT_ORIGIN_DEV` | Additional CORS origin; its parsed hostname also contributes to allowed hosts and an HTTPS CSRF origin. It is not a general local-development switch. |
| `REACT_FRONTEND_PROD_URL` | Additional CORS origin. The current code does not automatically add this value to `CSRF_TRUSTED_ORIGINS`. |

The base settings keep secure JWT, session and CSRF cookies with `SameSite=None` even when `DEV=True`. The explicit local override above configures HTTP-compatible settings for localhost. However, the custom [logout route](spoodle_space/views.py) imports cookie constants directly from the base settings, so its deletion cookies still use `Secure; SameSite=None` when the override is selected. Local HTTP-client logout passed, but browser cookie deletion needs separate verification. Hosted deployments must retain appropriate HTTPS cookie settings and configure their exact frontend origin.

Keep secrets, local settings and databases out of commits. Omitting an upload does not remove the default Cloudinary dependency: serializing profile or post image URLs also accesses the media backend. A separate test-only filesystem-storage override can isolate API behavior, but it does not verify Cloudinary upload or browser image delivery.

## Repository guide

| Path | Purpose |
| --- | --- |
| [spoodle_space/settings.py](spoodle_space/settings.py) | Django configuration |
| [requirements.txt](requirements.txt) | Python dependency versions |
| [manage.py](manage.py) | Django management commands |

## Checks and review

From the configured local terminal, run `python manage.py check --settings=local_settings` and `python manage.py test --settings=local_settings`. Both explicitly select the isolated local configuration above. Inspect the test modules: scaffold `tests.py` files may contain no actual tests.

Manual checks: create a local test account, sign in through the paired frontend, create a post with a small valid image using your development Cloudinary account, read and edit it, sign out, and confirm a protected action requires sign-in. Delete the test post after checking. The API accepts text-only posts when the image field is omitted, but the current frontend unconditionally appends an image field; submitting its form without a file returned HTTP 400 in an equivalent local multipart request.

On September 6, 2026, isolated HTTP API checks passed registration, login, PNG post creation and persistence, editing, authenticated non-owner restrictions, refresh, logout and deletion using SQLite and test-only filesystem storage. These checks used Python 3.10.20, setuptools 80.9.0, Pillow 8.2.0 built without JPEG support, and the pinned `psycopg2-binary` package while omitting the redundant source `psycopg2` package. They do not establish an unchanged clean installation, a complete browser journey, JPEG support or Cloudinary delivery.

Generate fresh results from the revision you are working on; historical test reports describe earlier runs.

## Deployment

Hosting entry points are recorded in [Procfile](Procfile). Configure the runtime, database, allowed origins and static/media handling for the chosen host. Historical deployment records may describe services that are no longer available.

## Credits and reuse

Created by Sam O'Brien-Olinger, with learning and starter material from Code Institute's [Moments project](https://github.com/Code-Institute-Solutions/moments). Thanks to Tom Ainsworth for debugging support, mentors Naoise Gaffney and Antonio Rodriguez, and the Code Institute tutors and Student Care Team.

The original acknowledgements also recognise W3Schools, Stack Overflow and Code Institute's [README template](https://github.com/Code-Institute-Solutions/readme-template).

Design decisions, original feature notes, historical testing evidence and detailed acknowledgements remain available in the preserved project record:

- [README.md · original project record](https://github.com/SamOBrienOlinger/drf-spoodle-space/blob/47cd7ab367a54787b9116e04e4bd6a4afd90fe9f/README.md)

Learning resources and starter material: [Code Institute](https://codeinstitute.net/).

No repository-level licence file is present in this snapshot. This README does not grant additional reuse permissions. Check with the relevant rights holders before reusing code, written content or assets.

## Support

Repository maintained in [Sam O’Brien-Olinger’s GitHub account](https://github.com/SamOBrienOlinger). For a problem or suggested improvement, [open an issue](https://github.com/SamOBrienOlinger/drf-spoodle-space/issues) with the affected page or command, steps to reproduce, and expected behaviour.

[Back to top](#spoodlespace--backend-api)

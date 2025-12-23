# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Run development server
python manage.py runserver

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test

# Run tests for a specific app
python manage.py test accounts
python manage.py test home

# Create superuser
python manage.py createsuperuser

# Format code with black
black .
```

## Architecture

This is a Django 6.0 e-commerce project using Python 3.13.

### Project Structure
- `django_project/` - Main project configuration (settings, root URLs, WSGI/ASGI)
- `accounts/` - Custom user authentication with extended user model
- `home/` - Landing page app
- `templates/` - Project-wide templates with `base.html` as the parent template
- `static/` - Static files (CSS, JS, images)

### Key Architectural Decisions

**Custom User Model**: The project uses `accounts.CustomUser` extending `AbstractUser` with additional fields (`age`, `phone`). Configured via `AUTH_USER_MODEL` in settings.

**URL Routing**:
- Root URLs in `django_project/urls.py` delegate to app-specific URLs
- Auth URLs use Django's built-in `django.contrib.auth.urls` at `/accounts/`
- Custom signup at `/accounts/signup/` via `accounts.urls`

**Templates**: Uses a project-level `templates/` directory with `registration/` subdirectory for auth templates.

**Environment Configuration**: Uses `python-decouple` for environment variables. Create a `.env` file for `DEBUG` and `ALLOWED_HOSTS`.

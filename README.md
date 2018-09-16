# django-clean-media

[![Build Status](https://img.shields.io/travis-ci/florimondmanca/django-clean-media.svg?style=flat-square)](https://travis-ci.org/florimondmanca/django-clean-media)
[![Python](https://img.shields.io/badge/python-3.4+-blue.svg?style=flat-square)](https://docs.python.org/3/)
[![Django](https://img.shields.io/badge/django-1.8+-blue.svg?style=flat-square)](https://www.djangoproject.com)

> 🚧 Work In Progress 🚧

Media files tend to go stale as a result of not being deleted along with their references in database.

This Django app provides simple utilities to **remove unused media files**.

## Features

- Configurable management command
- Looks for unused files in `FileField` and `ImageField`
- Easily extensible to support other fields that can hold references to files (such as Markdown fields)
- Integrates with any storage backend (e.g. disk storage, cloud storage…)

## Compatibility

- Tested under Django 1.8, 1.11, 2.0 and 2.1
- Tested under Python 3.4, 3.5, 3.6 and 3.7

## Install

Install from PyPI:

```
pip install django-clean-media
```

You can then add the `clean_media` app to your project:

```python
# settings.py

INSTALLED_APPS = [
  # ...
  'clean_media',
]
```

## Usage

### Management command

The main usage of `django-clean-media` is as a management command.

```bash
$ python manage.py clean_media
```

### Programmatic usage

As all management commands, `clean_media` can also be used in a programmatically using Django's `call_command` utility:

```python
# myapp/somefile.py
from django.core.management import call_command

call_command('clean_media')
```

### Periodic calls

Integrating the two previous usages with task scheduling tools (such as Celery or Cron jobs), you can setup `django-clean-media` to clean your media files periodically. 🤖

## Development

### Install

To try out the project locally, you can install development requirements in a virtualenv:

```bash
$ python3 -m venv env
$ . env/bin/activate
$ pip install -r requirements-dev.txt
```

### Tests

Run tests using:

```bash
$ python runtests.py
```

### CI/CD

CI/CD is configured on [Travis CI](https://travis-ci.org/florimondmanca/django-clean-media).

### Releasing to PyPI

TODO

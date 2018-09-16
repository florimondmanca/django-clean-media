# django-clean-media

> 🚧 Work In Progress 🚧

This Django app provides simple utilities to **remove unused media files**.

## Features

- Configurable management command
- Looks for unused files in `FileField` and `ImageField`
- Easily extensible to support other fields that can hold references to files (such as Markdown fields)
- Integrates with any storage backend (e.g. disk, cloud…)

## Compatibility

- Django 1.8+ and 2.0+
- Python 3.4+

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

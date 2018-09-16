"""Clean unusued media files."""
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Management command to delete unused media files."""

    def handle(self, *args, **options):
        pass

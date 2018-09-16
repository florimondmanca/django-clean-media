"""Tests for the management command."""
from django.test import TestCase
from django.core.management import call_command


class TestManagementCommand(TestCase):
    """Test the clean_media management command."""

    def test_command_can_be_called(self):
        call_command('clean_media')

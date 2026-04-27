from django.core.management.base import BaseCommand
from main.models import Language

class Command(BaseCommand):
    help = 'Populate the database with initial languages'

    def handle(self, *args, **kwargs):
        languages = [
            {'name': "O'zbekcha", 'code': 'uz'},
            {'name': 'English', 'code': 'en'},
            {'name': 'Русский', 'code': 'ru'},
            {'name': 'Deutsch', 'code': 'de'},
            {'name': 'Français', 'code': 'fr'},
            {'name': 'Türkçe', 'code': 'tr'},
            {'name': 'Español', 'code': 'es'},
        ]

        for lang_data in languages:
            lang, created = Language.objects.get_or_create(
                code=lang_data['code'],
                defaults={'name': lang_data['name']}
            )
            if created:
                self.stdout.write(f"Added language: {lang_data['code']}")
            else:
                self.stdout.write(f"Language already exists: {lang_data['code']}")

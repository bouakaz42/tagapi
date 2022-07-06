from django.apps import AppConfig


class ShorturlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shorturl'

    def ready(self):
        from . import signals

from django.apps import AppConfig


class QrappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qrapp'

    def ready(self):
        from . import signals

from django.apps import AppConfig


class InouttimeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inouttime'

    def ready(self):
        import inouttime.signals

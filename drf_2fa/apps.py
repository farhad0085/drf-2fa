from django.apps import AppConfig


class Drf2FaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drf_2fa'

    def ready(self) -> None:
        from drf_2fa import signals

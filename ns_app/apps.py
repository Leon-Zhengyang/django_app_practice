from django.apps import AppConfig


class NsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ns_app'
    
    # def ready(self):
    #     from .ap_scheduler import start
    #     start()
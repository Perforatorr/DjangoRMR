from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


class BlockPanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Block_panel'
    def ready(self):
        from .tasks import my_function
        scheduler = BackgroundScheduler()
        scheduler.add_job(my_function, 'interval', seconds=6000)  # Каждые 60 секунд
        scheduler.start()

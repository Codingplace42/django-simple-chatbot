from django.apps import AppConfig


class SimpleChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simple_chatbot'

    def ready(self):
        from simple_chatbot import signals

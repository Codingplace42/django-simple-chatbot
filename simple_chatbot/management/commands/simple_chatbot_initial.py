import logging
from django.core.management.base import BaseCommand
from simple_chatbot.models import Pattern

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("Initializing of default patterns started.")
        patterns = [
            "Hi, how are you?",
            "Is anyone there?",
            "Hello",
            "What's up?!",
            "hey there!",
            "Bye",
            "See you later",
            "Goodbye",
            "I need to go now.",
        ]
        for pattern in patterns:
            Pattern.objects.get_or_create(string=pattern)
            logger.info(f">> {pattern}")

import os
import logging
from django.core.management.base import BaseCommand
from simple_chatbot.models import Pattern

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("Initializing of default patterns started.")
        PYTHON_FILEPATH = os.path.dirname(__file__)
        PATTERN_FILEPATH = os.path.join(PYTHON_FILEPATH, "patterns.txt")
        with open(PATTERN_FILEPATH, "r") as file:
            patterns = file.readlines()
        for pattern in patterns:
            string = pattern.replace("\n", "")
            Pattern.objects.get_or_create(string=string)
            logger.info(f">> {string}")

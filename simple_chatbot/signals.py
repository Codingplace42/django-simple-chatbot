from django.dispatch import receiver
from django.db.models.signals import post_save
from simple_chatbot.models import Pattern, Token
from simple_chatbot.tokenizer import get_tokens_from_pattern


@receiver(post_save, sender=Pattern)
def create_tokens(instance, *args, **kwargs):
    tokens = get_tokens_from_pattern(instance.string)
    for token in tokens:
        token_instance, _ = Token.objects.get_or_create(token=token)
        token_instance.patterns.add(instance)
        token_instance.save()

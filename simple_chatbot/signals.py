from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from simple_chatbot.models import Pattern, Token, UserMessageInput


@receiver(post_save, sender=Pattern)
def create_tokens(instance, *args, **kwargs):
    tokens = list(set(instance.tokenized_string.split()))
    for token in tokens:
        token_instance, _ = Token.objects.get_or_create(token=token)
        token_instance.patterns.add(instance)
        token_instance.save()


@receiver(pre_save, sender=Pattern)
def clear_tokens_on_change(instance, *args, **kwargs):
    if not instance.pk:
        return
    pattern = Pattern.objects.get(id=instance.id)
    pattern.tokens.clear()


@receiver(post_save, sender=UserMessageInput)
def cp_user_message_input_to_pattern(instance, created, *args, **kwargs):
    if created:
        return
    if instance.status and instance.correct_tag != instance.identified_tag:
        instance.correct_tag = instance.identified_tag
        instance.save()
        return
    elif instance.correct_tag == instance.identified_tag and not instance.status:
        instance.status = True
        instance.save()
        return
    elif not instance.correct_tag:
        return
    else:
        Pattern.objects.get_or_create(string=instance.message, tag=instance.correct_tag)

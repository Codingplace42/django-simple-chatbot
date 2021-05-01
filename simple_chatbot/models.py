from django.db import models
from django.utils.translation import gettext_lazy as _
from .tokenizer import get_tokens_from_pattern
from .utils import PatternMatcher


class Token(models.Model):
    token = models.CharField(
        verbose_name=_("token"),
        max_length=40,
        db_index=True,
        unique=True,
        editable=False
    )
    patterns = models.ManyToManyField(
        to="Pattern",
        related_name="%(class)ss",
        blank=True,
        null=True,
        editable=False
    )

    class Meta:
        verbose_name = _("token")
        verbose_name_plural = _("tokens")
        app_label = "simple_chatbot"

    def save(self, *args, **kwargs):
        self.token = self.token.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.token


class TagManager(models.Manager):
    def get_tag_by_string(self, string):
        tokens = get_tokens_from_pattern(string)
        token_instances = Token.objects.filter(token__in=tokens)
        pattern_pks = token_instances.values_list("patterns")
        patterns = Pattern.objects.filter(id__in=pattern_pks)
        pattern_matcher = PatternMatcher(tokens=tokens, patterns=patterns)
        return pattern_matcher.get_best_matched_tag()


class Tag(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=120
    )
    description = models.TextField(
        verbose_name=_("description"),
        blank=True
    )

    objects = TagManager()

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        app_label = "simple_chatbot"

    def __str__(self):
        return self.name


class Pattern(models.Model):
    string = models.CharField(
        verbose_name=_("string"),
        max_length=1024
    )
    tokenized_string = models.CharField(
        verbose_name=_("tokenized string"),
        max_length=1024,
        editable=False
    )
    tag = models.ForeignKey(
        to=Tag,
        verbose_name=_("tag"),
        related_name="%(class)ss",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.string

    def save(self, *args, **kwargs):
        self.tokenized_string = " ".join(get_tokens_from_pattern(self.string))
        super().save(*args, **kwargs)


# class History(models.Model):
#     pass

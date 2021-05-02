from django.contrib import admin
from .models import Token, Tag, Pattern, UserMessageInput


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    readonly_fields = ("token", "patterns", )

    def has_add_permission(self, request):
        return False


class PatternInline(admin.StackedInline):
    model = Pattern


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("method", )
    inlines = (PatternInline, )


@admin.register(UserMessageInput)
class UserMessageInputAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'identified_tag', 'timestamp', 'correct_tag', )
    list_editable = ('status', 'correct_tag', )
    list_filter = ('status', )

    def has_add_permission(self, request):
        return False


@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ("__str__", "tag", )
    list_filter = ("tag", )
    readonly_fields = ("tokenized_string", )

from django.contrib import admin
from .models import Token, Tag, Pattern, UserMessageInput


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    readonly_fields = ("token", "patterns", )


admin.site.register(Tag)
admin.site.register(Pattern)
admin.site.register(UserMessageInput)

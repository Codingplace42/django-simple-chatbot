from django.contrib import admin
from .models import Token, Tag, Pattern


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    readonly_fields = ("token", "patterns", )


admin.site.register(Tag)
admin.site.register(Pattern)

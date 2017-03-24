import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer

from crash.models import Crash


@admin.register(Crash)
class CrashAdmin(admin.ModelAdmin):
    search_fields = ['device_id', 'error']
    readonly_fields = ['device_id', 'error_prettified', 'created']
    list_display = ['device_id', 'created']
    exclude = ('error',)

    def has_add_permission(self, request):
        return False

    def error_prettified(self, instance):
        response = json.dumps(instance.error, sort_keys=True, indent=2)
        response = response[:5000]
        formatter = HtmlFormatter(style='colorful')
        response = highlight(response, JsonLexer(), formatter)
        style = "<style>" + formatter.get_style_defs() + "</style><br>"
        return mark_safe(style + response)

    error_prettified.short_description = 'Error'

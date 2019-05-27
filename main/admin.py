from django.contrib import admin
from .models import Hand, HandSituation
from tinymce.widgets import TinyMCE
from django.db import models


class HandAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title", {'fields': ["hand_title"]}),
        ("Content", {"fields": ["hand_content"]}),
        ("URL", {'fields': ["hand_slug"]}),
        ("Situations", {'fields': ["hand_situation"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }


admin.site.register(HandSituation)
admin.site.register(Hand,HandAdmin)
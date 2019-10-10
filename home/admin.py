from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import About, Profile


class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(About, AboutAdmin)
admin.site.register(Profile)

from django.contrib import admin

# Register your models here.
from .models import Note, CheckListItem

admin.site.register(Note)
admin.site.register(CheckListItem)
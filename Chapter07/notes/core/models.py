from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    attach = models.FileField(blank=True, null=True)
    thumbnail_url = models.CharField(max_length=255, blank=True, null=True)


class CheckListItem(models.Model):
    title = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    note = models.ForeignKey('Note', related_name='checklist_items')

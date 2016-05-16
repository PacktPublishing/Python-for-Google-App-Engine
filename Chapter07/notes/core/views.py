from django.shortcuts import render
from django import get_version
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Note
from .models import CheckListItem
from .forms import NoteForm
from .storage import GoogleCloudStorage

from google.appengine.api import images
from google.appengine.ext import blobstore


@login_required()
def home(request):
    user = request.user
    if request.method == "POST":
        f = NoteForm(request.POST, request.FILES)
        if f.is_valid():
            note = f.save(commit=False)
            note.owner = user
            if f.cleaned_data['attach']:
                try:
                    s = GoogleCloudStorage()
                    path = '/gs' + s.path(f.cleaned_data['attach'].name)
                    key = blobstore.create_gs_key(path)
                    note.thumbnail_url = images.get_serving_url(key, size=150, crop=True)
                except images.TransformationError, images.NotImageError:
                    pass
            note.save()
            for item in f.cleaned_data['cl_items'].split(','):
                CheckListItem.objects.create(title=item, note=note)
            return HttpResponseRedirect(reverse('home'))

    else:
        f = NoteForm()

    context = {
        'django_version': get_version(),
        'form': f,
        'notes': Note.objects.filter(owner=user).order_by('-id'),
    }
    return render(request, 'core/main.html', context)

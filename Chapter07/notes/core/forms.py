from django import forms

from .models import Note, CheckListItem


class NoteForm(forms.ModelForm):
    cl_items = forms.CharField(required=False,
                               label="Checklist Items",
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'comma,separated,values'
                               }))

    class Meta:
        model = Note
        exclude = ['id', 'date_created', 'owner', 'thumbnail_url']

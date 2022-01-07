from django import forms
from django.utils.translation import gettext_lazy as _
from app_works.models import Work


class WorkForm(forms.ModelForm):
    images = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True}))
    files = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True}))
    file_title = forms.CharField(max_length=255)

    class Meta:
        model = Work
        fields = ('title', 'description', 'images', 'files', 'file_title')

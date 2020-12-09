from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from mainapp.models import Main

class PostForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  excerpt = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  author = forms.ModelChoiceField(
    widget=forms.Select(attrs={'class': 'form-control'}),
    queryset=get_user_model().objects.all(),
  )
  slug = forms.CharField(
    initial=slugify(title),
    widget=forms.HiddenInput,
    disabled=True
  )
  published = forms.DateTimeField(
    initial=timezone.now,
    widget=forms.DateTimeInput(attrs={'class': 'form-control'}),
    disabled=True
  )
  class Meta:
    model = Main
    fields = '__all__'
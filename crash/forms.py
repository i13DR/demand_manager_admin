from django import forms

from crash.models import Crash


class CrashForm(forms.ModelForm):
    class Meta:
        model = Crash
        exclude = ['created', ]

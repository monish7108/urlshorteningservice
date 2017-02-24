from django import forms
from .models import urltable
class urlform(forms.ModelForm):
    class Meta:
        model = urltable
        exclude = ('myurl',)
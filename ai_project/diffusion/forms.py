
from django import forms

class TextToImageForm(forms.Form):
    prompt = forms.CharField(label='Enter Prompt', widget=forms.TextInput(attrs={'class': 'form-control'}))

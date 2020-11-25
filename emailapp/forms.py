from django import forms

class Subscribe(forms.Form):
    Email = forms.EmailField()

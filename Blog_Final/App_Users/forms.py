from django import forms

class AvatarForm(forms.Form):
    image = forms.ImageField(required=True)
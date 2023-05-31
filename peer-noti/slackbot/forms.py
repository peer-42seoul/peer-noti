from django import forms


class UserForm(forms.Form):
    intra_id = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

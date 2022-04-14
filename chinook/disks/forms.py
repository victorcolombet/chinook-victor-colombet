from django import forms

class Search(forms.Form):
    search = forms.CharField(label='search', max_length=100)
from django import forms

class SearchForm(forms.Form):
    keyword_type = forms.CharField()
    keyword = forms.CharField()
from django import forms
from datetime import datetime


class Form_new_post (forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    author = forms.CharField()
    category = forms.CharField()
    tags = forms.CharField()




class Form_new_author (forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    pseudonym = forms.CharField()

from django import forms

class VoteForm(forms.Form):
    choice = forms.ChoiceField()

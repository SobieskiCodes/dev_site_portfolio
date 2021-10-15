from django import forms


class AugChanceForm(forms.Form):
    Enchanting = forms.IntegerField(label='Enchanting', max_value=200, initial=99)
    Augment = forms.IntegerField(label='Augment', max_value=100, initial=5)
    Chance = forms.IntegerField(label='Chance', max_value=6, initial=6)
    Result = forms.CharField(label='Result', disabled=True, initial='87.53')

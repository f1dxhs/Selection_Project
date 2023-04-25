from django import forms

class ItemSearchForm(forms.Form):
    length = forms.FloatField()
    Dia_dr = forms.FloatField()
    T_Force = forms.FloatField()
    T_Weight = forms.CharField(max_length=20)
    T_Weight_J = forms.CharField(max_length=20)
    map_code = forms.CharField(max_length=20)

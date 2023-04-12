from django import forms

class ItemSearchForm(forms.Form):
    length = forms.FloatField()
    Dia_dr = forms.FloatField()
    T_Force = forms.FloatField()
    T_Torque = forms.FloatField()
    T_weight = forms.CharField(max_length=20)
    map_code = forms.CharField(max_length=20)

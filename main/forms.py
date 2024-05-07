from django import forms
from main.models import Dogovor

class DogovorForm(forms.ModelForm):
    class Meta:
        model = Dogovor
        fields = "__all__"
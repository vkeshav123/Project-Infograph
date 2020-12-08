from django import forms
from infographApp.models import Facts, QNA


class FactsForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = ('title','facts')

class QNAForm(forms.ModelForm):
    class Meta:
        model = QNA
        fields = ('q','a')
        
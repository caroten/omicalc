from django import forms
from core.forms import FormBS


class CalculationForm(FormBS):
    pages = forms.IntegerField(label='Количество полос')
    fmt = forms.CharField(label='Формат печати')
    inkset = forms.CharField(label='Цветность')

from django.shortcuts import render, redirect, get_object_or_404
from . import forms

def index(request):
    form = forms.CalculationForm()
    return render(request, 'calculation/index.html', {'form': form })


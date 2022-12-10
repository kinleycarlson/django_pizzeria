from django import forms

from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':''} 

        widgets = {'text':forms.Textarea(attrs= {'cols':80})}

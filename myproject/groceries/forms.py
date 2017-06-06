from django import forms
from groceries.models import Item, CHOICES


class ItemForm(forms.ModelForm):
    name = forms.CharField()
    category = forms.ChoiceField(choices=CHOICES)
    quantity = forms.NumberInput()
    weight = forms.NumberInput()

    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'weight']

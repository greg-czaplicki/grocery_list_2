from django import forms
from groceries.models import Item, CHOICES, Recipe


class ItemForm(forms.ModelForm):
    name = forms.CharField()
    category = forms.ChoiceField(choices=CHOICES)
    quantity = forms.IntegerField(min_value=1.0, initial=1)
    weight = forms.NumberInput(label_suffix='lbs')

    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'weight']


class AddRecipe(forms.ModelForm):
    name = forms.CharField()
    address = forms.URLField()

    class Meta:
        model = Recipe
        fields = ['name', 'address']

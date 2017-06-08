from django import forms
from django.forms.widgets import TextInput

from groceries.models import Item, CHOICES, Recipe

nums = [(i, i) for i in range(1, 13)]


class ItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),
                           error_messages={'required': "Name field is required."})
    category = forms.ChoiceField(choices=CHOICES)
    quantity = forms.ChoiceField(choices=nums)
    weight = forms.DecimalField(min_value=0.0, initial=0.00, required=False)

    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity']


class AddRecipe(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),
                           error_messages={
                               'required': "Recipe Name field is required."})
    address = forms.URLField(max_length=200,
                             help_text="Please enter the URL of the page.",
                             initial="http://",
                             widget=TextInput)

    class Meta:
        model = Recipe
        fields = ['name', 'address']

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from groceries.models import Item, Recipe
from groceries.forms import ItemForm, AddRecipe


class HomeTemplateView(CreateView):
    model = Item
    template_name = 'home.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse('Home')

    def get_context_data(self, **kwargs):
        kwargs['grocery_list'] = Item.objects.order_by('category')
        kwargs['recipe_list'] = Recipe.objects.order_by('name')
        return super(HomeTemplateView, self).get_context_data(**kwargs)


class UpdateTemplateView(UpdateView):
    template_name = 'item_update.html'
    model = Item
    fields = ['name', 'category', 'quantity', 'weight']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('Home')


class RecipeTemplateView(CreateView):
    model = Recipe
    template_name = 'recipe.html'
    form_class = AddRecipe

    def get_success_url(self):
        return reverse('Home')

    def get_context_data(self, **kwargs):
        kwargs['recipe_list'] = Recipe.objects.order_by('name')
        return super(RecipeTemplateView, self).get_context_data(**kwargs)


def DeleteList(request):
    database = Item.objects.all()
    recipes = Recipe.objects.all()
    database.delete()
    recipes.delete()
    return redirect('Home')

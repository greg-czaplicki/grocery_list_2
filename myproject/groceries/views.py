from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from groceries.forms import ItemForm, AddRecipe
from groceries.models import Item, Recipe


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
    model = Item
    template_name = 'item_update.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse('Home')


class UpdateRecipeTemplateView(UpdateView):
    model = Recipe
    template_name = 'recipe_update.html'
    form_class = AddRecipe

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


def DeleteItem(request, pk):
    object = Item.objects.get(id=pk)
    object.delete()
    return redirect('Home')


def DeleteRecipe(request, pk):
    object = Recipe.objects.get(id=pk)
    object.delete()
    return redirect('Home')


def CompleteItem(request, pk):
    object = Item.objects.get(id=pk)

    if object.complete == False:
        object.complete = True
    else:
        object.complete = False

    object.save()
    return redirect('Home')


def DeleteList(request):
    database = Item.objects.all()
    recipes = Recipe.objects.all()
    database.delete()
    recipes.delete()
    return redirect('Home')

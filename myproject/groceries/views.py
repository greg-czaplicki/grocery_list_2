from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from groceries.models import Item


class HomeTemplateView(CreateView):
    model = Item
    fields = ['name', 'category', 'quantity', 'weight']
    template_name = 'home.html'
    success_url = 'home.html'

    def get_context_data(self, **kwargs):
        kwargs['grocery_list'] = Item.objects.order_by('category')
        return super(HomeTemplateView, self).get_context_data(**kwargs)

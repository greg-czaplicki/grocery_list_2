from django.conf.urls import url
from django.contrib import admin

from groceries import views
from groceries.views import HomeTemplateView, UpdateTemplateView, \
    RecipeTemplateView, UpdateRecipeTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeTemplateView.as_view(), name='Home'),
    url(r'^recipe/', RecipeTemplateView.as_view(), name='Recipe'),
    url(r'^edit/recipe/(?P<pk>[\w\ ]+)', UpdateRecipeTemplateView.as_view(),
        name='EditRecipe'),
    url(r'^edit/(?P<pk>[\w\ ]+)', UpdateTemplateView.as_view(),
        name='Edit'),
    url(r'^delete/item/(?P<pk>[\w\ ]+)', views.DeleteItem, name='Delete'),
    url(r'^delete/recipe/(?P<pk>[\w\ ]+)', views.DeleteRecipe, name='DeleteRecipe'),
    url(r'^complete/(?P<pk>[\w\ ]+)', views.CompleteItem, name='Complete'),
    url(r'^delete/', views.DeleteList, name='Delete'),
]

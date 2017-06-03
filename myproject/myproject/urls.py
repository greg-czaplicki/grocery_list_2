from django.conf.urls import url
from django.contrib import admin
from groceries.views import HomeTemplateView, UpdateTemplateView, RecipeTemplateView
from groceries import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeTemplateView.as_view(), name='Home'),
    url(r'^recipe/', RecipeTemplateView.as_view(), name='Recipe'),
    url(r'^edit/(?P<pk>[\w\ ]+)', UpdateTemplateView.as_view(),
        name='Edit'),
    url(r'^delete/', views.DeleteList, name='Delete'),
]

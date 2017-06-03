from django.conf.urls import url
from django.contrib import admin
from groceries.views import HomeTemplateView, UpdateTemplateView, RecipeTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeTemplateView.as_view(), name='Home'),
    url(r'^recipe/', RecipeTemplateView.as_view(), name='Recipe'),
    url(r'^edit/(?P<pk>[\w\ ]+)', UpdateTemplateView.as_view(),
        name='Edit')
]

from django.conf.urls import url
from django.contrib import admin
from groceries.views import HomeTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', HomeTemplateView.as_view(), name='Home'),
]

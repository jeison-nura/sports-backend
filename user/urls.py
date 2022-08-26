from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # ex: /polls/
    path('hola', views.holaGuebon.as_view(), name='index'),
]
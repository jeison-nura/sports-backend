from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # ex: /polls/
    path('api/hola', views.holaGuebon.as_view(), name='index'),
]
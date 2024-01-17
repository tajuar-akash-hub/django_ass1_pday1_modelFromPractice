
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ),
    path('djangomodel/',views.django_model,name='django_model'),
]

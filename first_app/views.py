from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def home(requeest):
    return HttpResponse("working well so far")


def django_model(request):
    form= forms.StudentForm()
    return render(request,"./django_model.html",{'data':form})


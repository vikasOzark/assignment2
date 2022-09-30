from django.shortcuts import render
from . import models
from django.views import generic

# Create your views here.

# class based views
class IndexView(generic.ListView):
    context_object_name = 'products'
    queryset = models.ProductModel.objects.all()
    template_name = 'main_site/index.html'

def documentation(request):
    template_name = 'main_site/document.html'
    return render(request, template_name)
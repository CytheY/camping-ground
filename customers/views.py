from django.shortcuts import render
from django.views import generic
from .models import Customer
from django.http import HttpResponse
from django.template import loader

class AllCustomersView(generic.ListView):
    template_name = "customers/all.html"
    context_object_name = "customers_list"

    def get_queryset(self):
        """
        Return all customers
        """
        return Customer.objects.all()
    

def index(request):
    return render(request, "customers/index.html", {})

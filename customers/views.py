from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Customer
from django.http import Http404

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

def detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, "customers/detail.html", {"customer": customer})

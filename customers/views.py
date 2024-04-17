from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Customer, Campground
from .forms import CampgroundForm

class AllCustomersView(generic.ListView):
    template_name = "customers/customers.html"
    context_object_name = "customers_list"

    def get_queryset(self):
        """
        Return all customers
        """
        return Customer.objects.all()
    
def all_campgrounds(request):

    if request.method == 'POST':
        form = CampgroundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CampgroundForm()

    campgrounds = Campground.objects.all()
    context = {'form' : form,
               'campgrounds_list' : campgrounds }
    
    return render(request, "customers/campgrounds.html", context)

def index(request):
    return render(request, "customers/index.html", {})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, "customers/customer_detail.html", {"customer": customer})

def campground_detail(request, campground_id):
    campground = get_object_or_404(Campground, pk=campground_id)
    return render(request, 'customers/campground_detail.html', {'campground' : campground })

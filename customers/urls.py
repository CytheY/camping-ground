from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "customers"
urlpatterns = [
    path("", views.index, name="index"),
    path("customers/", views.AllCustomersView.as_view(), name="customers"),
    path("customers/<int:customer_id>/", views.customer_detail, name="customer_detail"),

    path("campgrounds/", views.all_campgrounds, name="campgrounds"),
    path("campgrounds/<int:campground_id>/", views.campground_detail, name="campground_detail"),
]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
from django.contrib import admin

from .models import Customer, Parcel, Campground

admin.site.register(Campground)
admin.site.register(Customer)
admin.site.register(Parcel)


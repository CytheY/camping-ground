from django.db import models

class Campground(models.Model):
    name = models.CharField(max_length=50)
    campground_image = models.ImageField(upload_to='campgrounds/')

    def __str__(self):
        return self.name

class Parcel(models.Model):
    campground = models.ForeignKey(Campground, on_delete=models.CASCADE)
    parcel_identifier = models.CharField(max_length=5)
    def __str__(self):
        return self.parcel_identifier

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + " " + self.sur_name + ";" + self.parcel.parcel_identifier
    
    def getFullName(self):
        return self.first_name + " " + self.sur_name
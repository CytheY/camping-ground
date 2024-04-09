from django.db import models

class PlaceId(models.Model):
    place_identifier = models.CharField(max_length=10)
    def __str__(self):
        return self.place_identifier

class Customer(models.Model):
    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    place_id = models.ForeignKey(PlaceId, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " + self.sur_name + ";" + self.place_id.place_identifier
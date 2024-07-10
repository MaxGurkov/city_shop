from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.city.name}"

class Shop(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name

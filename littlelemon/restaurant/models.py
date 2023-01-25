from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255, null=False)
    no_of_guests = models.PositiveIntegerField(null=False, blank=False)
    booking_date = models.DateTimeField(auto_now=True)


class MenuItem(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

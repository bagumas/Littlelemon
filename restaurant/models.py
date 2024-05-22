from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,  db_index=True)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'



class Book(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField() #auto_now_add=True)
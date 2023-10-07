from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AddCustomer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    Name = models.CharField(max_length=500)
    Phone = models.IntegerField()
    Date = models.DateField(auto_now=True)
    Buy_kgs = models.FloatField()
    extra_kgs = models.FloatField()
    Rate = models.IntegerField()
    Bill = models.IntegerField(null=True)
    Pending = models.CharField(max_length=1,null=True)

    def __str__(self):
        return self.Name

    class Meta:

        order_with_respect_to = 'user'


class Contact(models.Model):
    Name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    message = models.CharField(max_length=2000)

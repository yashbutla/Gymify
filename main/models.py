from django.db import models

# Create your models here.
class Member(models.Model):
    name          = models.CharField(max_length=100)
    email         = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    height        = models.CharField(max_length=10, blank=True, null=True)
    weight        = models.CharField(max_length=10, blank=True, null=True)
    start_date    = models.DateField(blank=True, null=True)
    end_date      = models.DateField(blank=True, null=True)
    fees          = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    training_type = models.CharField(max_length=50, choices=[('Normal Training', 'Normal Training'), ('Personal Training', 'Personal Training')], blank=True, null=True)
    payment        = models.BooleanField(default=False) 

    def __str__(self):
        return self.name 
from django.db import models
# Create your models here.

class student(models.Model):
    classes = [
        ('100L', '100 Level'),
        ('200L', '200 Level'),
        ('300L', '300 Level'),
        ('400L', '400 Level'),
        ('500L', '500 Level'),
    ]

    fname = models.CharField(max_length=500, verbose_name='Surname Name')
    name = models.CharField(max_length=500, verbose_name='Other Names')
    dob = models.DateField(auto_now_add=False, verbose_name='Date of Birth')
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    classes = models.CharField(max_length=50, choices=classes)
    marks = models.IntegerField(verbose_name='Percentage')
    enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


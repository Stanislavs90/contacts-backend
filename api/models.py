from django.db import models
from phone_field import PhoneField


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    company = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True, max_length=100)
    related_name = models.CharField(blank=True, max_length=100)
    birthday = models.DateField(blank=True)

    def __str__(self):
        return self.name
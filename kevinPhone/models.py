from django.db import models

# Create your models here.

class Phone(models.Model) : 
    phone_name = models.CharField(max_length=60, null=True, blank=True)
    phone_price = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    phone_review = models.TextField(max_length=1000, null=True, blank=True)
    phone_id = models.AutoField(primary_key=True)
    phone_image = models.ImageField(upload_to="phone/")

    def __str__(self):
        return f"{self.phone_name}-{self.phone_id}"

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=60)
    contact_surname = models.CharField(max_length=60, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_message = models.TextField(max_length=1000,null=True, blank=True)
    
    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"
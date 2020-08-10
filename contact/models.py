from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.full_name 
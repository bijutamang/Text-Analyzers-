from django.db import models

# Contact Models 
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField();
    number = models.IntegerField();
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
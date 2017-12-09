from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProductAdminModels(models.Model):
    """
    model for product admin. this type of admin can input the product
    """
    def __init__(self):
        """
        user name
        """
        user_name = models.CharField(max_length=30)
        email_address = models.EmailField(max_length=50)
        pass_word = models.Pa


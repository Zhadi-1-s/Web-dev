from django.db import models

"""
create table products(
    id INTEGER,
    name VARCHAR(255),
    price NUMERIC default 1000
)
"""

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=1000)
    description = models.TextField(max_length=500)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(False)

    def to_json(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description':self.description,
            'count': self.description,
            'is_active':self.is_active
        }
    
class Category(models.Model):
    name = models.CharField(max_length=255)


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


from django.db import models

CHOICES = (
    (1, 'Produce'),
    (2, 'Deli'),
    (3, 'Breads/Pasta'),
    (4, 'Snacks'),
    (5, 'Baking/Condiments'),
    (6, 'Canned Goods'),
    (7, 'Meat/Seafood'),
    (8, 'Breakfast'),
    (9, 'Beverages'),
    (10, 'Frozen Foods'),
    (11, 'Dairy'),
    (12, 'Paper/Plastic'),
    (13, 'Cleaning Products'),
    (14, 'Toiletries'),
    (15, 'Miscellaneous'),
)


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.IntegerField(choices = CHOICES)
    quantity = models.IntegerField(default=1)
    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.URLField()

    def __str__(self):
        return self.name

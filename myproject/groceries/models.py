from django.db import models

CHOICES = (
    (1, 'Produce'),
    (2, 'Meat/Seafood'),
    (3, 'Dairy'),
    (4, 'Frozen Foods'),
    (5, 'Breads/Pasta'),
    (6, 'Canned Goods'),
    (7, 'Breakfast'),
    (8, 'Snacks'),
    (9, 'Baking/Condiments'),
    (10, 'Beverages'),
    (11, 'Paper/Plastic'),
    (12, 'Cleaning Products'),
    (13, 'Toiletries'),
    (14, 'Miscellaneous'),
    (15, 'Deli'),
)


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.IntegerField(choices = CHOICES)
    quantity = models.IntegerField(default=1)
    weight = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.URLField()

    def __str__(self):
        return self.name

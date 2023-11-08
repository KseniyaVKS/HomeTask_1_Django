from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, unique=True)



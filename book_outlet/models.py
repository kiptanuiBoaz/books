from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)


class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.OneToOneField(
        Address, models.CASCADE, null=True, related_name="author"
    )


class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Author, models.CASCADE, null=True, related_name="books")
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=True, unique=True)
    published_countries = models.ManyToManyField(Country, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        self.slug = slug
        super().save(*args, **kwargs)

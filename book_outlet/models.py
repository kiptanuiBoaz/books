from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=True, unique=True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        self.slug = slug
        super().save(*args, **kwargs)

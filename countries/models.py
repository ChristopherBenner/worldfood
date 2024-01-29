from django.db import models
from django.utils.text import slugify

class Continent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)
    continent = models.ForeignKey(Continent, related_name='country', on_delete=models.CASCADE)
    slug = models.SlugField(default = "")

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

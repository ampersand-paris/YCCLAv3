from django.db import models

# Create your models here.

# Currently this model is used as a stand-in for postcard collection aka 'Summer Series', 'Pickle Pack', etc.
# Perhaps there is also a place to add Recipe Author and Illustrator in the model?

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    recipe_authors = models.CharField(max_length=100)
    illustrators = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.category_name
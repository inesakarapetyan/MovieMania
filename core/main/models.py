from django.db import models

# Create your models here.

class Logo(models.Model):
    logo = models.ImageField('Logo image', upload_to='logo', blank=True)

    def __str__(self):
        return self.logo
    

class Category(models.Model):
    name = models.CharField('Category name', max_length=50)
    img = models.ImageField('Category image', upload_to='category_img')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_movie')
    name = models.CharField('Movies name', max_length=60)
    img = models.ImageField('Movies image', upload_to='movies_img')
    rate = models.CharField('Movie rate', max_length=50)
    description = models.TextField('Movie description')


    def __str__(self):
        return self.name
    

class Cart(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


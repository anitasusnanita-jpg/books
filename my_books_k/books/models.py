from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    

class Book(models.Model):

    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    update_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title

    
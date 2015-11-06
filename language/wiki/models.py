from django.db import models


class Category(models.Model):
    name = models.CharField(max_length= 128,unique=True)
    views = models.IntegerField()
    likes = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128,unique=True)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
        
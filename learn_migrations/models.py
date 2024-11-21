from django.db import models

# Create your models here.

#we create a simple model

class Blog(models.Model):
    content = models.TextField(verbose_name='Blog Content')
    title = models.CharField(max_length=150,verbose_name='Title')
    date_published = models.DateField(verbose_name='Publication Date')


    def __str__(self):
        return self.title
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.




class VideoBackHome(models.Model):
    
    title = models.CharField(max_length=25)

    # content  = RichTextField(blank=True)
    content = models.TextField(max_length=255)
    
    videofile= models.FileField(upload_to='static/video/', null=True)

    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse('video')

class InfoForAll(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        ordering = ['id']



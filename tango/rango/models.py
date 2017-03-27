from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
class UserProfile(models.Model):
 user = models.OneToOneField(User)
 picture = models.ImageField(upload_to='profile_images' ,blank=True)
 #website = models.URLField(blank=True)
 def __unicode(self):
    return self.user.username
User._meta.get_field('email')._unique = True
class restrict (models.Model):
        name = models.CharField(max_length=128,unique=False)
        views = models.IntegerField(default=0)
        likes = models.IntegerField(default=0)
        body  =  models.TextField()
        slug = models.SlugField(unique=True)
        @models.permalink
        def get_absolute_url(self):
         return 'blog:post',(self.slug,)
# Create your models here.

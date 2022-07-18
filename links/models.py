from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from .utils import generate_random_id
from .managers import PostManager

User = get_user_model()

class PostManager(models.Manager):
    objects = models.Manager()
    public = ActiveLinkManager()

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)


    




        
    def save(self, **kwargs):
        self.identifier = slugify(generate_random_id())
        super(Link, self).save(*args, **kwargs)





# Create your models here.

from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    github = models.CharField(max_length=300)
    link = models.ChardField(max_length=300)
    slug = models.SlugField(unique=True)

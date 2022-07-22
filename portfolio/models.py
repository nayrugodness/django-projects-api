from django.db import models

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Framework(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    github = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    framework = models.ForeignKey(Framework, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
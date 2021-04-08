from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.

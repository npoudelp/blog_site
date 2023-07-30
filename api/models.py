from django.db import models
from django.utils import timezone

# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)

class Posts(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    date = models.DateField(default=timezone.now())
    author = models.CharField(max_length=25)
    tag = models.ForeignKey(Tags, on_delete=models.PROTECT, null=True)
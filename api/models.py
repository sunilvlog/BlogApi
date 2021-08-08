from django.db import models

# Create your models here.
class ArticleName(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    descryption = models.TextField(max_length=450)
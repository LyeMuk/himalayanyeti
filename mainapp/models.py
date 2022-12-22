from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class categories(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class label(models.Model):
    lid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parentcategory = models.ForeignKey(categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class article(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # headerimage = models.ImageField()
    headerimage = models.ImageField(null=True, upload_to="images")
    # author = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postdate = models.DateField(auto_now_add=True)
    # category = models.CharField(max_length=255)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    # label = models.CharField(max_length=255)
    label = models.ForeignKey(label, on_delete=models.CASCADE)
    # body = models.TextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return f"Title: {self.title} (Author: {self.author})"




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
        return f"{self.name}({self.parentcategory})"


class article(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    # headerimage = models.ImageField()
    headerimage = models.ImageField(null=True, upload_to="images")
    # author = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postdate = models.DateTimeField(editable=False, auto_now=True) 
    # category = models.CharField(max_length=255)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    # label = models.CharField(max_length=255)
    label = models.ForeignKey(label, on_delete=models.CASCADE)
    # body = models.TextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return f"Title: {self.title} (Author: {self.author})"

class subscriber(models.Model):
    eid = models.AutoField(primary_key=True)
    mail = models.EmailField(max_length = 254)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        status=""
        if self.isactive==True:
            status="ACTIVE"
        else:
            status="DEACTIVE"
        return f"{self.mail}|({status})"





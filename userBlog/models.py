from django.db import models

class MyBlogsDatabase(models.Model):
        blogTitle = models.CharField(max_length=105)
        blogContent = models.TextField(max_length=15000)
        images = models.ImageField(upload_to='blogImages/')
        slug = models.CharField(max_length=105)
        blogInfo = models.CharField(max_length=200)
        author = models.CharField(max_length=50)
        blogTimeStamp = models.DateField()

        def __str__(self):
                return self.blogTitle + ' ' + str(self.blogTimeStamp)

class ContactDatabase(models.Model):
        username = models.CharField(max_length=20)
        email = models.EmailField()
        message = models.TextField(max_length=5000)

        def __str__(self):
                return  self.username + ' ' + self.email
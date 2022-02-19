from django.db import models

'''
This is exactly what Schema does, it's called a djangoORM, which is also used in building our 
Database tables
'''

class Posts(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=400)
    body = models.TextField()
    
    def __str__(self):
        return self.title

class Comments(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    postId = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    email = models.EmailField(max_length=100)
    body = models.TextField()
                           
    def __str__(self):
        return self.name

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    items = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)
    video = models.FileField(upload_to='static/videos/', null=True, blank=True)
    #image = models.FilePathField(path="/img")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

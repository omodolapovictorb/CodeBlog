from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    #body = models.TextField()
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Post - "+ str(self.title)

    class Meta:
        ordering=['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
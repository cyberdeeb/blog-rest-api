from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=50, default='General')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
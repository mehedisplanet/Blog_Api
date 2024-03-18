from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    topic=models.CharField(max_length=30)
    note=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self):
        return f"{self.topic} {self.title}"
    


STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Reviewer : {self.reviewer.first_name} --> Blog Title : {self.blog.title}"

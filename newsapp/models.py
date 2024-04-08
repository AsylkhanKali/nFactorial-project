# models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    main_text = models.TextField()
    date_posted = models.DateField()
    time_posted = models.TimeField()
    image = models.ImageField(upload_to='news_images/')
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_posts', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_posts', null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
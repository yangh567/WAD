from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'


class Question(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category)


class Answer(models.Model):
    content = models.TextField()
    rank_points = models.IntegerField(default=0)
    rank_count = models.PositiveIntegerField(default=0)
    last_modified = models.DateTimeField(auto_now=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    popular = models.IntegerField(default=0)

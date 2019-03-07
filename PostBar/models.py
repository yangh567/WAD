from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.id])

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)

    viewed_users = models.ManyToManyField(User, related_name="viewed_questions")
    views = models.PositiveIntegerField(default=0)

    liked_users = models.ManyToManyField(User, related_name="liked_questions")
    likes = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, related_name="questions", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="questions", on_delete=models.CASCADE)

    def get_answers(self):
        return self.answers.all()

    def add_views(self, user):
        if not self.viewed_users.filter(id=user.id).exists():
            self.viewed_users.add(user)
            self.views += 1
            self.save()

    def add_likes(self, user):
        if not self.liked_users.filter(id=user.id).exists():
            self.liked_users.add(user)
            self.likes += 1
            self.save()

    def sub_likes(self, user):
        if self.liked_users.filter(id=user.id).exists():
            self.liked_users.remove(user)
            self.likes -= 1
            self.save()

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.id])


class Answer(models.Model):
    content = models.TextField()
    rank_points = models.IntegerField(default=0)
    rank_count = models.PositiveIntegerField(default=0)

    ranked_users = models.ManyToManyField(User, related_name="ranked_answers")
    last_modified = models.DateTimeField(auto_now=True)

    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="answers", on_delete=models.CASCADE)

    def add_ranks(self, user):
        if not self.ranked_users.filter(id=user.id).exists():
            self.ranked_users.add(user)
            self.rank_count += 1
            self.save()

    def sub_ranks(self, user):
        if self.ranked_users.filter(id=user.id).exists():
            self.ranked_users.remove(user)
            self.rank_count -= 1
            self.save()

    def get_absolute_url(self):
        return reverse('answer_detail', args=[self.id])

    def preview(self):
        return self.content[:50] + " ... "


class UserProfile(models.Model):
    popular = models.IntegerField(default=0)
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    location = models.CharField(max_length=128, default="")
    background = models.TextField(default="")
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def add_following(self, user_id):
        user = User.objects.get(user_id=user_id)
        if user:
            self.followings.add(user.userprofile)
            self.save()
            return True
        return False

    def delete_following(self, user_id):
        user = User.objects.get(user_id=user_id)
        if user:
            self.followings.remove(user.userprofile)
            self.save()
            return True
        return False

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.id])

    def __str__(self):
        return self.user.username

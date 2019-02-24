from django.contrib import admin
from PostBar.models import Category, Question,Answer,UserProfile

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserProfile)
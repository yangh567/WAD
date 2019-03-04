from pprint import pprint

from django.contrib import admin
from PostBar.models import Category, Question, Answer, UserProfile

from django.contrib import admin


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionInline(admin.TabularInline):
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

    def icount(self, obj):
        return obj.answers.count()

    list_display = ["title", "icount"]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]

    def icount(self, obj):
        return obj.questions.count()

    list_display = ["name", "icount"]


class UserProfileAdmin(admin.ModelAdmin):
    def name(self, obj):
        return obj.user.username

    list_display = ["name"]


class AnswerAdmin(admin.ModelAdmin):
    def name(self, obj):
        return obj.user.username

    def short_content(self, obj):
        return obj.content[:20]

    list_display = ["name", "short_content"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

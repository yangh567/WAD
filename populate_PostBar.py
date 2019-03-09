import os
from datetime import datetime
from typing import List

from autofixture import AutoFixture

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Post_Bar.settings')
import django

django.setup()
from PostBar.models import Category, Question, Answer, UserProfile
from django.contrib.auth.models import User


def populate():
    user1, profile1 = create_or_get_user_profile("john", 'jlennon@beatles.com', "passowrd", "nyu", "a@b.com", "daycare")
    user2, profile2 = create_or_get_user_profile("mary", 'mary@beatles.com', "passowrd", "nyu", "a@b.com", "daycare")
    profile1.add_following(user2.id)
    profile2.add_following(user1.id)

    math_answers = [
        {
            "answer_content": "I can swim and you can not",
            "answer_username": user1.username,
            "rank_counts": 12,
            "rank_points": 115},
        {
            "answer_content": "well that it to combine something togather",
            "answer_username": user1.username,
            "rank_counts": 12,
            "rank_points": 13},
    ]

    computing_science_answers = [
        {
            "answer_content": "study harder",
            "answer_username": user1.username,
            "rank_counts": 2,
            "rank_points": 23},
        {
            "answer_content": "read them multiple times",
            "answer_username": user1.username,
            "rank_counts": 12,
            "rank_points": 13},
    ]

    other_answers = [
        {
            "answer_content": "Yes of course ",
            "answer_username": user1.username,
            "rank_counts": 12,
            "rank_points": 131},
        {
            "answer_content": "No doubt",
            "answer_username": user1.username, "rank_counts": 12,
            "rank_points": 131}

    ]

    math_questions = [
        {
            "question_title": "What is the differentiation?",
            "question_content": "I heard a lot about differentiation during hight school,what is that exactly",
            "username": user1.username,
            "id": 0,
            "views": 31,
            "likes": 12,
            "question_isComplete": True,
            "latest_question_published": "2009-11-13",
            "answers": math_answers
        }
    ]

    computing_science_questions = [
        {
            "question_title": "How am i supposed to learn Cs?",
            "question_content": "cause it is so difficult for me!",
            "username": user1.username,
            "views": 34,
            "likes": 12,
            "question_isComplete": True,
            "latest_question_published": "2009-11-13",
            "answers": computing_science_answers
        }
    ]

    other_questions = [
        {"question_title": "Do we have to attend any of the lectures?",
         "question_content": "i know is not correct to skip any lectures,however i think some of them is not that kind of important",
         "username": user1.username,
         "views": 31,
         "likes": 12,
         "question_isComplete": True,
         "latest_question_published": "2009-11-13",
         "answers": other_answers
         }
    ]

    Cats = {
        "Math": math_questions,
        "Computing_Science": computing_science_questions,
        "Other_Questions": other_questions
    }

    for c, qs in Cats.items():
        cat = add_cat(c)
        for i, q in enumerate(qs):
            qa = add_question(cat, user1, q["question_title"], q["question_content"], q["views"], q["likes"],
                              q["latest_question_published"], q["question_isComplete"])
            q_answers = q["answers"]
            for ans in q_answers:
                add_answer(user1, qa, content=ans["answer_content"],
                           rank_count=ans["rank_counts"],
                           rank_points=ans["rank_points"])


def create_or_get_user_profile(username, email, password, location, webside, background):
    status = User.objects.filter(username=username, email=email).exists()
    if not status:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user_profile = UserProfile.objects.create(user=user, location=location, website=webside, background=background)
        user_profile.save()
    else:
        user = User.objects.filter(username=username, email=email).get()
        user_profile = user.userprofile
    return user, user_profile


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_question(category, user, title, content, views, likes, last_modified, completed):
    last_modified = datetime.strptime(last_modified, "%Y-%m-%d")
    q = Question.objects.create(user=user, category=category)
    q.title = title
    q.content = content
    q.views = views
    q.likes = likes
    q.last_modified = last_modified
    q.completed = completed
    q.save()
    return q


def add_answer(user: User, question: Question, content, rank_count=0, rank_points=0):
    a, _ = Answer.objects.get_or_create(question=question, user=user, content=content)
    a.rank_count = rank_count
    a.rank_points = rank_points
    a.save()
    return a


def gen_save(class_type, n=10):
    fixture = AutoFixture(class_type)
    objs: List[Category] = fixture.create(n)
    for obj in objs:
        obj.save()


def save_all(objects: List[Category]):
    for o in objects:
        o.save()


if __name__ == '__main__':
    populate()
    # gen_save(User)
    # gen_save(Category)
    # gen_save(Question, 50)
    # gen_save(Answer, 1500)
    # gen_save(UserProfile, 10)

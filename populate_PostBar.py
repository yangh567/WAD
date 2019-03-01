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
    status = User.objects.filter(username='john', email='jlennon@beatles.com').exists()
    if not status:
        user = User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
    else:
        user = User.objects.filter(username='john', email='jlennon@beatles.com').get()

    answers = [{"answer_id": 0,
                "answer_content": "I can swim and you can not",
                "answer_username": user.username,
                "rank_counts": 12,
                "rank_points": 115},
               {"answer_id": 1,
                "answer_content": "well that it to combine something togather",
                "answer_username": user.username,
                "rank_counts": 12,
                "rank_points": 13},
               {"answer_id": 2,
                "answer_content": "study harder",
                "answer_username": user.username,
                "rank_counts": 2,
                "rank_points": 23},
               {"answer_id": 3,
                "answer_content": "read them multiple times",
                "answer_username": user.username,
                "rank_counts": 12,
                "rank_points": 13},
               {"answer_id": 4,
                "answer_content": "Yes of course ",
                "answer_username": user.username,
                "rank_counts": 12,
                "rank_points": 131},
               {"answer_id": 5,
                "answer_content": "No doubt",
                "answer_username": user.username, "rank_counts": 12,
                "rank_points": 131}
               ]

    math_questions = [{"question_title": "What is the differentiation?",
                       "question_content": "I heard a lot about differentiation during hight school,what is that exactly",
                       "username": user.username, "id": 0, "views": 31, "likes": 12, "question_isComplete": True,
                       "latest_question_published": "2009-11-13",
                       "answers": answers[:2]
                       }]

    computing_science_questions = [
        {"question_title": "How am i supposed to learn Cs?", "question_content": "cause it is so difficult for me!",
         "username": user.username, "id": 2, "views": 31, "likes": 12, "question_isComplete": True,
         "latest_question_published": "2009-11-13",
         "answers": answers[2:4]
         }]

    other_questions = [{"question_title": "Do we have to attend any of the lectures?",
                        "question_content": "i know is not correct to skip any lectures,however i think some of them is not that kind of important",
                        "username": user.username, "id": 4, "views": 31, "likes": 12,
                        "question_isComplete": True, "latest_question_published": "2009-11-13",
                        "answers": answers[4:6]
                        }]

    Cats = {"Math": {"question": math_questions}, "Computing_Science": {"question": computing_science_questions},
            "Other_Questions": {"question": other_questions}}

    userprofile = {"popular": 120, "user": user}

    add_profile(userprofile["popular"], userprofile["user"])
    for c, qs in Cats.items():
        cat = add_cat(c)
        for i, q in enumerate(qs["question"]):
            qa = add_question(cat, user, q['id'], q["question_title"], q["question_content"], q["views"], q["likes"],
                              q["latest_question_published"], q["question_isComplete"])
            q_answers = q["answers"]
            for ans in q_answers:
                add_answer(user, qa, content=ans["answer_content"],
                           rank_count=ans["rank_counts"],
                           rank_points=ans["rank_points"])


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_question(category, user, id, title, content, views, likes, last_modified, completed):
    last_modified = datetime.strptime(last_modified, "%Y-%m-%d")
    q, _ = Question.objects.get_or_create(id=id, user=user, category=category)
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


def add_profile(popular, user):
    p = UserProfile.objects.get_or_create(popular=popular, user=user)[0]
    p.save()
    return p


def gen_save(class_type, n=10):
    fixture = AutoFixture(class_type)
    objs: List[Category] = fixture.create(n)
    for obj in objs:
        obj.save()


def save_all(objects: List[Category]):
    for o in objects:
        o.save()


if __name__ == '__main__':
    gen_save(User)
    gen_save(Category)
    gen_save(Question, 20)
    gen_save(Answer, 50)

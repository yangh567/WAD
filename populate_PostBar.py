import os

from django.db.models import QuerySet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Post_Bar.settings')
import django
import datetime

django.setup()
from PostBar.models import Category, Question, Answer, UserProfile
from django.contrib.auth.models import User


def populate():
    user, status = User.objects.get_or_create(username='john', email='jlennon@beatles.com', password='glass onion')
    # math_questions = [{"question_title":"What is the differentiation?","question_content":"I heard a lot about differentiation during hight school,what is that exactly","username":"Yang"},
    #					{"question_title":"What is the intergration?","question_content":"I heard a lot about differentiation during hight school,what is that exactly","username":"Yang"},
    #					]
    # computing_science_questions = [{"question_title":"How i am i suppose to learn Cs?","question_content":"cause it is so difficult for me!","username":"Yang"},
    #								{"question_title":"What is the best way to unserstand the code?","question_content":"i think to unserstand other's code is really hard ,is there any other way to help us better understand it ?","username":"Yang"},
    #								]
    # other_questions = [{"question_title":"Do we have to attend any of the lectures?","question_content":"i know is not correct to skip any lectures,however ithink some of them is not that kind of important","username":"Yang"},
    #					{"question_title":"Do we have to drink water every day?","question_content":"what would i do to keep myself not thirsty?","username":"Yang"},
    #					]

    answers = [{"answer_id": 0, "question_title": "what is the differentiation?", "answer_content": ".........",
                "answer_username": user.username},
               {"answer_id": 1, "question_title": "What is the intergration?", "question_content": "...........",
                "answer_username": user.username},
               {"answer_id": 2, "question_title": "How i am i suppose to learn Cs?", "answer_content": ".........",
                "answer_username": user.username},
               {"answer_id": 3, "question_title": "What is the best way to unserstand the code?",
                "answer_content": ".........", "answer_username": user.username},
               {"answer_id": 4, "question_title": "Do we have to attend any of the lectures?",
                "answer_content": ".........", "answer_username": user.username},
               {"answer_id": 5, "question_title": "Do we have to drink water every day?", "answer_content": ".........",
                "answer_username": user.username},
               ]

    math_questions = [{"question_title": "What is the differentiation?",
                       "question_content": "I heard a lot about differentiation during hight school,what is that exactly",
                       "username": user.username, "answer_id": 0, "views": 31, "likes": 12, "question_isComplete": True,
                       "latest_question_published": "2009-11-13"}]

    computing_science_questions = [
        {"question_title": "How i am i supposed to learn Cs?", "question_content": "cause it is so difficult for me!",
         "username": user.username, "answer_id": 2, "views": 31, "likes": 12, "question_isComplete": True,
         "latest_question_published": "2009-11-13"}]

    other_questions = [{"question_title": "Do we have to attend any of the lectures?",
                        "question_content": "i know is not correct to skip any lectures,however i think some of them is not that kind of important",
                        "username": user.username, "answer_id": 4, "views": 31, "likes": 12,
                        "question_isComplete": True, "latest_question_published": "2009-11-13"}]

    Cats = {"Math": {"question": math_questions}, "Computing_Science": {"question": computing_science_questions},
            "Other_Questions": {"question": other_questions}}

    userprofile = {"popular": 120, "uesr": User.username}

    def add_cat(title_name):
        c = Category.objects.get_or_create(title_name=title_name)[0]
        c.save()
        return c

    def add_question(category, question_title, question_content, username, views, likes, question_isComplete,
                     latest_question_published):
        q = Question.objects.get_or_create(category=category, question_title=question_title,
                                           question_content=question_content, username=username, views=views,
                                           likes=likes, question_isComplete=question_isComplete,
                                           latest_question_published=latest_question_published)[0]
        q.username = username
        q.views = views
        q.likes = likes
        q.question_isComplete = question_isComplete
        q.latest_question_published = latest_question_published
        q.save()
        return q

    def add_answer(user: User, question: Question, question_title, content, rank_count=0, rank_points=0):
        a = Answer.objects.create(question_title=question_title)
        a.user = user
        a.question = question
        a.content = content
        a.rank_count = rank_count
        a.rank_points = rank_points
        a.save()
        return a

    def add_profile(popular, user):
        p = UserProfile.objects.get_or_create(popular=popular, user=user)
        p.save()
        return p

    for cat, cat_data in Cats.items():
        c = add_cat(cat)
        for q_i in cat_data['question']:
            add_question(c, q_i['question_title'], q_i['question_content'], user, q_i['views'], q_i['likes'],
                         q_i['question_isComplete'], q_i['latest_question_published'])


if __name__ == '__main__':
    print("Starting PostBar population script...")
    populate()

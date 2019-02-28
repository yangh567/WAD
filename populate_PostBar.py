import os
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Post_Bar.settings')
import django

django.setup()
from PostBar.models import Category, Question, Answer, UserProfile
from django.contrib.auth.models import User


def populate():
    user, status = User.objects.get_or_create(username='john', email='jlennon@beatles.com', password='glass onion')

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
                       "username": user.username, "id": 0, "views": 31, "likes": 12, "question_isComplete": True,
                       "latest_question_published": "2009-11-13"}]

    computing_science_questions = [
        {"question_title": "How am i supposed to learn Cs?", "question_content": "cause it is so difficult for me!",
         "username": user.username, "id": 2, "views": 31, "likes": 12, "question_isComplete": True,
         "latest_question_published": "2009-11-13"}]

    other_questions = [{"question_title": "Do we have to attend any of the lectures?",
                        "question_content": "i know is not correct to skip any lectures,however i think some of them is not that kind of important",
                        "username": user.username, "id": 4, "views": 31, "likes": 12,
                        "question_isComplete": True, "latest_question_published": "2009-11-13"}]

    Cats = {"Math": {"question": math_questions}, "Computing_Science": {"question": computing_science_questions},
            "Other_Questions": {"question": other_questions}}

    userprofile = {"popular": 120, "user": user}

    add_profile(userprofile["popular"], userprofile["user"])
    for c, qs in Cats.items():
        cat = add_cat(c)
        for i, q in enumerate(qs["question"]):
            add_question(cat, user, q["question_title"], q["question_content"], q["views"], q["likes"],
                         q["latest_question_published"], q["question_isComplete"])
    # for c, qs in Cats.items():


# for ad in answers:


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_question(category, user, title, content, views, likes, last_modified, completed):
    last_modified = datetime.strptime(last_modified, "%Y-%m-%d")
    q, _ = Question.objects.get_or_create(title=title,
                                          content=content,
                                          views=views,
                                          likes=likes,
                                          user=user,
                                          category=category,
                                          last_modified=last_modified,
                                          completed=completed)
    q.save()
    return q


def add_answer(user: User, question: Question, content, rank_count=0, rank_points=0):
    a = Answer.objects.create(question=question,
                              user=user,
                              content=content,

                              )
    a.user = user
    a.question = question
    a.content = content
    a.rank_count = rank_count
    a.rank_points = rank_points
    a.save()
    return a


def add_profile(popular, user):
    p = UserProfile.objects.get_or_create(popular=popular, user=user)[0]
    p.save()
    return p


# for cat, cat_data in Cats.items():
#     c = add_cat(cat)
#     for q_i in cat_data['question']:
#         add_question(c, q_i['question_title'], q_i['question_content'], user, q_i['views'], q_i['likes'],
#                      q_i['question_isComplete'], q_i['latest_question_published'])

if __name__ == '__main__':
    populate()

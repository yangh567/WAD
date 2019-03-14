from django.conf.urls import url
from PostBar import views
from PostBar.views import question_like_up, answer_rank_up, answer_rank_down, question_like_down

urlpatterns = [
    url(r'^$', views.QuestionListView.as_view(), name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),

    # user profile
    url(r'^user_profile_detail/(?P<user_id>\d+)/$', views.user_profile_detail, name='user_profile_detail'),
    url(r'^edit_user_profile/$', views.edit_user_profile, name='edit_user_profile'),
    url(r'^user_profile_list/(?P<page>\d+)$', views.edit_user_profile, name='user_profile_list'),

    # following system
    url(r'^following_list/(?P<user_id>\d+)/(?P<page>\d+)$', views.following_list, name='following_list'),
    url(r'^follower_list/(?P<user_id>\d+)/(?P<page>\d+)$', views.follower_list, name='follower_list'),

    url(r'^add_following/(?P<user_id>\d+)$', views.add_following, name='add_following'),
    url(r'^delete_following/(?P<user_id>\d+)$', views.delete_following, name='delete_following'),

    url(r'^if_following/(?P<user_id>\d+)$', views.if_following, name='if_following'),

    # user profile
    # url(r'^user_profile_detail/(?P<pk>\d+)$', views.UserProfileDetail.as_view(), name='user_profile_detail'),

    # Category
    url(r'^category_create/$', views.CategoryCreateView.as_view(), name='category_create'),
    url(r'^category_update/(?P<pk>\d+)$', views.CategoryUpdateView.as_view(), name='category_update'),
    url(r'^category_detail/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^category_list$', views.CategoryListView.as_view(), name='category_list'),

    # question
    url(r'^question_create/$', views.QuestionCreateView.as_view(), name='question_create'),
    url(r'^question_update/(?P<pk>\d+)$', views.QuestionUpdateView.as_view(), name='question_update'),
    url(r'^question_detail/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^question_list$', views.QuestionListView.as_view(), name='question_list'),
    url(r'^question_like_up/(?P<pk>\d+)$', views.question_like_up, name='question_like_up'),
    url(r'^question_like_down/(?P<pk>\d+)$', views.question_like_down, name='question_like_down'),
    url(r'^question_liked/(?P<pk>\d+)$', views.question_liked, name='question_liked'),

    # answer
    url(r'^answer_detail/(?P<pk>\d+)$', views.AnswerDetailView.as_view(), name='answer_detail'),
    url(r'^answer_create/(?P<question_id>\d+)$', views.AnswerCreateView.as_view(), name='answer_create'),
    url(r'^answer_update/(?P<pk>\d+)$', views.AnswerUpdateView.as_view(), name='answer_update'),
    url(r'^answer_rank_up/(?P<pk>\d+)$', views.answer_rank_up, name='answer_rank_up'),
    url(r'^answer_rank_down/(?P<pk>\d+)$', views.answer_rank_down, name='answer_rank_down'),
    url(r'^answer_delete/(?P<pk>\d+)/(?P<question_id>\d+)$', views.answer_delete, name='answer_delete'),

    url(r'^query_ip/$', views.query_ip, name="query_ip")
]

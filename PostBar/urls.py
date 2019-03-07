from django.conf.urls import url
from PostBar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),

    # user profile
    url(r'^user_profile_detail/(?P<user_id>\d+)/$', views.user_profile_detail, name='user_profile_detail'),
    url(r'^edit_user_profile/$', views.edit_user_profile, name='edit_user_profile'),
    url(r'^user_profile_list/(?P<page>\d+)$', views.user_profile_list, name='user_profile_list'),

    # following system
    url(r'^following_list/(?P<user_id>\d+)/(?P<page>\d+)$', views.following_list, name='following_list'),
    url(r'^follower_list/(?P<user_id>\d+)/(?P<page>\d+)$', views.follower_list, name='follower_list'),
    url(r'^add_following/$', views.add_following, name='add_following'),
    url(r'^delete_following/$', views.delete_following, name='delete_following'),

    # Category
    url(r'^category_update/(?P<pk>\d+)$', views.CategoryUpdateView.as_view(), name='category_update'),
    url(r'^category_detail/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^category_list$', views.CategoryListView.as_view(), name='category_list'),

    # question
    url(r'^question_update/(?P<pk>\d+)$', views.QuestionUpdateView.as_view(), name='question_update'),
    url(r'^question_detail/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^question_list$', views.QuestionListView.as_view(), name='question_list')
]

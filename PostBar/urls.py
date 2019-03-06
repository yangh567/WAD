from django.conf.urls import url
from PostBar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^about/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^user_profile/detail/(?P<user_id>\d+)/$', views.user_profile_detail, name='user_profile_detail'),
    url(r'^user_profile/edit$', views.edit_user_profile, name='edit_user_profile'),
    url(r'^user_profile/list$', views.user_profile_list, name='user_profile_list'),
]

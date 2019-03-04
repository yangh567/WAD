from django.conf.urls import url
from PostBar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^about/',views.about,name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    ]
=======
	url(r'^about/',views.about,name='about'),

]
>>>>>>> 219e6a19a9e31be40f45ee78b5ab14e33b92de29

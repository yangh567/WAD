from django.test import TestCase

from PostBar.models import Category
from django.core.urlresolvers import reverse
from django.apps import apps
from PostBar.apps import PostbarConfig
from PostBar.context import additional_categories_list
from PostBar.models import Category


from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY

from django.test import TestCase
from django.test import Client
from .forms import *   # import all forms
from . import views
from django.urls import resolve


class Test_App(TestCase):
    
    def test_apps(self):
        self.assertEqual(PostbarConfig.name, 'PostBar')
        self.assertEqual(apps.get_app_config('PostBar').name, 'PostBar')




# website used for index page and about page: https://wsvincent.com/django-testing-tutorial/
class Test_Index_Page(TestCase):
    
    def test_home_page_status_code(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)


    def test_index_uses_base_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'PostBar/base.html')

    def test1_index_uses_question_list_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'PostBar/question_list.html')

    def test_index_contains_home_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Home</title>')

    def test_index_contains_popular_questions(self):
        response = self.client.get('/')
        self.assertContains(response, '<strong>Popular Questions</strong>')

    def test_index_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


class Test_About_Page(TestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'PostBar/about.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/about/')
        self.assertContains(response, '<title>About</title>')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_about_using_template(self): 
        self.client.get(reverse('index'))
        response = self.client.get(reverse('about'))

        # Check the template used to render about page
        self.assertTemplateUsed(response, 'PostBar/about.html')

    def test_about_contain_image(self):
        self.client.get(reverse('index'))
        response = self.client.get(reverse('about'))

        # Check if is there an image in index page
        self.assertIn('img src="/static/images/', response.content.decode('ascii'))


class Test_Login(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        
    def test_login(self):
        # login
        response = self.client.post('/login/', self.credentials, follow=True)      
        # should be logged in now, fails however
        self.assertTrue(response.context['user'].is_authenticated)

    def test_user_login(self):
        user_login = User.objects.create(username="use",email="user@mp.com", password="user")
        self.assertTrue(user_login)
        
        response = self.client.get("/edit_user_profile/")
        self.assertEqual(response.status_code, 302)
        
        
    def test_login_status(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

        
    def test_login_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'PostBar/login.html')


class Test_View(TestCase):
    

    def test_view_has_title(self): ###
        response = self.client.get(reverse('index'))

        #Check title used correctly
        self.assertIn('<title>', response.content.decode('ascii'))




#-------------------------- test form.py    start

class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="use",email="user@mp.com", password="user")

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'username': "use", 'email': "user@mp.com", 'password': "user"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'email': "", 'password': "mp"})
        self.assertFalse(form.is_valid())



#-------------------------- test form.py    end

class Test_Url(TestCase):

    def test_Url_user_profile_detail(self):
        url = reverse('user_profile_detail', args=[1988])
        self.assertEqual(url, '/user_profile_detail/1988/')

    def test_Url_user_following_list(self):
        url = reverse('follower_list', args=[1988,1234])
        self.assertEqual(url, '/follower_list/1988/1234')
        
        

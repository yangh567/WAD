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

from django.contrib.staticfiles.storage import staticfiles_storage #The file storage engine to use when collecting static files with the collectstatic management command.
from django.contrib.staticfiles import finders



from populate_PostBar import populate



class Test_App(TestCase):
    
    def test_apps(self):
        self.assertEqual(PostbarConfig.name, 'PostBar')
        self.assertEqual(apps.get_app_config('PostBar').name, 'PostBar')

# website used for index page and about page: https://wsvincent.com/django-testing-tutorial/
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

class Test_Index_Page(TestCase):
    
    def test_index_status_code(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_index_page_url_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
    def test_index_uses_base_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'PostBar/base.html')

    def test1_index_uses_question_list_template(self):
        response = self.client.get(reverse('index'))
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

    def test_url_reference_in_index_page_when_not_logged(self):
        #Access index page with user not logged
        response = self.client.get(reverse('index'))

        # Check links that appear for logged person only
        self.assertIn(reverse('register'), response.content.decode('ascii'))
        self.assertIn(reverse('login'), response.content.decode('ascii'))
        self.assertIn(reverse('about'), response.content.decode('ascii'))


    def test_link_to_index_in_base_template(self):
        # Access index
        response = self.client.get(reverse('index'))

        # Check for url referencing index
        self.assertIn(reverse('index'), response.content.decode('ascii'))
        
    
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


    def test_about_uses_base_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'PostBar/base.html')

        
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

    def test_about_contain_correct_image(self):
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

        
    def test_login_url_status(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        
    def test_login_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'PostBar/login.html')


    def test_theoretical_username(self):
        User.objects.create(username="use",email="user@mp.com", password="user")
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')


    def test_username_max_length(self):
        User.objects.create(username="use",email="user@mp.com", password="user")
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 150)


    def test_practical_username(self):
        User.objects.create(username="use",email="user@mp.com", password="user")
        user = User.objects.get(id=1)
        expected_object_name = f'{user.username}'
        self.assertEquals(expected_object_name, str(user))


    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('images/bg.jpg')
        self.assertIsNotNone(result)

    def test_url_reference_in_index_page_when_logged(self):
        # Create user and log in
        self.client.login(username="use", email= "user@mp.com", password= "user")

        # Access index page
        response = self.client.get(reverse('index'))
        # Check links that appear for logged person only
        self.assertIn(reverse('question_create'), response.content.decode('ascii'))
        self.assertIn(reverse('category_list'), response.content.decode('ascii'))
        self.assertIn(reverse('about'), response.content.decode('ascii'))


class Test_Login_Out(TestCase):
    
    def test_url_reference_in_index_page_when_not_logged(self):
        #Access index page with user not logged
        response = self.client.get(reverse('index'))

        # Check links that appear for logged person only
        self.assertIn(reverse('register'), response.content.decode('ascii'))
        self.assertIn(reverse('login'), response.content.decode('ascii'))
        self.assertIn(reverse('about'), response.content.decode('ascii'))




    
class Test_View(TestCase):

    def test_view_has_title(self):
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



class Test_Population_Script(TestCase):
    
    def test_create_a_new_category(self):
        cat = Category(name="Maths question")
        cat.save()

        # Check category is in database
        categories_in_database = Category.objects.all()
        self.assertEquals(len(categories_in_database), 1)
        only_poll_in_database = categories_in_database[0]
        self.assertEquals(only_poll_in_database, cat)



#class other_test(TestCase):



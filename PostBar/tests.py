from django.test import TestCase

# Create your tests here.


# Chapter 3
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.core.urlresolvers import reverse
import os
import socket

# ===== CHAPTER 3

class Chapter3LiveServerTests(StaticLiveServerTestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options = chrome_options)
        self.browser.implicitly_wait(3)

    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(Chapter3LiveServerTests, cls).setUpClass()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_navigate_from_index_to_about(self):
        # Go to main page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        print(url)
        self.browser.get(url + reverse('index'))

        # Search for a link to About page
        about_link = self.browser.find_element_by_partial_link_text("About")
        about_link.click()

        # Check if it goes back to the home page
        self.assertIn(url + reverse('about'), self.browser.current_url)

    def test_navigate_from_about_to_index(self):
        # Go to main page
        self.client.get(reverse('index'))
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('about'))

        # Check if there is a link back to the home page
        # link_to_home_page = self.browser.find_element_by_tag_name('a')
        link_to_home_page = self.browser.find_element_by_link_text('Index')
        link_to_home_page.click()

        # Check if it goes back to the home page
        self.assertEqual(url + reverse('index'), self.browser.current_url)


class Chapter3ViewTests(TestCase):
    def test_index_contains_hello_message(self):  
        # Check if there is the message 'hello world!'
        response = self.client.get(reverse('index'))
        self.assertIn('Popular Questions'.lower(), response.content.decode('ascii').lower())
        # file.write('test_index_contains_hello_message\n')

    def test_about_contains_contact_information(self):
        # Check if in the about page is there a message
        # self.client.get(reverse('index'))
        response = self.client.get(reverse('about'))
        self.assertIn('Contact Information'.lower(), response.content.decode('ascii').lower())

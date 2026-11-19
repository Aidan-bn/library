from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

# Create your tests here.
# class HomePageTests(SimpleTestCase):
#   def test_url_exist_in_correct_location(self):
#     response = self.client.get('/')
#     self.assertEqual(response.status_code, 200)

#   def test_homepage_url_name(self):
#     response = self.client.get(reverse('home'))
#     self.assertEqual(response.status_code, 200)

#   def test_homepage_template(self):
#     response = self.client.get('/')
#     self.assertTemplateUsed(response, 'home.html')

#   def test_homepage_contains_correct_html(self):
#     response = self.client.get('/')
#     self.assertContains(response, 'Home Page')

#   def test_homepage_does_not_contain_incorrect_html(self):
#     response = self.client.get('/')
#     self.assertNotContains(response, 'Hello there, I am ot in')

class HomepageTest(SimpleTestCase):
  def setUp(self):
    url = reverse('home')
    self.response = self.client.get(url)

  def test_url_exist_at_correct_location(self):
    self.assertEqual(self.response.status_code, 200)

  def test_homepage_template(self):
    self.assertTemplateUsed(self.response, 'home.html')

  def test_homepage_contains_correct_html(self):
    self.assertContains(self.response, 'Home Page')

  def test_homepage_url_resolves_homepageview(self):
    view = resolve('/')
    self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
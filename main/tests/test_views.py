from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LogoutUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_logout_user(self):
        response = self.client.get(reverse('main:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main:main'))


class MainViewTest(TestCase):
    def test_main_view(self):
        url = reverse('main:main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/news.html')
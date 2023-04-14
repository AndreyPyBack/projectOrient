from django.test import TestCase

# Create your tests here.

class TestArciv(TestCase):

    def text_register(self):
        response = self.client.get('/arxiv/')
        self.assertEqual(response.status_code,200)
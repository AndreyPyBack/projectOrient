from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from ..models import Training


class OrientationTrainingTest(TestCase):
    def setUp(self):
        self.training = Training.objects.create(
            training_title='Тестовый тренинг',
            summary_training='Описание тестового тренинга',
            slug='testovyi-trening',
            date_of_publication=timezone.now()
        )
        self.url = reverse('main:tra', kwargs={'slug': self.training.slug})

    def test_orientation_training_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'training/training.html')
        self.assertEqual(response.context['orientation_training'], self.training)


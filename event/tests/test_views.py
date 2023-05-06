from django.test import TestCase
from django.urls import reverse
from ..models import Event



# class EventTest(TestCase):
#     def setUp(self):
#         self.event = Event.objects.create(
#             date_event='2023-05-01 00:00:00',
#             slug='test-event',
#             title_event='Тестовое событие',
#             place_realization='Тестовое место',
#             illustration_event='media/event/test.jpg',
#             brief_announcement='Тестовое объявление',
#             link_to_position='https://example.com/test-event'
#         )
#         self.url = reverse('main:ev', kwargs={'slug': self.event.slug})
#
#     def test_event_view(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'event/event.html')
#         self.assertEqual(response.context['event_news'], self.event)




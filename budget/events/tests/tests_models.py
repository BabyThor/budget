from datetime import date

from django.test import TestCase

from ..models import Event

class EventTest(TestCase):
	def tests_create_event_successfully(self):
		event = Event()
		event.name = 'First Event'
		event.event_date = date(2015, 01, 01)
		event.budget_amount = 10000
		event.note = 'This is first event'

		self.assertFalse(event.id)

		event.save()

		self.assertTrue(event.id)
		event_objs = Event.objects.all()

		self.assertEqual(1, len(event_objs))
		self.assertEqual('First Event', event_objs[0].name)
		self.assertEqual(date(2015, 01, 01), event_objs[0].event_date)
		self.assertEqual(10000, event_objs[0].budget_amount)
		self.assertEqual('This is first event', event_objs[0].note)
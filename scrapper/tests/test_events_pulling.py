from django.test.testcases import TestCase
from django.urls import reverse

from scrapper.dataset import (
    EVENTS, EVENT_WITH_PLACE_AND_DATES, EVENT_WITH_PLACES_AND_DATE, EVENT_WITH_PLACES_AND_DATES
)
from scrapper.models import Event, Date, Place
from scrapper.utils import Mapper


class TestPullingData(TestCase):
    def test_scraping_events(self):
        response = self.client.get(reverse('get_events_dataset'))
        mapping = Mapper(
            dictionary=response.json(),
        )
        if mapping.is_valid():
            mapping.save_to_db()
        self.assertEqual(Event.objects.all().count(), len(EVENTS))

    def test_handling_multiple_dates(self):
        mapping = Mapper(
            dictionary=EVENT_WITH_PLACE_AND_DATES,
        )
        if mapping.is_valid():
            mapping.save_to_db()

        self.assertEqual(Event.objects.all().count(), 1)
        self.assertEqual(Date.objects.all().count(), 2)
        self.assertEqual(Event.objects.last().date.all().count(), 2)
        self.assertEqual(Event.objects.last().place.all().count(), 1)

    def test_handling_multiple_places(self):
        mapping = Mapper(
            dictionary=EVENT_WITH_PLACES_AND_DATE,
        )
        if mapping.is_valid():
            mapping.save_to_db()

        self.assertEqual(Event.objects.all().count(), 1)
        self.assertEqual(Place.objects.all().count(), 2)
        self.assertEqual(Event.objects.last().place.all().count(), 2)
        self.assertEqual(Event.objects.last().date.all().count(), 1)

    def test_handling_multiple_places_and_dates(self):
        mapping = Mapper(
            dictionary=EVENT_WITH_PLACES_AND_DATES,
        )
        if mapping.is_valid():
            mapping.save_to_db()

        self.assertEqual(Event.objects.all().count(), 1)
        self.assertEqual(Place.objects.all().count(), 2)
        self.assertEqual(Date.objects.all().count(), 2)
        self.assertEqual(Event.objects.last().place.all().count(), 2)
        self.assertEqual(Event.objects.last().date.all().count(), 2)

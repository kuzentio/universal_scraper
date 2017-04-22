from django.test.testcases import TestCase
from django.urls import reverse

from scraper.dataset import (
    EVENTS, EVENT_WITH_PLACE_AND_DATES, EVENT_WITH_PLACES_AND_DATE, EVENT_WITH_PLACES_AND_DATES,
    DATES
)
from scraper.models import Event, Date, Place
from scraper.utils import Mapper, find


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


class TestFindInDict(TestCase):
    def test_getting_values_by_key(self):
        start_dates = [date for date in find('start', EVENT_WITH_PLACES_AND_DATES['event'])]
        self.assertEquals(len(start_dates), 2)
        self.assertEquals(start_dates, [DATES[0]['start'], DATES[1]['start']])

    def test_return_all_nested(self):
        start_dates = [date for date in find('start', EVENT_WITH_PLACES_AND_DATES)]
        self.assertEquals(len(start_dates), 2)
        self.assertEquals(start_dates, [DATES[0]['start'], DATES[1]['start']])

from django.test.testcases import TestCase
from django.urls import reverse

from scrapper.utils import Mapper


class TestPullingData(TestCase):
    def test_mapping_direct_events(self):
        response = self.client.get(reverse('get_events_dataset'))
        mapping = Mapper(
            dictionary=response.json(),
        )
        if mapping.is_valid():
            mapping.save_to_db()

    def test_handling_multiple_dates(self):
        pass

    def test_handling_multiple_places(self):
        pass

    def test_handling_multiple_places_and_dates(self):
        pass

    def test_handling_direct_dates_and_places(self):
        pass

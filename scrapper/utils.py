from scrapper import models


class Mapper(object):
    def __init__(self, dictionary, *args, **kwargs):
        self.dictionary = dictionary
        self.event_key = kwargs.get('event_key', 'event')
        self.date_key = kwargs.get('date_key', 'date')
        self.place_key = kwargs.get('place_key', 'place')

    def is_valid(self):
        if not isinstance(self.dictionary, dict):
            raise Exception("Not valid incoming data")
        return True

    def save_dates(self, event_data):
        incoming_dates = event_data.get(self.date_key)
        dates = []
        if isinstance(incoming_dates, dict):
            dates.append(
                models.Date.objects.create(
                    start=incoming_dates.get('start'),
                    end=incoming_dates.get('end')
                )
            )
        if isinstance(incoming_dates, list):
            for date in incoming_dates:
                dates.append(
                    models.Date.objects.create(
                        start=date.get('start'),
                        end=date.get('end')
                    )
            )
        return dates

    def save_places(self, event_data):
        incoming_places = event_data.get(self.place_key)
        places = []
        if isinstance(incoming_places, dict):
            places.append(
                models.Place.objects.create(
                    name=incoming_places.get('name'),
                )
            )
        if isinstance(incoming_places, list):
            for place in incoming_places:
                places.append(
                    models.Place.objects.create(
                        name=place.get('name'),
                    )
                )
        return places

    def save_to_db(self):
        for event_data in find(self.event_key, self.dictionary):
            event, _ = models.Event.objects.get_or_create(
                name=event_data.get('name')
            )
            places = self.save_places(event_data)
            dates = self.save_dates(event_data)
            event.place.add(*places)
            event.date.add(*dates)
            event.save()


def find(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

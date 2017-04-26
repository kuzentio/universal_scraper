from django.db.models import Model
from scraper import models


class Mapper(object):
    model = models.Event
    model_key = 'event'
    mapping = {
        'name': 'name',
        'place': models.Place,
        'date': models.Date,
    }

    def __init__(self, dictionary, *args, **kwargs):
        self.dictionary = dictionary
        self.created_instances = {}
        for k, v in self.mapping.iteritems():
            try:
                self.created_instances[k] = [] if issubclass(v, Model) else None
            except TypeError:
                pass

    def is_valid(self):
        if not isinstance(self.dictionary, dict):
            raise Exception("Not valid incoming data")
        return True

    def save_to_db(self):
        for payload in find(self.model_key, self.dictionary):
            data = {}
            related_objects = {}
            for key in self.mapping.keys():
                if not payload[key].__class__.__name__ in ['dict', 'list']:
                    data[key] = payload[key]
                else:
                    related_objects[key] = payload[key]
            self.proceed_relation_objects(related_objects)
            node, _ = self.model.objects.get_or_create(**data)
            record, _ = self.model.objects.update_or_create(id=node.id, defaults=self.created_instances)

            return record

    def proceed_relation_objects(self, objects):
        for object_key in objects:
            if not isinstance(objects[object_key], list):
                instance, _ = self.mapping[object_key].objects.get_or_create(
                    **objects[object_key]
                )
                self.created_instances[object_key].append(instance.pk)

            else:
                for obj in objects[object_key]:
                    self.proceed_relation_objects({object_key: obj})


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

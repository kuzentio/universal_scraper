from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'{}. {}'.format(self.id, self.name)


class Date(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return u'{} - {}'.format(self.start, self.end)


class Event(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    place = models.ManyToManyField('scrapper.Place', related_name='places')
    data = models.ManyToManyField('scrapper.Date', related_name='dates')

    def __unicode__(self):
        return u'{}. {}'.format(self.name, self.id)

from django.contrib import admin

from scrapper.models import Date, Place, Event


admin.site.register(Date)
admin.site.register(Event)
admin.site.register(Place)

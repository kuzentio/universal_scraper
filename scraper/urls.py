from django.conf.urls import url

from scraper import views

urlpatterns = [
    url(r'^get_events/', views.get_events_dataset, name='get_events_dataset'),
]


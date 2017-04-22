from django.http.response import JsonResponse

from scraper.dataset import EVENTS


def get_events_dataset(request):
    return JsonResponse({'events': EVENTS})

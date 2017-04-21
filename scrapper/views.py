from django.http.response import JsonResponse

from scrapper.dataset import EVENTS


def get_events(request):
    return JsonResponse({'events': EVENTS})


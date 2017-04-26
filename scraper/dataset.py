PLACES = [
    {
        'name': 'Palace1'
    },
    {
        'name': 'Palace2'
    },
]

DATES = [
    {
        'start': '2017-04-22',
        'end': '2017-04-22'
    },
    {
        'start': '2017-04-23',
        'end': '2017-04-23'
    },
]

EVENT_WITH_PLACES_AND_DATES = {
    'event': {
        'name': 'Django conf',
        'place': PLACES,
        'date': DATES,
    }
}
EVENT_WITH_PLACE_AND_DATES = {
    'event': {
        'name': 'Python conf',
        'place': PLACES[0],
        'date': DATES,
    }
}

EVENT_WITH_PLACES_AND_DATE = {
    'event': {
        'name': 'Python/Django conf',
        'place': PLACES,
        'date': DATES[0],
    }
}

EVENT_WITH_PLACE_AND_DATE = {
    'event': {
        'name': 'Advance python',
        'place': PLACES[0],
        'date': DATES[0],
    }
}

EVENTS = [
    EVENT_WITH_PLACES_AND_DATES,
    EVENT_WITH_PLACE_AND_DATES,
    EVENT_WITH_PLACES_AND_DATE,
    EVENT_WITH_PLACE_AND_DATE,
]


EVENTS = [
    EVENT_WITH_PLACE_AND_DATE,
    # EVENT_WITH_PLACES_AND_DATES,
    # EVENT_WITH_PLACE_AND_DATES,
    # EVENT_WITH_PLACES_AND_DATE,
    # EVENT_WITH_PLACE_AND_DATE,
]
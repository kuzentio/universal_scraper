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
        'start': '2017-04-22',
        'end': '2017-04-22'
    },
]

EVENTS = [
    {
        'event': {
            'place': PLACES[0],
        },
    },
    {
        'event': {
            'date': DATES[0],
        },
    },
    {
        'event': {
            'place': PLACES[0],
            'date': DATES[0],
        },
    },
    {
        'event': {
            'place': PLACES
        },
    },
    {
        'event': {
            'place': PLACES,
            'date': DATES[0],
        },
    },
    {
        'event': {
            'place': PLACES,
            'date': DATES,
        },
    },
    {
        'event': {
            'date': DATES,
        },
    },
    {
        'event': {
            'place': PLACES[0],
            'date': DATES,
        },
    },
    {
        'event': {
            'place': PLACES,
            'date': DATES,
        },
    },
]

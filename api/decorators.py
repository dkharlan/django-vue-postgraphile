import json
from functools import partial
from collections import Iterable

from toolz.dicttoolz import keymap
from django.http import HttpResponse

from api.util import to_camel_case


def json_response(view):
    camel_caser = partial(keymap, to_camel_case)

    def wrapper(*args, **kwargs):
        data = view(*args, **kwargs)
        is_iterable = isinstance(data, Iterable)
        is_dict = isinstance(data, dict)

        if is_iterable and not is_dict:
            content = list(map(camel_caser, data))
        else:
            content = camel_caser(data)

        return HttpResponse(content=json.dumps(content),
                            content_type='application/json')
    return wrapper

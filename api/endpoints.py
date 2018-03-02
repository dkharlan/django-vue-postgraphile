from django.http import Http404

from api.models import TodoItem
from api.decorators import json_response


@json_response
def todo_items(request, item_id):
    if item_id == 'all':
        items = TodoItem.objects.all().order_by('id')
        data = map(lambda td: td.to_dict(), items)
    else:
        try:
            data = [TodoItem.objects.get(id=item_id).to_dict()]
        except TodoItem.DoesNotExist:
            raise Http404
    return data

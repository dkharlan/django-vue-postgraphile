import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def who_am_i(request):
    return JsonResponse({'username': request.user.username})


@login_required
def tell_me_something(request):
    if request.method != 'POST':
        response = JsonResponse({'error': 'Method not allowed'})
        response.status_code = 405
    else:
        body = json.loads(request.body)
        response = JsonResponse({'message_was': body['message']})
    return response

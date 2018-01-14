from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


@login_required
def who_am_i(request):
    return JsonResponse({'username': request.user.username})

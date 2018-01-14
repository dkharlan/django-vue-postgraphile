import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required
def who_am_i(request):
    return json.dumps({'username': request.session['user'].username})

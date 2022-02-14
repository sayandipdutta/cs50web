from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


# Create your views here.
def index(request):
    today = datetime.today()
    is_new_year = (
        today.day == today.month == 1
    )
    return render(
        request,
        'newyear/index.html',
        {
            'newyear': is_new_year,
        }
    )

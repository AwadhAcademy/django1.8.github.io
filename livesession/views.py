# from django.Http import HttpResponse
from django.shortcuts import render
from .models import livesession_Links

def live(request):
    record=livesession_Links.objects.all()
    record={'record':record}
    return render(request, 'live.html',record)

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def start(request):
    # return HttpResponse("Hello")
    return render(request, 'index.html')


def programming(request):
    return render(request, 'programming.html')


def class9(request):
    return render(request, '9.html')


def class8(request):
    return render(request, '8.html')


def class10(request):
    return render(request, '10.html')


def contact(request):
    return render(request, 'contact.html')


def basic(request):
    return render(request, 'courses/basic/basic2.html')


def ccpp(request):
    return render(request, 'courses/cc++/cc++.html')


def python(request):
    return render(request, 'courses/python/python.html')


def webdevlopment(request):
    return render(request, 'courses/webdevlopment/webdevlopment.html')


def django(request):
    return render(request, 'courses/django/django.html')


def androidstudio(request):
    return render(request, 'courses/androidstudio/androidstudio.html')


def booklist(request):
    return render(request, 'booklist.html')


# def family(request):
#     user=UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     data={'form':user}
#     return render(request, 'registration.html',data)

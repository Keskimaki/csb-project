from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def login(request):
    if request.method == 'POST':
        body = request.POST

    return render(request, 'pages/login.html')

def id_generator():
    id = User.objects.latest('id').id
    id += 1
    return id

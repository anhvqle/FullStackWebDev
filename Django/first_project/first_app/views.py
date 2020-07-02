from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"My name is Anh Le. Nice to Meet You!"}
    return render(request, 'first_app/index.html', context = my_dict)

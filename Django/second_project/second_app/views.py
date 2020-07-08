from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User

def home(request):
    return render(request, 'second_app/home.html')

def userInfo(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users_info' : user_list}
    return render(request, 'second_app/user.html', context = user_dict)

# Create your views here.

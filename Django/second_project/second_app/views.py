from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
from second_app.forms import NewUserForm

def home(request):
    return render(request, 'second_app/home.html')

def userInfo(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users_info' : user_list}
    # return render(request, 'second_app/user.html', context = user_dict)
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return home(request)
        else:
            print("ERROR FORM INVALID")

    return render(request, 'second_app/user.html', {'form' : form})

# Create your views here.

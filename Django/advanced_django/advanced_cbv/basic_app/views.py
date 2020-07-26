from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# def index(request):
#     return render(request, 'index.html')

class CBView(View):
    def get(self, request):
        return HttpResponse("Class based views")

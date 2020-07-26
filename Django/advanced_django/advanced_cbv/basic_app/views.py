from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# def index(request):
#     return render(request, 'index.html')
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context

class CBView(View):
    def get(self, request):
        return HttpResponse("Class based views")

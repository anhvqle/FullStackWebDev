from django.contrib import admin
from django.urls import path
from second_app import views

urlpatterns = [
    path('', views.help, name='help'),
    # path('admin/', admin.site.urls),
]

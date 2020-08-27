from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroup.as_view(), name = 'all'),
    path('new/', views.CreateGroup.as_view(), name = 'create'),
    path('posts/in/(?P<slug>[-\w]+/)', views.SingleGroup.as_view(), name = 'single'),
]
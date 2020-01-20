from django.conf.urls import url
from . import views
urlpatterns = [
    url('posts',views.Getpostpage),
    url('createpost',views.Createpost),
]

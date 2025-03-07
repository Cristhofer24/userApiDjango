from django.urls import path
from .views import users_list,user_detail

urlpatterns = [
    path("", users_list, name='users_list'),
    path("user/<int:id>", user_detail, name='user_detail'),
]
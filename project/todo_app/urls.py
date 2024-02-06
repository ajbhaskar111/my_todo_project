from django.urls import path
from .views import *

urlpatterns = [
    path("", index,name="index"),
    path("register-page", register_page,name="register-page"),
    path("reset-page", reset_password_page,name="reset-page"),
    path("links_page", link_page,name="links_page"),
    path("todo-list/", todo_list_page,name="todo_list_page"),
    path("todo-detail/", todo_detail_page,name="todo-detail"),
    path("user-profile/", user_profile_page,name="user-profile"),
]

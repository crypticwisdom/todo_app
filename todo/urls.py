from django.contrib.auth import logout
from django.urls import path
from todo.views import index, login_page, logout_handler, register_page, user_page, edit, delete

app_name = 'todo'

urlpatterns = [
    path('', index, name="index"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('logout/', logout_handler, name="logout_handler"),
    path('profile/<int:pk>', user_page, name="user_page"),
    path('Update/<int:pk>', edit, name="edit"),
    path('Delete/<int:pk>', delete, name="delete"),

]
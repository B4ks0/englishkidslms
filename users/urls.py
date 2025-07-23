from django.urls import path
from .views import course_redirect, home, lobby
from .views import home,profile_view, change_password, CustomLoginView, register, custom_login


urlpatterns = [
    path('', home, name='home'),  # <- ini paling atas biar jadi root
    path('dashboard/', home, name='dashboard_redirect'),
    path('belajar/', course_redirect, name='course_redirect'),  # ✅ Bukan 'course_list'
    path('profile/', profile_view, name='profile'),
    path('profile/password/', change_password, name='change_password'),
    path('login/', custom_login, name='login'),
    path('register/', register, name='register'),
]



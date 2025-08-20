from django.urls import path
from blog.views import UserLoginView, UserLogoutView, home, register, profile

app_name = 'blog'  # Set the app name

urlpatterns = [
    path('', home, name='home'),
    path('login/', UserLoginView.as_view(), name='login_short'),
    path('logout/', UserLogoutView.as_view(), name='logout_short'),
    path('register/', register, name='register_short'),
    path('profile/', profile, name='profile_short'),
]

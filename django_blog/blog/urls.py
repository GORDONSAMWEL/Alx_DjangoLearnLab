from django.urls import path
from blog.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, UserLoginView, UserLogoutView, home, register, profile

app_name = 'blog'  # Set the app name

urlpatterns = [
    path('', home, name='home'),
    path('login/', UserLoginView.as_view(), name='login_short'),
    path('logout/', UserLogoutView.as_view(), name='logout_short'),
    path('register/', register, name='register_short'),
    path('profile/', profile, name='profile_short'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

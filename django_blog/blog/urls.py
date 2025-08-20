from django.urls import path
from blog.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, UserLoginView, UserLogoutView, home, register, profile

app_name = 'blog'  # Set the app name

urlpatterns = [
    path('', home, name='home'),
    path('login/', UserLoginView.as_view(), name='login_short'),
    path('logout/', UserLogoutView.as_view(), name='logout_short'),
    path('register/', register, name='register_short'),
    path('profile/', profile, name='profile_short'),

    path('posts/', PostListView.as_view(), name='post-list'),              # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),      # Create a new post
    path('post/<int:pk>/update/', PostDetailView.as_view(), name='post-detail'), # View single post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete post
]

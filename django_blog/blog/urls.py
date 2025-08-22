from django.urls import path
from blog.views import (
    CommentDeleteView, CommentUpdateView, PostCreateView, PostDeleteView,
    PostDetailView, PostListView, PostSearchView, PostUpdateView, TaggedPostListView, UserLoginView, UserLogoutView,
    add_comment, home, register, profile
)

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('login/', UserLoginView.as_view(), name='login_short'),
    path('logout/', UserLogoutView.as_view(), name='logout_short'),
    path('register/', register, name='register_short'),
    path('profile/', profile, name='profile_short'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', add_comment, name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', TaggedPostListView.as_view(), name='tagged-posts'),
]

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, UserUpdateForm
from .models import Profile
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'blog/home.html')


class UserLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True  # optional: auto-redirect if already logged in
    next_page = reverse_lazy('home')

class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'  # optional

def register(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('profile_short')

    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('profile_short')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile_short')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {'u_form': u_form, 'p_form': p_form})



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

# Show details of a post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile




# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # required: use this exact method
    return render(request, "relationship_app/list_books.html", {'books': books})


# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # required
    context_object_name = "library"  # required





def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Adjust as needed
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")



def role_check(role):
    def check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(check)


@user_passes_test(is_admin)
@role_check('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
@role_check('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
@role_check('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

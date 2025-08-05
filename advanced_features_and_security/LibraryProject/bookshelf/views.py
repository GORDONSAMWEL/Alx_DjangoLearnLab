from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm



# Permissions enforced using @permission_required
# Ensure that only users in the correct group (Editors, Viewers, Admins)
# can access these views based on their permissions.


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        Book.objects.create(title=title, author_id=author_id)
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')



# Example view using the form
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # adjust this to your view name
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

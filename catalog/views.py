from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    word = 'personal'
    num_books_with_word = Book.objects.filter(title__contains = word).count()
    num_genres_with_word = Genre.objects.filter(name__contains = word).count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'word': word,
        'num_books_with_word': num_books_with_word,
        'num_genres_with_word': num_genres_with_word
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# "generic, class-based views" - seems to be django-speak for "resources" in rails - views based on a model
from django.views import generic
class BookListView(generic.ListView):
    model = Book

    # pagination is built in 
    # creates `is_paginated` method and and `page_obj` methods for use in templates
    paginate_by = 10

    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    # You can also override class methods such as `get_queryset(self):`to control what is returned
    # Overriding get_context_data() allows you to pass custom variables to the template


    # this class replaces the following function-based view
    # def book_detail_view(request, primary_key):
    #     try:
    #         book = Book.objects.get(pk=primary_key)
    #     except Book.DoesNotExist:
    #         raise Http404('Book does not exist')
    #     (THE ABOVE CAN BE WRITTEN AS:) book = get_object_or_404(Book, pk=primary_key)

    #     return render(request, 'catalog/book_detail.html', context={'book': book})


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllLoanedBooks(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing all borrowed books, only meant for librarians """    
    model = BookInstance
    template_name = 'catalog/all_borrowed.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

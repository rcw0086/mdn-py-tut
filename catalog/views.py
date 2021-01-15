from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

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
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'word': word,
        'num_books_with_word': num_books_with_word,
        'num_genres_with_word': num_genres_with_word
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

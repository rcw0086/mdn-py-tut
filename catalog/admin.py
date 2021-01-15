from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# the @register decorator is equal to: `admin.site.register(Author, AuthorAdmin`
# list_display = (...) lists what fields to display
# list_filter = (...) gives you a handy filtering panel on the screen, pre-populated with useful filters
# fieldsets = (...) allows you to split attributes for a model into different sections on the screen, with section headings
# fields = [] string-names of fields to show. To group inline, use a tuple ('', '')
# exclude = [] string names of fields to exclude
# inlines = [] class names of objects to include inline

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
  model = Book
  extra = 0

# Define the Admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
  # exclude = ['first_name']
  inlines = [BookInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('book', 'status', 'due_back', 'id')
  list_filter = ('status', 'due_back')

  fieldsets = (
      (None, {
          'fields': ('book', 'imprint', 'id')
      }),
      ('Availability', {
          'fields': ('status', 'due_back')
      }),
  )

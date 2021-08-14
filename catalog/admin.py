from django.contrib import admin
from .models import Book, BookInstance, Author, Genre



class AuthorBooks(admin.TabularInline):
	model = Book

#@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display =('full_name', 'date_of_birth', 'date_of_death')
	fields = ('first_name', 'last_name',( 'date_of_birth', 'date_of_death'))
	inlines =[AuthorBooks]
	
class BookInstanceInlines(admin.TabularInline):
	model = BookInstance

class BookAdmin(admin.ModelAdmin):
	list_display=('title', 'isbn', 'author', 'display_genre')
	inlines= [BookInstanceInlines]
	

class BookInstanceAdmin(admin.ModelAdmin):
	list_display=('book','status', 'borrower', 'due_back', 'id')
	list_filter=('status','due_back')
	fieldsets = (
		(None,{'fields':('book','imprint','id')}),
		("Availability",{'fields':('status','borrower','due_back')}),)



# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)


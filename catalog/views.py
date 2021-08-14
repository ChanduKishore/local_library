from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.

def index(request):
	num_books = Book.objects.all().count()
	num_authors = Author.objects.all().count()
	num_books_avaliable = BookInstance.objects.filter(status__exact='a').count()
	num_book_instance = BookInstance.objects.all().count()
	genre = Genre.objects.all()
	books_genre=[gen.name for gen in genre]
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1 

	context ={"book_count":num_books,
			"book_instance_count":num_book_instance,
			"avaliable_books":num_books_avaliable,
			"authors_count":num_authors,
			'genre':books_genre,
			"num_visits":num_visits}

	return render(request, "index.html",context=context)


class BookListView(generic.ListView):
	model = Book

class BookDetailView(generic.DetailView):
	model = Book
class AuthorListView(generic.ListView):
	model=Author

class AuthorDetailView(generic.DetailView):
	model=Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
	model= BookInstance
	template_name = 'bookinstance_borrowed_by_user.html'
	paginate_by=10

	def get_queryset(self):
		return BookInstance.objects.filter(borrower =self.request.user).filter(status__exact='o').order_by('due_back')



class LoanedBooksByAllUsersListView(LoginRequiredMixin,PermissionRequiredMixin, generic.ListView):
	model= BookInstance
	template_name = 'bookinstance_borrowed_by_all_user.html'
	paginate_by=10
	permission_required = 'catalog.can_mark_returned'

	def get_queryset(self):
		return BookInstance.objects.filter(status__exact='o').order_by('due_back')

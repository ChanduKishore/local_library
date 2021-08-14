from django.urls import path
from . import views

urlpatterns=[

path('',views.index, name="index"),
path('books/', views.BookListView.as_view(template_name='book_list.html'), name='books'),
path('books/<int:pk>/', views.BookDetailView.as_view(template_name='book_details.html'), name='book_details'),
path('authors/',views.AuthorListView.as_view(template_name='author_list.html'), name='authors'),
path('authors/<int:pk>/', views.AuthorDetailView.as_view(template_name='author_details.html'), name='author_details'),
path('mybooks/',views.LoanedBooksByUserListView.as_view(),name='my_books'),
path('allborrows/',views.LoanedBooksByAllUsersListView.as_view(),name='all_books'),

]
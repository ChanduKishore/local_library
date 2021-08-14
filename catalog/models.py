from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

class Genre(models.Model):
	'''this model represent book genre'''
	name= models.CharField(max_length=50, help_text="enter a Genre (ex:science fiction)")

	def __str__(self):
		"""String for representing the Model object."""
		return self.name




class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete= models.SET_NULL,null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions =(('can_mark_returned','set book as returned'),)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'

    def status_display(self):

        return [self.LOAN_STATUS[i][1] for i in range(len(self.LOAN_STATUS)) if self.status == self.LOAN_STATUS[i][0] ][0]

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

        
class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author_details', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.full_name()

    def full_name(self):
        return self.first_name+' '+self.last_name

class Book(models.Model):
    '''this models represents a book and storesa all the detials of the book except for he instance of book for loan'''
    title = models.CharField(max_length=50, help_text="enter name of the book (eg: pristage)")
    isbn =models.CharField('ISBN',max_length=13, unique=True,
                                         help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary =models.TextField(max_length=1000, help_text='enter a breif summary of the book')

    genre= models.ManyToManyField(Genre, help_text='select genre of the book')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_details', args=[str(self.id)])
     
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description="genre"



from django.shortcuts import render
from .models import Book, Author, BookCategory, Review

def index(request):
    # Get all books
    books = Book.objects.all()

    # Get all book categories
    book_categories = BookCategory.objects.all()

    # Render the homepage template
    context = {
        'books': books,
        'book_categories': book_categories,
    }
    return render(request, 'books/index.html', context)


def book_detail(request, book_id):
    # Get the book with the specified ID
    book = Book.objects.get(pk=book_id)

    # Get all reviews for the book
    reviews = Review.objects.filter(book=book)

    # Render the book detail template
    context = {
        'book': book,
        'reviews': reviews,
    }
    return render(request, 'books/book_detail.html', context)


def add_book(request):
    if request.method == 'POST':
        # Get form data
        book_name = request.POST['book_name']
        book_description = request.POST['book_description']
        book_isbn = request.POST['book_isbn']
        book_price = request.POST['book_price']
        book_image = request.FILES['book_image']
        book_category_id = request.POST['book_category']
        author_id = request.POST['author']

        # Create a new book object
        book = Book.objects.create(
            name=book_name,
            description=book_description,
            ISBN=book_isbn,
            price=book_price,
            image=book_image,
            book_category_id=book_category_id,
            author_id=author_id,
        )

        # Save the book object
        book.save()

        # Redirect to the homepage
        return redirect('index')

    else:
        # Get all book categories
        book_categories = BookCategory.objects.all()

        # Get all authors
        authors = Author.objects.all()

        # Render the add book template
        context = {
            'book_categories': book_categories,
            'authors': authors,
        }
        return render(request, 'books/add_book.html', context)


def edit_book(request, book_id):
    if request.method == 'POST':
        # Get form data
        book_name = request.POST['book_name']
        book_description = request.POST['book_description']
        book_isbn = request.POST['book_isbn']
        book_price = request.POST['book_price']
        book_image = request.FILES.get('book_image')
        book_category_id = request.POST['book_category']
        author_id = request.POST['author']

        # Get the book with the specified ID
        book = Book.objects.get(pk=book_id)

        # Update the book object
        book.name = book_name
        book.description = book_description
        book.ISBN = book_isbn
        book.price = book_price
        if book_image:
            book.image = book_image
        book.book_category_id = book_category_id
        book.author_id = author_id

        # Save the book object
        book.save()

        # Redirect to the book detail page
        return redirect('book_detail', book_id=book.id)

    else:
        # Get the book with the specified ID
        book = Book.objects.get(pk=book_id)

        # Get all book categories
        book_categories = BookCategory.objects.all()

        # Get all authors
        authors = Author.objects.all()

        # Render the edit book template
        context = {
            'book': book,
            'book_categories': book_categories,
            'authors': authors,
        }
        return render(request, 'books/edit_book.html', context)


def delete_book(request, book_id):
    # Get the book with the specified ID
    book = Book.objects.get(pk=book_id)

    # Delete the book object
    book.delete()

    # Redirect to the homepage or any other appropriate page
    return redirect('index')


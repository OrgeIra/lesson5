from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

class BookCategory(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ISBN = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images', blank=True)
    book_category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    year = models.IntegerField()
    review = models.TextField()
    star_given = models.IntegerField()

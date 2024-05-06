"""
URL configuration for app5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .other_urls import (
    index,
    books,
    book_detail,
    add_book,
    edit_book,
    delete_book,
    authors,
    author_detail,
    add_author,
    edit_author,
    delete_author,
    categories,
    category_detail,
    add_category,
    edit_category,
    delete_category,
    reviews,
    review_detail,
    add_review,
    edit_review,
    delete_review,
)

urlpatterns = [
    path('', index, name='index'),

    # Book URLs
    path('books/', books, name='books'),
    path('book/<int:book_id>', book_detail, name='book_detail'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>', delete_book, name='delete_book'),

    # Author URLs
    path('authors/', authors, name='authors'),
    path('author/<int:author_id>', author_detail, name='author_detail'),
    path('add_author/', add_author, name='add_author'),
    path('edit_author/<int:author_id>', edit_author, name='edit_author'),
    path('delete_author/<int:author_id>', delete_author, name='delete_author'),

    # Category URLs
    path('categories/', categories, name='categories'),
    path('category/<int:category_id>', category_detail, name='category_detail'),
    path('add_category/', add_category, name='add_category'),
    path('edit_category/<int:category_id>', edit_category, name='edit_category'),
    path('delete_category/<int:category_id>', delete_category, name='delete_category'),

    # Review URLs
    path('reviews/', reviews, name='reviews'),
    path('review/<int:review_id>', review_detail, name='review_detail'),
    path('add_review/', add_review, name='add_review'),
    path('edit_review/<int:review_id>', edit_review, name='edit_review'),
    path('delete_review/<int:review_id>', delete_review, name='delete_review'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
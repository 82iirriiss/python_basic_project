from django.contrib import admin

# Register your models here.
from django.contrib import admin
from books.models import Book, Author, Publisher

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
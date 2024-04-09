from django.contrib import admin

from django.contrib import admin
from .models import Author, Entry, AuthorProfile, Tag

admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(AuthorProfile)
admin.site.register(Tag)

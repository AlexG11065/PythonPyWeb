import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train.models import Blog, Author, AuthorProfile, Entry, Tag

    max_age = Author.objects.aggregate(max_age=Max('age'))
    print(Author.objects.filter(age=max_age['max_age']))  # TODO Какой автор имеет наибольший возраст?














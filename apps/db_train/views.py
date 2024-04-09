from django.db.models import Max, Q
from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag


class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])  # Какие авторы имеют самую высокую уровень самооценки(self_esteem)?


        self.answer2 = None  # TODO Какой автор имеет наибольшее количество опубликованных статей?


        self.answer3 =  Entry.objects.filter(Q(tags__name='Кино') |Q (tags__name='Музыка'))
        #  Какие статьи содержат тег 'Кино' или 'Музыка' ?


        self.answer4 = Author.objects.filter(gender__contains='ж').count()  # Сколько авторов женского пола зарегистрировано в системе?


        self.answer5 = None  # TODO Какой процент авторов согласился с правилами при регистрации?


        self.answer6 = AuthorProfile.objects.filter(stage__gte=1).filter(stage__lte=5)
        # Какие авторы имеют стаж от 1 до 5 лет?

        max_age = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = Author.objects.filter(age=max_age['max_age'])#.values_list('last_name', 'first_name', flat=True)  # TODO Какой автор имеет наибольший возраст?



        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()  # Сколько авторов указали свой номер телефона?

        self.answer9 = Author.objects.filter(age__lte=25)  # Какие авторы имеют возраст младше 25 лет?


        self.answer10 = None  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)



# from django.db.models import Count
#
# # Группировка категорий и подсчёт количества книг в них
# category_book_counts = Category.objects.annotate(book_count=Count('books'))
#
# # Вывод результатов
# for category in category_book_counts:
#     print(f"{category.name}: {category.book_count} книг(и)")
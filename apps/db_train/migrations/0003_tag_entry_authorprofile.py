# Generated by Django 4.2.5 on 2024-04-04 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0002_alter_author_options_alter_author_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='db_train.author')),
                ('tags', models.ManyToManyField(related_name='entries', to='db_train.tag')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, default=0, help_text='Стаж в годах', verbose_name='Стаж')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='db_train.author')),
            ],
            options={
                'verbose_name': 'Профиль Автора',
                'verbose_name_plural': 'Профили авторов',
            },
        ),
    ]

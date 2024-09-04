# Generated by Django 5.1 on 2024-09-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('author', models.CharField(max_length=64, verbose_name='Автор')),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Книга',
                'ordering': ['pub_date'],
                'indexes': [models.Index(fields=['pub_date'], name='books_book_pub_dat_4bd024_idx')],
            },
        ),
    ]

# Generated by Django 4.2 on 2023-04-04 07:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_publication', models.DateTimeField(verbose_name='Дата публикации')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('training_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('summary_training', models.CharField(max_length=255, verbose_name='Краткое содержание')),
                ('full_training', models.TextField(blank=True, verbose_name='Полный текст')),
                ('links_training', models.URLField(blank=True, verbose_name='Ссылка на обучающие ресурсы')),
                ('video_training', models.FileField(blank=True, upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Видео')),
                ('graphic_illustrations', models.ImageField(blank=True, null=True, upload_to='media/illustrations/', verbose_name='Иллюстрация')),
            ],
            options={
                'verbose_name': 'Обучение',
                'verbose_name_plural': 'Обучения',
            },
        ),
    ]

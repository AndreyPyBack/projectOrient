from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')

    def __str__(self):
        return self.name
class Event(models.Model):
    date_event = models.DateTimeField('Дата проведения')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',blank=True,null=True)
    slug = models.SlugField(max_length=100, unique=True,null=True)
    title_event = models.CharField('Заголовок события',max_length=255)
    place_realization = models.CharField('Место проведения',max_length=255,blank=True)
    illustration_event = models.ImageField('Иллюстрация',upload_to='media/event/')
    brief_announcement = models.CharField('Краткое объявление',max_length=255)
    link_to_position = models.URLField('Ссылка на положение',blank=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title_event

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_event)
        super(Event, self).save(*args, **kwargs)


class Comments(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,verbose_name='Событие',blank=True,null=True,related_name='comments_event')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор комментария',blank=True,null=True)
    create_data = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name="Видимость статьи", default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class LinkEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='link_event')
    title = models.CharField('Событие',max_length=200)
    url = models.URLField()

    class Meta:
        verbose_name = 'Ccылка'
        verbose_name_plural = 'Ссылки'
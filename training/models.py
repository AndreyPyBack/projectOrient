from django.db import models

# Create your models here.
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class Training(models.Model):
    date_of_publication = models.DateTimeField('Дата публикации')
    slug = models.SlugField(max_length=100, unique=True, null=True)
    category = models.CharField('Категория',max_length=100)
    training_title = models.CharField('Заголовок',max_length=255)
    summary_training = models.CharField('Краткое содержание',max_length=255)
    full_training = models.TextField('Полный текст',blank=True)
    links_training = models.URLField('Ссылка на обучающие ресурсы',blank=True)
    video_training = models.FileField(
        'Видео',
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        blank=True,
    )
    graphic_illustrations = models.ImageField('Иллюстрация',upload_to='media/illustrations/',blank=True,null=True)

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучения'

    def __str__(self):
        return self.training_title
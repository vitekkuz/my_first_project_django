from django.db import models


# Create your models here
class Category(models.Model):
    '''' Категория услуг '''
    name = models.CharField('Название категории', max_length=200)
    slug = models.SlugField('URL', max_length=120)
    text = models.TextField('Текст')
    # для баннера параметры прописанны необязательные
    banner = models.ImageField('Баннер', upload_to='imeges/', blank=True, null=True)
    title = models.CharField('Title', max_length=120)
    descripton = models.CharField('Description', max_length=250)
    keywords = models.CharField('Keywords', max_length=250)

    def __str__(self):
        return self.name

    # прописываем, как будет отоборажаться название модели в админке
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Model(models.Model):
    '''' Модель из категории '''
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 verbose_name='Выбор категории')
    name = models.CharField('Название услуги', max_length=120)
    slug = models.SlugField('URL', max_length=120, unique=True)
    text = models.TextField('Текст', default='')
    header = models.CharField('Заголовок', max_length=240, blank=True, null=True)
    sub_header = models.CharField('Подзаголовок', max_length=240, blank=True, null=True)
    images = models.ImageField('Картинка техники', upload_to='images/', blank=True, null=True)
    active = models.BooleanField('Опубликовать', default=True)
    banner = models.ImageField('Баннер', upload_to='images/', blank=True, null=True)
    title = models.CharField('Title', max_length=120)
    descripton = models.CharField('Description', max_length=250)
    keywords = models.CharField('Keywords', max_length=250)
    sort = models.PositiveIntegerField('Порядок', default=0, unique=True)

    def __str__(self):
        return self.name

    # прописываем, как будет отоборажаться название модели в админке
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

from django.db import models


# Create your models here
class category(models.Model):
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

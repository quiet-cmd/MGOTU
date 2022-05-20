from django.db import models

from ckeditor.fields import RichTextField


class Services(models.Model):
    """Список медицинских услуг и их цена"""
    name = models.CharField(max_length=255, verbose_name='Название услуги')
    code = models.CharField(max_length=255, verbose_name='Код услуги')
    price = models.IntegerField(verbose_name='Стоимость услуги')
    cat = models.ForeignKey('CategoryServices', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Список услуг'
        ordering = ['cat', 'code']


class CategoryServices(models.Model):
    """Категории медицинских услуг"""
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категорий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'Категории услуг'


class ClinicDocuments(models.Model):
    """Награды, сертификаты клиники"""
    name = models.CharField(max_length=255, verbose_name='Название награды')
    photo = models.ImageField(upload_to='photos/ClinicDocuments', verbose_name='Фотография')
    cat = models.ForeignKey('CategoryClinicDocuments', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы поликлиники'


class CategoryClinicDocuments(models.Model):
    """Категории документов клиники (сертификаты, награды)"""
    name = models.CharField(max_length=255, db_index=True, verbose_name='Тип документа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'Категории документов'


def doctors_default():
    text = """
    <h3> Образование</h3>
    <ul>
    <li> текст </li>
    <li> текст </li>
    <li> текст </li>
    </ul>
    
    <h3> Опыт работы </h3>
    <ul>
    <li> текст </li>
    <li> текст </li>
    <li> текст </li>
    </ul>
    """
    return text


class Doctors(models.Model):
    """Информация о врачах поликлиники"""
    name = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(upload_to='photos/Doctors', verbose_name='Фотография врача')
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    experience = RichTextField(default=doctors_default, verbose_name='опыт работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['-name', 'experience']


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    text = models.TextField(null=True, blank=True, verbose_name='Текст статьи')
    cat = models.ForeignKey('CategoryArticle', on_delete=models.PROTECT, verbose_name='Категория статьи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class CategoryArticle(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категории статей'

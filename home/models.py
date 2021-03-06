from django.db import models
from datetime import date
from django.urls import reverse


class ProductType(models.Model):  # Category
    """Тип продукта"""
    name = models.CharField("Тип продукта", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"


class Category(models.Model):  # Genre
    """Категории"""
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория продукта"
        verbose_name_plural = "Категории продуктов"


class Firm(models.Model):  # Actor
    """Фирма"""
    name = models.CharField("Название фирмы", max_length=100)
    # age
    description = models.TextField("Описание")
    # image

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фирма"
        verbose_name_plural = "Фирмы"


class Product(models.Model):  # Movie
    """Продукт"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    cover_photo = models.ImageField("Обложка", upload_to="products/", blank=True)  # poster  # blank=True - сделать необязательное заполнение
    # year = models.PositiveSmallIntegerField("Дата выхода", default=2020)
    country = models.CharField("Страна", max_length=30)
    firms = models.ManyToManyField(Firm, verbose_name="Фирма", related_name="product_firm")  # directors, related_name="film_director"
    # actors
    categories = models.ManyToManyField(Category, verbose_name="Категория")  # genres
    year = models.DateField("Год выпуска", default=date.today)  # world_premiere
    price = models.PositiveIntegerField("Цена", default=0, help_text="в рублях")  # budget
    # fees_in_usa
    # fees_in_world
    producttypes = models.ForeignKey(ProductType, verbose_name="Тип продукта", on_delete=models.SET_NULL, null=True)  # category
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик?", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Правильные url к продукту
        return reverse("product_detail", kwargs={"slug": self.url})  # 1 аргумент - имя url, 2 - в словаре передать параметры, которые мы передаём в url

    def get_comment(self):  # Вывести только родительские комменты
        return self.comment_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Photo(models.Model):  # MovieShots
    """Фирма"""
    title = models.CharField("Название", max_length=100)
    description = models.CharField("Описание", max_length=300)
    image = models.ImageField("Изображение", upload_to="photo/")
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)  # movie

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фотографии товаров"


# class RatingStar(models.Model):


# class Rating(models.Model):


class Comment(models.Model):  # Reviews
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Комментарий", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)  # 'self' - запись будет ссылкаться на запись в этой же таблице
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

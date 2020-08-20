from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):  # CategoryAdmin
    """Типы продуктов"""
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name",)  # Поле, которое будет ссылкой


class CommentInline(admin.TabularInline):
    """На странице товара показывать комментарии"""
    model = Comment
    extra = 0
    readonly_fields = ("name", "email")


class PhotoInline(admin.TabularInline):  # MovieShotsInline
    model = Photo
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="120"')

    get_image.short_description = "Изображение"


# class MovieAdminForm(forms.ModelForm):
#     """Форма с виджетом ckeditor"""
#     description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
#     description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Movie
#         fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # MoviesAdmin
    """Продукты"""
    list_display = ("title", "producttypes", "url", "draft")
    list_filter = ("producttypes",)  # Фильтры
    search_fields = ("title", "producttypes__name")  # Поиск
    inlines = [PhotoInline, CommentInline]  # Встроенные классы
    save_on_top = True  # Кнопки "удалить" и "сохранить" наверх
    save_as = True  # Добавить кнопку "сохранить как новый объект"
    list_editable = ("draft",)  # Редактировать "черновик" прям в списке продуктов
    actions = ["publish", "unpublish"]  # Регистрация экшенов
    readonly_fields = ("get_image",)  # Показать фото
#     fields = (("firms", "categories"),)  # Покажет только firms и categories в строку
    fieldsets = (
        (None, {
            "fields": ("title",)
        }),
        (None, {
            "fields": (("price", "producttypes"),)
        }),
        # ("Категории", {
        #     "classes": ("collapse",),
        #     "fields": (("firms", "categories"),)
        # }),
        (None, {
                "fields": (("firms", "categories"),)
            }),
        (None, {
            "fields": ("description",)
        }),
        (None, {
            "fields": (("country", "year",),)
        }),
        (None, {
            "fields": (("cover_photo", "get_image"),)
        }),
        ("Настройки", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):  # Показать фото
        return mark_safe(f'<img src={obj.cover_photo.url} height="110"')

    def unpublish(self, request, queryset):
        """Экшн - снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Экшн - опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"  # Экшн - опубликовать
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"  # Экшн - снять с публикации
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Обложка"  # Показать фото


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):  #RewiesAdmin
    """Комментарии"""
    list_display = ("name", "email", "parent", "product", "id")
    readonly_fields = ("name", "email")  # Скрыть от редактирования


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # GenreAdmin
    """Жанры"""
    list_display = ("name", "url")


@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):  # ActorAdmin
    """Актеры"""
    list_display = ("name", "description")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):  # MovieShotsAdmin
    """Фотографии к товарам"""
    list_display = ("title", "product", "get_image")
    readonly_fields = ("get_image",)
    list_filter = ("product",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="120"')

    get_image.short_description = "Изображение"


admin.site.site_title = "Администрирование"  # Название на начальной странице
admin.site.site_header = "Администрирование"  # Название в обложке

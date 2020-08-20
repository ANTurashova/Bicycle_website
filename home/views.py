from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу
# from django.http import HttpResponse  # Чтобы выводить строку с текстом
# def home(request):
#     return HttpResponse("<h4>X</h4>")
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import *
from .forms import *


# def home(request):
#     return render(request, 'home/home.html')


# class ProductView(View):
#     """Список велосипедов"""
#     def get(self, request):
#         products = Product.objects.all()
#         return render(request, "home/product_list.html", {"product_list": products})
class ProductView(ListView):
    """Список велосипедов"""
    model = Product
    queryset = Product.objects.filter(draft=False)  # filter, чтобы не выводились черновики
    template_name = "home/product_list.html"  # Не обязательно указывать

    def get_context_data(self, *args, **kwargs):  # Чтобы в категориях в "все" выводить категории
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


# class ProductDetailView(View):
#     """Страница с описанием продукта"""
#     def get(self, request, slug):
#         product = Product.objects.get(url=slug)
#         return render(request, "home/product_detail.html", {"product": product})
class ProductDetailView(DetailView):
    """Страница с описанием продукта"""
    model = Product
    slug_field = "url"
    template_name = "home/product_detail.html"


class AddComment(View):
    """Отправка отзывов"""
    def post(self, request, pk):
    #     print(request.POST)  # Весь запрос в консоль
        form = CommentForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            # pass
            form = form.save(commit=False)  # commit=False чтобы приостановить сохранение формы
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))

            form.product = product
            form.save()
        return redirect(product.get_absolute_url())

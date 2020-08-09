from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу
# from django.http import HttpResponse  # Чтобы выводить строку с текстом
# def home(request):
#     return HttpResponse("<h4>X</h4>")
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import *


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
    template_name = "home/product_list.html"


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

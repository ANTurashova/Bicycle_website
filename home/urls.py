from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.ProductView.as_view()),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail")
]

from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView,home, about_us, contact

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('', home, name='home'),
    path('aboutus/', about_us, name='about-us'),
    path('contact/', contact, name='contact'),
]

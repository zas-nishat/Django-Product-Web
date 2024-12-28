from django.views.generic import ListView, DetailView, CreateView
from .models import Product
from django.urls import reverse_lazy
from django.shortcuts import render


# ListView
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)  # Debugging: Check what's being fetched
        return queryset
 

# DetailView
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

# CreateView
class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'price', 'description']
    success_url = reverse_lazy('product-list')
    
#Home Page
def home(request):
    return render(request, 'homepage.html')
    
# About us page
def about_us(request):
    return render(request, 'aboutus.html')

#Contact Page
def contact(request):
    return render(request, 'contact.html')

from django.urls import path

from store.views import product_all, category_list, product_detail

app_name = 'store'

urlpatterns = [
    path('', product_all, name='product_all'),
    path('item/<slug:slug>/', product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', category_list, name='category_list'),
]

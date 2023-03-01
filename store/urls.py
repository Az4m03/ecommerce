from django.urls import path
from store.views import all_products

urlpatterns = [
    path('', all_products, name='all_products'),
]

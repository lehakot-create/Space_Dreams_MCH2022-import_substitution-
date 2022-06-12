from django.urls import path
from .views import *


urlpatterns = [
    path('regions/', api_region_list),
    path('region/<str:region>/', api_region_detail),

    path('locality/', api_locality_list),
    path('locality/<str:locality>/', api_locality_detail),

    path('inn/<int:inn>/', api_inn_detail),

    path('categories/', api_categories_list),
    path('category/<str:category>/', api_categories_detail),

    path('products/', api_products_list),
    path('product/<str:product>/', api_products_detail),
]

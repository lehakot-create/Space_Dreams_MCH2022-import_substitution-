from django.http import JsonResponse

from .models import Company
from .serializers import *
from .utils import remove_dublicate


def api_region_list(request):
    """
    Возвращает список регионов
    :param request:
    :return:
    """
    if request.method == 'GET':
        region = Company.objects.values('Region').distinct('Region')
        serializer = RegionSerializer(region, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_region_detail(request, **kwargs):
    """
    Возвращает все записи с заданным регионом
    :param request:
    :return:
    """
    if request.method == 'GET':
        companies = Company.objects.filter(Region=kwargs.get('region'))
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_locality_list(request):
    """
    Возвращает список всех городов
    :param request:
    :return:
    """
    if request.method == 'GET':
        locality = Company.objects.values('Locality').distinct('Locality')
        print(locality)
        serializer = LocalitySerializer(locality, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_locality_detail(request, **kwargs):
    """
    Возвращает все записи с заданным городом
    :param request:
    :param kwargs:
    :return:
    """
    if request.method == 'GET':
        companies = Company.objects.filter(Locality=kwargs.get('locality'))
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_inn_detail(request, **kwargs):
    if request.method == 'GET':
        companies = Company.objects.filter(INN=kwargs.get('inn'))
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_categories_list(request):
    """
    Возвращает список категорий
    :param request:
    :return:
    """
    if request.method == 'GET':
        categories_raw = Company.objects.values('Categories').distinct('Categories')
        categories = remove_dublicate('Categories', categories_raw)
        serializer = CategoriesSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_categories_detail(request, **kwargs):
    """
     Возвращает компании по заданной категории
    :param request:
    :param kwargs: название категории
    :return:
    """
    if request.method == 'GET':
        companies = Company.objects.filter(Categories__icontains=kwargs.get('category'))
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_products_list(request):
    """
    Возвращает список всех продуктов
    :param request:
    :return:
    """
    if request.method == 'GET':
        products_raw = Company.objects.values('Products').distinct('Products')
        products = remove_dublicate('Products', products_raw)
        serializer = ProductsSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_products_detail(request, **kwargs):
    """
    Возвращает все записи с заданным продуктом
    :param request:
    :param kwargs:
    :return:
    """
    if request.method == 'GET':
        companies = Company.objects.filter(Products__icontains=kwargs.get('product'))
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

from django.test import TestCase
from .models import Company

dct = {
    "id_company": "20800",
    "Company": "Экор-Фиш",
    "Direction": "Производство рыбного филе",
    "Description": "Производим рыбное филе, стейки, фасованную рыбу и морепродукты по ГОСТу, ТУ, СТО. Работаем с сегментом HoReCa, сетями, магазинами, оптовиками, производителями. Доставка от 1 упаковки по Москве и области. Оптовые цены при заказе от 500 кг в ассортименте.\nОсуществляем доставку в регионы. Производственные мощности - 20 тонн продукции в сутки. Предоставляем услуги переработки вашего сырья.",
    "Categories": [],
    "Products": [
        "Рыба мороженая",
        "Рыбное филе"
    ],
    "Status": "Действующая организация",
    "INN": "7722379983",
    "OGRN": "5167746256640",
    "KPP": "772201001",
    "Entity": "1998",
    "Employ_number": "200",
    "Region": "Московская область",
    "Locality": "д. Черное",
    "Address": "Московская обл., г Балашиха, д. Черное, ул Чернореченская 170Б",
    "Telephone": "+79167226980",
    "Post": "andreevdn@ekorfish.ru",
    "URL": "https://ekorfish.com/",
    "Catalogs": [
        "catalogs/Экор-Фиш_7722379983/Прайс производство Экор_16.02.2022.pdf"
    ]
}


def test(dct: dict = ''):
    dct = {
        "id_company": "20800",
        "Company": "Экор-Фиш",
        "Direction": "Производство рыбного филе",
        "Description": "Производим рыбное филе, стейки, фасованную рыбу и морепродукты по ГОСТу, ТУ, СТО. Работаем с сегментом HoReCa, сетями, магазинами, оптовиками, производителями. Доставка от 1 упаковки по Москве и области. Оптовые цены при заказе от 500 кг в ассортименте.\nОсуществляем доставку в регионы. Производственные мощности - 20 тонн продукции в сутки. Предоставляем услуги переработки вашего сырья.",
        "Categories": [],
        "Products": [
            "Рыба мороженая",
            "Рыбное филе"
        ],
        "Status": "Действующая организация",
        "INN": "7722379983",
        "OGRN": "5167746256640",
        "KPP": "772201001",
        "Entity": "1998",
        "Employ_number": "200",
        "Region": "Московская область",
        "Locality": "д. Черное",
        "Address": "Московская обл., г Балашиха, д. Черное, ул Чернореченская 170Б",
        "Telephone": "+79167226980",
        "Post": "andreevdn@ekorfish.ru",
        "URL": "https://ekorfish.com/",
        "Catalogs": [
            "catalogs/Экор-Фиш_7722379983/Прайс производство Экор_16.02.2022.pdf"
        ]
    }

    Company.objects.create(
        id_company=dct.get('id_company', None),
        Company=dct.get('Company', None),
        Direction=dct.get('Direction', None),
        Description=dct.get('Description', None),
        Categories=dct.get('Categories', None),
        Products=dct.get('Products', None),
        Status=dct.get('Status', None),
        INN=dct.get('INN', None),
        OGRN=dct.get('OGRN', None),
        KPP=dct.get('KPP', None),
        Entity=dct.get('Entity', None),
        Employ_number=dct.get('Employ_number', None),
        Region=dct.get('Region', None),
        Locality=dct.get('Locality', None),
        Address=dct.get('Address', None),
        Telephone=dct.get('Telephone', None),
        Post=dct.get('Post', None),
        URL=dct.get('URL', None),
        VK=dct.get('VK', None),
        Instagram=dct.get('Instagram', None),
        Facebook=dct.get('Facebook', None),
        Youtube=dct.get('Youtube', None),
        Catalogs=dct.get('Catalogs', None)
    )


# py manage.py shell
# from backend.tests import test



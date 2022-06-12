import os
import json

from backend.models import Company
from django.core.management.base import BaseCommand

from prj.settings import BASE_DIR
# from prj.prj.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Эта команда заполняет базу данных'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', type=str, help='Название файла')

    def handle(self, *args, **kwargs):
        with open(os.path.join(BASE_DIR, f'parser\{kwargs["filename"]}.json'), encoding="utf-8") as f:
            data = json.loads(f.read())
            for el in data:
                try:
                    Company.objects.create(
                        id_company=el.get('id_company', None),
                        Company=el.get('Company', None),
                        Direction=el.get('Direction', None),
                        Description=el.get('Description', None),
                        Categories=el.get('Categories', None),
                        Products=el.get('Products', None),
                        Status=el.get('Status', None),
                        INN=el.get('INN', None),
                        OGRN=el.get('OGRN', None),
                        KPP=el.get('KPP', None),
                        Entity=el.get('Entity', None),
                        Employ_number=el.get('Employ_number', None),
                        Region=el.get('Region', None),
                        Locality=el.get('Locality', None),
                        Address=el.get('Address', None),
                        Telephone=el.get('Telephone', None),
                        Post=el.get('Post', None),
                        URL=el.get('URL', None),
                        VK=el.get('VK', None),
                        Instagram=el.get('Instagram', None),
                        Facebook=el.get('Facebook', None),
                        Youtube=el.get('Youtube', None),
                        Catalogs=el.get('Catalogs', None)
                    )
                    print(f'Сделана запись: {el.get("id_company")}')
                except BaseException as e:
                    print(f'{el.get("id_company")} - error - {e}')
            self.stdout.write(self.style.SUCCESS('Данные успешно записаны в базу данных'))

        # dct = {
        #     "id_company": "20800",
        #     "Company": "Экор-Фиш",
        #     "Direction": "Производство рыбного филе",
        #     "Description": "Производим рыбное филе, стейки, фасованную рыбу и морепродукты по ГОСТу, ТУ, СТО. Работаем с сегментом HoReCa, сетями, магазинами, оптовиками, производителями. Доставка от 1 упаковки по Москве и области. Оптовые цены при заказе от 500 кг в ассортименте.\nОсуществляем доставку в регионы. Производственные мощности - 20 тонн продукции в сутки. Предоставляем услуги переработки вашего сырья.",
        #     "Categories": [],
        #     "Products": [
        #         "Рыба мороженая",
        #         "Рыбное филе"
        #     ],
        #     "Status": "Действующая организация",
        #     "INN": "7722379983",
        #     "OGRN": "5167746256640",
        #     "KPP": "772201001",
        #     "Entity": "1998",
        #     "Employ_number": "200",
        #     "Region": "Московская область",
        #     "Locality": "д. Черное",
        #     "Address": "Московская обл., г Балашиха, д. Черное, ул Чернореченская 170Б",
        #     "Telephone": "+79167226980",
        #     "Post": "andreevdn@ekorfish.ru",
        #     "URL": "https://ekorfish.com/",
        #     "Catalogs": [
        #         "catalogs/Экор-Фиш_7722379983/Прайс производство Экор_16.02.2022.pdf"
        #     ]
        # }

        # Company.objects.create(
        #     id_company=dct.get('id_company', None),
        #     Company=dct.get('Company', None),
        #     Direction=dct.get('Direction', None),
        #     Description=dct.get('Description', None),
        #     Categories=dct.get('Categories', None),
        #     Products=dct.get('Products', None),
        #     Status=dct.get('Status', None),
        #     INN=dct.get('INN', None),
        #     OGRN=dct.get('OGRN', None),
        #     KPP=dct.get('KPP', None),
        #     Entity=dct.get('Entity', None),
        #     Employ_number=dct.get('Employ_number', None),
        #     Region=dct.get('Region', None),
        #     Locality=dct.get('Locality', None),
        #     Address=dct.get('Address', None),
        #     Telephone=dct.get('Telephone', None),
        #     Post=dct.get('Post', None),
        #     URL=dct.get('URL', None),
        #     VK=dct.get('VK', None),
        #     Instagram=dct.get('Instagram', None),
        #     Facebook=dct.get('Facebook', None),
        #     Youtube=dct.get('Youtube', None),
        #     Catalogs=dct.get('Catalogs', None)
        # )


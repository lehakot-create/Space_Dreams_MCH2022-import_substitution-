import requests
from bs4 import BeautifulSoup
import json
import os

from prj.backend.models import Company

# from db import write_to_db


''' лучше сохранить дубль файла с 10-20 ссылками и вставить его сюда, чтобы каждый раз не ждать проход 2000 ссылок '''
with open('persons_url_list.txt', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0

    ''' !!! вставлена ссылка на все компании, если хочешь спарсить только одну -
    исправь например q = requests.get('https://xn--b1aedfedwrdfl5a6k.xn--p1ai/producer/end15') '''
    for line in lines:
        # q = requests.get(line)
        q = requests.get('https://xn--b1aedfedwrdfl5a6k.xn--p1ai/producer/rusprom')
        result = q.content

        soup = BeautifulSoup(result, 'lxml')

        ''' ID '''
        id_company = soup.find('div', class_='comp-card comp-card-top node-stat').get('rel').replace('node-', '')

        ''' Название, направление, описание '''
        person = soup.find(class_='manufacturers-card-info-col-1').find('h1').text.strip()
        direction = soup.find(class_='comp-card-info-txt').text.strip()
        description = soup.find(class_="abcomp-desc").text.strip()

        ''' Категория '''
        categories = soup.find_all(class_='category-bott-li')
        categories_item = []
        for item in categories:
            categories_item.append(item.text)

        ''' Продукция '''
        products = soup.find_all(class_='productis-nav-li')
        products_item = []
        for item in products:
            products_item.append(item.text)

        ''' Заполнение словаря компании '''
        data = {
            'id_company': id_company,
            'Company': person,
            'Direction': direction,
            'Description': description,
            'Categories': categories_item,
            'Products': products_item
        }

        ''' Реквизиты '''
        requisites = soup.find_all(class_='brequisits-row')
        for item in range(len(requisites)):
            requisites_key = requisites[item].find('div', class_="brequisits-col-1").text.replace(':', '')

            if requisites_key == 'Статус':
                key = 'Status'
            elif requisites_key == 'ИНН':
                key = 'INN'
            elif requisites_key == 'ОГРН':
                key = 'OGRN'
            elif requisites_key == 'КПП':
                key = 'KPP'
            elif requisites_key == 'Название юр лица':
                key = 'Entity'
            elif requisites_key == 'Кол-во сотрудников':
                key = 'Employ_number'
            else:
                pass

            val = requisites[item].find('div', class_="brequisits-col-2").text
            data[key] = val

        ''' Регион и город '''
        location = soup.find(class_='comp-card-info-a-geo').text.strip().split(',')
        for item in location:
            region = 'Region'
            locality = 'Locality'
            data[region] = location[0].strip()
            data[locality] = location[1].strip()

        ''' Контакты и соцсети '''
        contacts = soup.find_all(class_='bconts-row')
        for item in range(len(contacts)):
            try:
                contacts_key = contacts[item].find('div', class_="bconts-col-1").text.replace(':', '')
                if contacts_key == 'Адрес':
                    key = 'Address'
                elif contacts_key == 'Телефон':
                    key = 'Telephone'
                elif contacts_key == 'Почта':
                    key = 'Post'
                elif contacts_key == 'Сайт':
                    key = 'URL'
                elif contacts_key == 'Вконтакте':
                    key = 'VK'
                elif contacts_key == 'Инстаграм':
                    key = 'Instagram'
                elif contacts_key == 'Фейсбук':
                    key = 'Facebook'
                elif contacts_key == 'Ютуб':
                    key = 'Youtube'
                else:
                    pass
                val = contacts[item].find('div', class_="bconts-col-2").text.replace('\n', '')
                data[key] = val
            except:
                pass

        ''' Каталоги '''
        catalogs_item = []

        try:
            catalogs = soup.find('div', class_='abcomp-acts').find_all('a', class_="abcomp-act")
            if os.path.exists(f'catalogs/{person}_{data["INN"]}/'):
                pass
            else:
                os.mkdir(f'catalogs/{person}_{data["INN"]}/')

            for catalog in catalogs:
                download_catalog = catalog.get('href')
                catalog_bytes = requests.get(f'https://xn--b1aedfedwrdfl5a6k.xn--p1ai{download_catalog}').content
                filename = catalog.find(class_='abcomp-name').text

                if os.path.isfile(f'catalogs/{person}_{data["INN"]}/{filename}'):
                    catalogs_item.append(f'catalogs/{person}_{data["INN"]}/{filename}')
                    data['Catalogs'] = catalogs_item

                else:
                    with open(f'catalogs/{person}_{data["INN"]}/{filename}', 'wb') as file:
                        file.write(catalog_bytes)
                    catalogs_item.append(f'catalogs/{person}_{data["INN"]}/{filename}')
                    data['Catalogs'] = catalogs_item

        except:
            data['Catalogs'] = catalogs_item

        ''' счетчик в консоль '''
        count += 1
        print(f'#{count}: {line} is done')

        data_dict.append(data)

        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4, ensure_ascii=False)


    """
    Write to DB
    """
    for el in data_dict:
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


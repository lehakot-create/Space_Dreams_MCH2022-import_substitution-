### Парсер компаний МО из каталога производитель.рф



### Запускаем на локальной машине с помощью Докер
1. Клонируем репозиторий: git clone https://github.com/Space-dreams/parse_producersMO.git
2. Переходим в папку с файлом docker-compose.yml
3. Запускаем докер
4. Набираем в консоли:
   1. docker-compose up -d --build  - собрать и запустить два контейнера
   2. docker-compose exec web python manage.py makemigrations
   3. docker-compose exec web python manage.py migrate   - сделать миграции
   4. docker-compose exec web python manage.py fill_database -f data  - заполняет базу данных
   5. docker-compose exec web python manage.py fill_database -f data_moscow  - заполняет базу данных

    

### Работает на Heroku:
https://msh777.herokuapp.com/manufacturer_lk/1234567890/



### Описание API:
https://msh777.herokuapp.com/api/v1/regions/ - вернет список регионов

https://msh777.herokuapp.com/api/v1/region/Московская область/ - вернет все записи с регионом Московская область 


https://msh777.herokuapp.com/api/v1/locality/ - вернет список городов

https://msh777.herokuapp.com/api/v1/locality/д. Барабаново/ - вернет все записи с городом д. Барабаново 


https://msh777.herokuapp.com/api/v1/locality/5047112414/ - вернет все записи с ИНН 5047112414


https://msh777.herokuapp.com/api/v1/categories/ - вернет все категории (осторожно их очень много)

https://msh777.herokuapp.com/api/v1/category/Авиатранспорт моторный/ - вернет все записи которые относятся к категории Авиатранспорт моторный


https://msh777.herokuapp.com/api/v1/products/ - вернет все продукты

https://msh777.herokuapp.com/api/v1/product/Посуда пластиковая/ - вернет все записи которые содержат продукт Посуда пластиковая



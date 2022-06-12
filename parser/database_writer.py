# -*- coding: utf-8 -*-

import sqlite3
from typing import Dict


class Db:
    def __init__(self, db_name: str, table: str, column: Dict):
        """

        :param db_name: Имя базы данных
        :param table: Имя таблицы
        :param Типы столбцов. Например {'name': 'TEXT', 'Age': 'INT'}
        """
        self.db_name = db_name or 'temp.db'
        self.conn = sqlite3.connect(self.db_name)  # создание соединения
        self.cur = self.conn.cursor()  # для запросов
        self.table = table
        self.column = ', '.join(f'{key} {column[key]}' for key in column)
        self.mask = ', '.join('?' for _ in range(len(column)))
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}({self.column});")
        self.conn.commit()

    def write_one(self, value):
        """
        Делает одну запись в базу данных
        :param передаваемое значение: кортеж ('name': 'Bob')
        :return: ничего не возвращает
        """
        self.cur.execute(f"INSERT INTO {self.table} VALUES({self.mask});", value)
        self.conn.commit()

    def write_many(self, more_value):
        self.cur.executemany(f"INSERT INTO {self.table} VALUES({self.mask});", more_value)
        self.conn.commit()

    def fetch_several(self, count):
        self.cur.execute(f"SELECT * FROM {self.table};")
        return self.cur.fetchmany(count)

    def fetch_several_by_filter(self, column, where):
        """
        Возвращает несколько записей из таблицы table_name по фильтру "where"
        :param column: column_name
        :param where: значение которое ищем
        :return:
        """
        self.cur.execute(f'SELECT {column} FROM {self.table} WHERE {column} = {where}')
        return self.cur.fetchmany()

    def fetch_all(self):
        self.cur.execute(f"SELECT * FROM {self.table};")
        return self.cur.fetchall()

    def delete(self, column_name, value):
        self.cur.execute(f"DELETE FROM {self.table} WHERE {column_name}='{value}';")
        self.conn.commit()


def write_to_db(dct: dict):
    """
    Получаем список словарей и передаем в объект класса Db для записи
    :param dct:
    :return:
    """
    type_column = {
        "Company": "TEXT",
        "Direction": "TEXT",
        "Description": "TEXT",
        "Categories": "TEXT",
        "Products": "TEXT",
        "Статус": "TEXT",
        "ИНН": "INT",
        "ОГРН": "INT",
        "КПП": "INT",
        "Название юр лица": "TEXT",
        "Год основания": "INT",
        "Колво сотрудников": "INT",
        "Область": "TEXT",
        "Населенный пункт": "TEXT",
        "Адрес": "TEXT",
        "Телефон": "INT",
        "Почта": "TEXT",
        "Сайт": "TEXT",
        "Вконтакте": "TEXT",
        "Инстаграм": "TEXT",
    }
    db = Db(db_name='CompanyLst', table='companies', column=type_column)

    if dct.get('ИНН') != None:
        if db.fetch_several_by_filter(column='ИНН', where=dct.get('ИНН')):
            print(f'Company with ИНН {dct.get("ИНН")} already exists')
            return f'Company with ИНН {dct.get("ИНН")} already exists'

    lst = []
    for el in type_column:
        if el == 'Колво сотрудников':
            el = 'Кол-во сотрудников'
        try:
            lst.append(str(dct.get(el, None)))
        except Exception as e:
            print(f'{e}')

    db.write_one(tuple(lst))

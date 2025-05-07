import sqlite3
conn = sqlite3.connect('Control_panel/db.sqlite3')

# Создайте курсор
cursor = conn.cursor()

# Выполнение запроса для получения названий таблиц
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# # Получение всех результатов
# tables = cursor.fetchall()

# # Вывод всех имен таблиц
# for table in tables:
#     print(table[0])

# cursor.execute("select * from Block_panel_condition ")
# tables = cursor.fetchall()

# # Вывод всех имен таблиц
# for table in tables:
#     print(f"('{table[2]}','{table[1]}'),")

# conn.commit()
# print('complete)')

data = [
    ('1', 'Эксплуатация'),
    ('2', 'Перемещение комплектации на оборудование'),
    ('3', 'Ожидание крана'),
    ('4', 'Уборка комплектации с рабочего места'),
    ('5', 'Укладка комплектации'),
    ('6', 'Подрезка перемычек'),
    ('7', 'Ожидание подвоза комплектации'),
    ('8', 'Ожидание увоза комплектации'),
    ('9', 'Переходы за ручной плазмой'),
    ('10', 'Переход за краном'),
    ('11', 'Переход за необходимой комплектацией'),
    ('12', 'Отсутствие оператора'),
    ('13', 'Отсутствие расходников на оборудование'),
    ('14', 'Отсутствие или повреждение оснастки'),
    ('15', 'Отсутствие технологии изготовления, обработки'),
]

cursor.executemany("INSERT INTO Block_panel_condition (id_number, name) VALUES (?, ?)", data)

conn.commit()
import sqlite3
DBNAME = "db.sqlite3"

conn = sqlite3.Connection(DBNAME)
cur = conn.cursor()
query = ('''INSERT INTO "WebARM_machine" ("id", "name", "condition_id") 
VALUES 
('M001', 'Токарный станок ЧПУ', 0),
('M002', 'Фрезерный станок', 0),
('M003', 'Пресс гидравлический', 1),
('M004', 'Ленточная пила', 3),
('M005', 'Сварочный аппарат', 5);''')
cur.execute(query)
conn.commit()
# print(cur.fetchall())
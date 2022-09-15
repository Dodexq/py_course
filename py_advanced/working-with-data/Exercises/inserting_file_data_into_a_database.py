import sqlite3
import os

os.chdir(os.path.dirname(__file__))
connection = sqlite3.connect(':memory:')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

create = """CREATE TABLE states (
                'state' text,
                'pop2020' integer,
                'pop2000' integer
            )"""

cursor.execute(create)

insert = 'INSERT INTO states VALUES (?, ?, ?)'

insert_data = []
with open("../data/states.txt", "r") as f:
    for line in f.readlines():
        data = line.split("\t")
        return_data = (data[0], int(data[1].replace(",","")), \
            int(data[2].replace(",","")))
        insert_data.append(return_data)

cursor.executemany(insert, insert_data)

#     line = (i.split("\t") for i in f.read().splitlines())
# for insert_tuple in line:
#     cursor.execute(insert, insert_tuple)
    
select = """SELECT state,
            CAST((pop2020*1.0/pop2000) * pop2020 AS INTEGER) AS pop2040
            FROM states ORDER BY pop2040 DESC"""

cursor.execute(select)
results = cursor.fetchall()

for record in results:
    state = record['state']
    pop2040 = record['pop2040']
    print(f'The projected 2040 population of {state} is {pop2040:,}.')

cursor.close()
connection.close()
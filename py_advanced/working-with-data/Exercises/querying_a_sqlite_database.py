import sqlite3
import os

os.chdir(os.path.dirname(__file__))
connection = sqlite3.connect('../data/lahmansbaseballdb.sqlite')
connection.row_factory = sqlite3.Row

query = """SELECT nameFirst, nameLast, weight, 
                  debut AS debut
           FROM people
           ORDER BY weight DESC
           LIMIT 5"""

cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    player_name = result['nameFirst'] + ' ' + result['nameLast']
    weight = result['weight']
    year = result['debut'][:4]
    print(f'{player_name} weighed {weight} when he debuted in {year}.')

cursor.close()
connection.close()

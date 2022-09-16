import mysql.connector

connection = mysql.connector.connect(
    host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
    user='python',
    passwd='python',
    db='lahmansbaseballdb'
)

query = """SELECT nameFirst, nameLast, birthCity, birthState, birthYear
           FROM people
           WHERE birthYear=%s;"""

year = int(input("Birth Year: "))
cursor = connection.cursor(prepared=True)
cursor.execute(query, [year])

results = cursor.fetchall()

for i, result1 in enumerate(results, 1):
    row = dict(zip(cursor.column_names, result1))
    name = f"{row['nameFirst']} {row['nameLast']}"
    print(f"{i}. {name}: birn in {row['birthCity']} city")

cursor.close()
connection.close()
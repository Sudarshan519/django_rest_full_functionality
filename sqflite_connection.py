import sqlite3

connection = sqlite3.connect("db.sqlite3")
print(connection.total_changes)
cursor = connection.cursor()
rows=cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
# print(rows)

all_data=[]
for d in rows:
    table=d[2]
    q="SELECT * FROM " +table
    data=cursor.execute(q).fetchall()
    print(data)
    all_data.append([d[2],data])
    print(d[2])

with open("postal_code.txt", "w") as file:
    for x in all_data:


        file.writelines((all_data))
file.close

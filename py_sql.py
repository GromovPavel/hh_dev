import postgresql


db = postgresql.open("pq://postgres:Qwerty123@localhost:5432/mydb")

t = db.query('SELECT * FROM t')

for i in t:
   print(i[1])
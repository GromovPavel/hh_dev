import postgresql


db = postgresql.open("pq://postgres:Qwerty123@localhost:5432/mydb")

db.execute("CREATE TABLE IF NOT EXIST offers_t (id SERIAL PRIMARY KEY,"
           "name VARCHAR, station VARCHAR, address VARCHAR, employer VARCHAR, requirement VARCHAR, alternate_url VARCHAR, open BOOLEAN, ")

t = db.query('SELECT * FROM t')

for i in t:
   print(i[0])
   
   
   
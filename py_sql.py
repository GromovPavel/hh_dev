import postgresql


db = postgresql.open("pq://postgres:Qwerty123@localhost:5432/mydb")

db.execute("CREATE TABLE IF NOT EXISTS offers_t (id SERIAL PRIMARY KEY,"
           "name VARCHAR, station VARCHAR, address VARCHAR, employer VARCHAR, requirement VARCHAR, alternate_url VARCHAR, degree BOOLEAN)")


insert = db.prepare('INSERT INTO offers_t (name, station, address, employer, requirement, alternate_url, degree) VALUES ($1, $2, $3, $4, $5, $6, $7)')


t = db.query('SELECT * FROM offers_t')


#for i in t:
#   print(i[0])
   
   
   
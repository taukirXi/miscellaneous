import psycopg2

con = psycopg2.connect(host='10.69.217.84',
                       user='postgres',
                       database='postgres',
                       password='Dbspostgres1',
                       port=5432)

cur = con.cursor()
try:
    cur.execute("select * from author")
    for row in cur:
except psycopg2.

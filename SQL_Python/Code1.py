import psycopg2

# Establish connection

conn = psycopg2.connect(dbname='db', user='sai')
cursor = conn.cursor()

cursor.execute('SELECT 2 + 3;')
records = cursor.fetchall()

print (records)
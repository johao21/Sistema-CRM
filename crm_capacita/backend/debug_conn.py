import psycopg2

conn = psycopg2.connect(
    dbname="crm_leads",
    user="postgres",
    password="123456",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())

conn.close()
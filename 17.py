from mysql import connector

conn = connector.connect(host='lokalhost', user='root', password='1234')
with conn.cursor() as cursor:
    cursor.execute("DROP DATABASE IF EXISTS traveles;")
    cursor.execute(" CRETE DATABASE traveles;")
 with conn.cursor() as cursor:
     cursor.execute("USE traveles;")
     cursor.execute("""
     GREAT TABLE travels""")













































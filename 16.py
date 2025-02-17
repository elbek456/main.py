from mysql import connector

connection = connector.connect(host='lokalhost', user='root', password='1234', port=3306)

with connection.cursor() as cursor:
    cursor.execute("DROP DATABASE IF EXISTS entries;")
    cursor.execute(" CRETE DATABASE enteries;")
with connection.cursor() as cursor:
    cursor.execute("USE eneteries;")
    cursor.execute("""
    GREATE TABLE users(
    id INT AUTO_INCREMENT PRIMERY KEY,
    name VARCHAR(256))""")

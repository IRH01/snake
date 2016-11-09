import mysql.connector

conn = mysql.connector.connect(host='192.168.105.66', port='3306', user='root', password='root', database='test',
                               use_unicode=True)

cursor = conn.cursor()

cursor.execute('select * from user2 where id = %s', ('1',))

values = cursor.fetchall()

print values

cursor.close()

conn.close()

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM emp"
cursor.execute(sql)

result = cursor.fetchall()

cursor.close()
conn.close()

for i in result:
    print(i)

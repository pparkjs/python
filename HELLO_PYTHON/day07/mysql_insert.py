import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = "insert into emp values(%s, %s, %s, %s)"
data = ('4','4','4','4')
cursor.execute(sql, data)

conn.commit()

cursor.close()
conn.close()
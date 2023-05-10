import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')

e_id = '5'
e_name = '5'
sex = '5'
addr = '5'

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = f"""
        insert into emp 
            values('{e_id}', '{e_name}', '{sex}', '{addr}')
       """
print('sql', sql)
cursor.execute(sql)
print('cnt',cursor.rowcount)

conn.commit()
conn.close()
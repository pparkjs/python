import pymysql

class DaoEmp:
    
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "SELECT * FROM emp"
        self.cursor.execute(sql)
        
        list = self.cursor.fetchall()
        return list
    
    def selectOne(self, e_id):
        sql = f"""
                SELECT 
                    e_id, e_name, sex, addr 
                  FROM emp 
                 where e_id = '{e_id}' 
            """
        self.cursor.execute(sql)
        
        obj = self.cursor.fetchall()
        return obj[0]
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"""
                insert into emp
                    values('{e_id}', '{e_name}', '{sex}', '{addr}')
            """
        self.cursor.execute(sql)
        cnt = self.cursor.rowcount
        self.conn.commit()
        return cnt
    
    def update(self, e_id, e_name, sex, addr): 
        sql = f"""
                update emp  
                    set addr = '{addr}'
                where e_id = '{e_id}'
               """
       
        self.cursor.execute(sql)
        cnt = self.cursor.rowcount
        self.conn.commit()
        return cnt
    
    def delete(self, e_id):
        sql = f"""
                delete from emp  
                  where e_id = '{e_id}'
               """
        self.cursor.execute(sql)
        cnt = self.cursor.rowcount
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        

    
if __name__ == '__main__':
    de = DaoEmp()
    # obj = de.selectOne("1")
    # cnt = de.insert('6','6','6','6')
    # ucnt = de.update('1', '0', '0', '0')
    dcnt = de.delete('1')
    # print('obj',obj)
    # print('cnt',cnt)
    # print('ucnt',ucnt)
    print('dcnt',dcnt)
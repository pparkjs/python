import pymysql


class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect( host='127.0.0.1', port=3305, 
                                     user='root', db='python', 
                                     password='python',charset='utf8' )
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):    
        sql = "select * from emp";
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def selectOne(self, e_id):
        sql = f"""
        select 
            e_id, e_name, sex, addr 
        from 
            emp 
        where 
            e_id = '{e_id}'
        """
        self.curs.execute(sql)
        
        obj = self.curs.fetchall()
        return obj[0] 
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"""
        insert into emp
        (e_id, e_name, sex, addr)
        values 
            ('{e_id}', '{e_name}', '{sex}', '{addr}')
        """
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        return cnt
        
    def update(self, e_id, e_name, sex, addr):
        sql = f"""
        update emp
             set e_id = '{e_id}',
             e_name = '{e_name}',
             sex = '{sex}',
             addr = '{addr}'
           where e_id = '{e_id}'
        """
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
        delete from emp 
        where e_id='{e_id}'"""

        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        return cnt
 
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
    
if __name__ == '__main__':
    de = DaoEmp()
#    list = de.selectList()    
#    obj = de.selectOne("1")
#    cnt = de.insert("3", "3", "3", "3")
    cnt = de.update("4", "4", "4", "4")
#    cnt = de.delete("3")
   
#    print("list", list)    
#    print("obj", obj)    
    print("cnt", cnt)    
#    print("count", count)    
   
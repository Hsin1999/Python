import pymysql
#Datebase（地址，用户名，密码，数据库）
class Database():
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.db=pymysql.connect(host=self.host,
                           user=self.user,
                           password=self.password,
                           database=self.database,
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor
                           )
        self.cur=self.db.cursor()
    #查询数据（sql语句，查询条数（0：默认全部，1：一条））
    def select_Mysql(self,sql,a=0):
        self.cur.execute(sql)
        if isinstance(a,int):
            if a==1:
                result=self.cur.fetchone()
                return result
            elif a==0:
                result=self.cur.fetchall()
                return result
            else:
                raise print('查询条数输入错误')
        else:
            raise print('参数类型错误（int）')
    def delete_Mysql(self,sql):
        try:
            self.cur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def update_Mysql(self,sql):
        try:
            self.cur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_Mysql(self,sql):
        try:
            self.cur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    def close_Mysql(self):
        self.cur.close()

s=Database('47.101.53.77','root','ppaa1122','test')
s.update_Mysql("update t_student set name='wzb' where id=1")
for i in s.select_Mysql('select * from t_student',0):
    print(i)
s.close_Mysql()













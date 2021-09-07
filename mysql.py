import pymysql
class Datebase():
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
    def select_Mysql(self,sql):
        self.cur.execute(sql)












# db=pymysql.connect(host='47.101.53.77',user='root',password='ppaa1122',database='test')
# cursor=db.cursor()
# cursor.execute('insert into t_student values(888,"zzx",2,21,"zhuanye","188888888")')
# db.commit()
# cursor.execute('select * from t_student where id=888')
# result=cursor.fetchone()
# print(result)
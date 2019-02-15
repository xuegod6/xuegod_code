import pymysql
#连接数据库，参数分别为本地地址，用户名，密码，数据库，字符集
db = pymysql.connect('localhost','root','123456','new_test',charset='utf8')
#使用cursor方法创建一个游标对象，相当于一个操作者
cursor = db.cursor()
#使用execute方法执行sql语句，相当于操作者在mysql命令中输入SQL语句并回车

try:
    cursor.execute("delete from test_sql where age ='%d'"%(20))
    db.commit()
except:
    db.rollback()
cursor.close()
#关闭数据库连接
db.close()

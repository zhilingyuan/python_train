#数据库的使用
import pymysql
conn=pymysql.connect(host='',user='',passwd='')
conn.query('sql语句')

cs=conn.cursor() #创建游标
cs.execute('')

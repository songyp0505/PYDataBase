'''
安装Mysql的时候需要安装
https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package

先在bin文件夹打开cmd
输入 create database mydb 建立数据库
通过 use mydb 进入mydb数据库

创建数据表：
CREATE　TABLE　students（
    name char(5),
    sex char(1）,
    grade int
）ENGINE INNODB DEFAULT CHARSET = utf8

可以通过命令行插入数据：
insert into students (name,sex,grade) values("小明","男",92)
'''

import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root',passwd = '123456',db = 'mydb',port = 3306,charset = 'utf8')#连接数据库
cursor = conn.cursor()#光标对象
cursor.execute("insert into students (name,sex,grade) values(%s,%s,%s)",('张三','女',81))#插入数据
conn.commit()#提交改变
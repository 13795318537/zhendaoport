# -*- coding: utf-8 -*-
import pymysql

db = pymysql.connect(
    host='121.46.197.172',
    port=3306,
    user='root',
    password='zhendao@2020',
    charset='utf8',
    database='pymysql'
)

# cur = db.cursor()
# cur.execute('select * from student;')

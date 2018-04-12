# 将输出优惠码保存进数据库
import pymysql
import sys
sys.path.append('..')
from A0001 import Invente_card

HOST = '127.0.0.1'
PORT = 3306
DB = '0002'
CHARSET = 'utf8mb4'
USER = 'root'
PASSWORD = 'wzy850321'


def export_to_mysql():
    sql = "INSERT codes(code) VALUES (%s)"

    with pymysql.Connection(host=HOST, port=PORT, user=USER,
     password=PASSWORD, database=DB, charset=CHARSET) as cursor:
        defination_tables(cursor)
        effect_rows = cursor.executemany(sql, Invente_card.generator())
        print('代码影响行数:' + str(effect_rows))


def defination_tables(cursor):
    cursor.execute('DROP TABLE IF EXISTS `codes`;')
    cursor.execute('CREATE TABLE `codes` ('
                   '  `id` int(11) NOT NULL AUTO_INCREMENT,'
                   '  `code` varchar(10) NOT NULL,'
                   '  PRIMARY KEY (`id`)'
                   ') ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;')


if __name__ == '__main__':
    try:
        export_to_mysql()
    except Exception as e:
        print(e)
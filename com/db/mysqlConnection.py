# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/18 9:22
@file    :mysqlConnection.py
"""
import pymysql
import logging


class MySqlConnect(object):
    def __init__(self, host='localhost', user='root', password='muzili', database='ApiTool', port=3306, charset='utf8'):
        logging.debug("connect mysql>>> host={host}, port={port}, user={user}, password={password}, "
                      "database={database}, charset={charset}".format(host=host, port=port, user=user,
                                                                      password=password, database=database,
                                                                      charset=charset))
        try:
            self.db = pymysql.Connect(host=host, port=port, user=user, password=password,
                                      database=database, charset=charset)
        except Exception as e:
            logging.error("MySQL连接异常>>>{}".format(e))

    def __del__(self):
        try:
            self.db.close()
        except Exception as e:
            logging.error("MySQL关闭异常>>>{}".format(e))

    def execute(self, sql):
        """
        新增、修改、删除
        :param sql:
        :return:
        """
        try:
            # 重连
            self.db.ping(reconnect=True)
            cur = self.db.cursor()
            cur.execute(sql)
            self.db.commit()
            cur.close()
        except Exception as e:
            self.db.rollback()
            logging.error("MySQL执行异常>>>{}".format(e))

    def query(self, sql, is_dict=False):
        """
        查询
        :param sql:
        :param is_dict:
        :return:
        """
        try:
            # 重连
            self.db.ping(reconnect=True)
            if is_dict:
                cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            else:
                cur = self.db.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            logging.error("MySQL执行异常>>>{}".format(e))


if __name__ == "__main__":
    pass

# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/26 17:49
@file    :mysqlConnection.py
"""
from typing import Any

import pymysql

from common.util.logOperation import logger


class MySqlConnect(object):
    def __init__(self, host='localhost', user='root', password='muzili', database='ApiTool', port=3306, charset='utf8'):
        logger.debug("connect mysql: >>> host={host}, port={port}, user={user}, password={password}, "
                     "database={database}, charset={charset}".format(host=host, port=port, user=user,
                                                                     password=password, database=database,
                                                                     charset=charset))
        try:
            self.db = pymysql.Connect(host=host, port=int(port), user=user, password=password,
                                      database=database, charset=charset)
            self.cur = self.db.cursor()
        except Exception as e:
            logger.error("MySQL连接异常: >>>{}".format(e))
            raise e

    def __del__(self):
        try:
            self.cur.close()
            self.db.close()
        except Exception as e:
            logger.error("MySQL关闭异常: >>>{}".format(e))
            raise e

    def execute(self, sql: str) -> None:
        """
        新增、修改、删除
        :param sql:
        :return:
        """
        try:
            # 重连
            self.db.ping(reconnect=True)
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error("MySQL执行异常: >>>{}".format(e))
            raise e

    def query_one(self, sql: str, is_dict: bool = False) -> Any:
        """
        查询单条
        :param sql:
        :param is_dict:
        :return:
        """
        logger.info('查询语句: {}'.format(sql))
        try:
            # 重连
            self.db.ping(reconnect=True)
            if is_dict:
                self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            else:
                self.cur = self.db.cursor()
            self.cur.execute(sql)
            data = self.cur.fetchone()
            return data
        except Exception as e:
            logger.error("MySQL查询异常: >>>{}".format(e))
            raise e

    def query_all(self, sql: str, is_dict: bool = False) -> Any:
        """
        查询多条
        :param sql:
        :param is_dict:
        :return:
        """
        logger.info('查询语句: {}'.format(sql))
        try:
            # 重连
            self.db.ping(reconnect=True)
            if is_dict:
                self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            else:
                self.cur = self.db.cursor()
            self.cur.execute(sql)
            datas = self.cur.fetchall()
            return datas
        except Exception as e:
            logger.error("MySQL查询失败: >>>{}".format(e))
            raise e


if __name__ == "__main__":
    pass

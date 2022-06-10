# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/1 16:56
@file    :test.py
"""
import logging
import re

from com.db.mysqlConnection import MySqlConnect
from com.util.getConfig import Config

con = Config()
host = con.get_config('MySql', 'host')
port = con.get_config('MySql', 'port')
user = con.get_config('MySql', 'user')
password = con.get_config('MySql', 'password')
database = con.get_config('MySql', 'database')
charset = con.get_config('MySql', 'charset')
mysql = MySqlConnect(host=host, port=port, user=user, password=password, database=database, charset=charset)



def sql_extract(case, sql_list: list):
    if re.search('\$DB\{.*?\}', case) is not None:
        res = re.findall('\$DB\{.*?\}', case)
    else:
        return case
    query_result = list()
    for sql in sql_list:
        if ('where' in sql and 'limit' in sql) or ('WHERE' in sql and 'limit' in sql):
            data = mysql.query(sql, is_dict=True)
            query_result.append(data)
        else:
            logging.error("请编写含有where条件的sql: >>>{}".format(sql))
    try:
        for index in range(len(res)):
            var = res[index].split('{')[1].split('}')[0]
            for result in query_result:
                value = result.get(var)
                if value is not None:
                    case = case.replace(res[index], str(value))
                    break
    except KeyError:
        logging.error("获取不到响应报文字段值: >>>{}".format(var))
    except ValueError:
        logging.error("jsonpath表达式有误: >>>{}".format(var))
    return case


if __name__ == "__main__":
    exp = r"^select (.*?) from (.*?) where (.*?)$"
    s = ["select process_name, process_type_id from t_flowable_ent_process_template WHERE process_name = '删除业务类型111' limit 1",
         "select process_name, process_type_id from t_flowable_ent_process_template WHERE process_name = '删除业务类型' limit 1"]

    case = "{'process_name': '$DB{process_name}', 'process_type_id': '$DB{process_type_id}'}"
    print(sql_extract(case, s))
    pass

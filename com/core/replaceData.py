"""
@Time ： 2022/5/19 19:45
@Auth ： muzili
@File ： replaceData.py
@IDE  ： PyCharm
"""
import re
import logging

from jsonpath import jsonpath

from com.core.initializeParam import ini_db_params
from com.db.mysqlConnection import MySqlConnect
from com.util import sysFunc
from api import userFunc
from com.util.getConfig import Config
from com.util.glo import GolStatic


def connection():
    """
    连接mysql
    :return:
    """
    con = Config()
    host = con.get_config('MySql', 'host')
    port = con.get_config('MySql', 'port')
    user = con.get_config('MySql', 'user')
    password = con.get_config('MySql', 'password')
    database = con.get_config('MySql', 'database')
    charset = con.get_config('MySql', 'charset')
    mysql = MySqlConnect(host=host, port=port, user=user, password=password, database=database, charset=charset)
    return mysql


def query_db(sql_list: list):
    """
    查询数据库
    :param sql_list:
    :return: [{}, {}]
    """
    mysql = connection()
    query_result = list()
    for sql in sql_list:
        # if ('where' in sql and 'limit' in sql) or ('WHERE' in sql and 'limit' in sql):
        if 'where' in sql or 'WHERE' in sql:
            sql = ini_db_params(sql)
            logging.info("正在执行的sql: >>>{}".format(sql))
            result = mysql.query(sql, is_dict=True)
            query_result.append(result)
            logging.info("sql的结果: >>>{}".format(result))
        else:
            logging.error("请编写含有where条件的sql: >>>{}".format(sql))
    return query_result


def replace_db(case, data: dict):
    """
    从数据库中查询替换请求报文中的参数值 $DB{变量名}
    :param case: 用例报文
    :param data: 用例数据
    :return:
    """
    if re.search('\$DB\{.*?\}', case) is not None:
        res = re.findall('\$DB\{.*?\}', case)
    else:
        return case
    query_result = query_db(eval(data.get('sql')))
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


def replace_user_var(case, data: dict):
    """
    替换请求报文中的用户参数值 ${变量名}
    :param case: 用例报文
    :param data: 用例数据
    :return:
    """
    if re.search('\$\{.*?\}', case) is not None:
        res = re.findall('\$\{.*?\}', case)
    else:
        return case
    try:
        for index in range(len(res)):
            var = res[index].split('{')[1].split('}')[0]
            case = case.replace(res[index], str(data[var]), 1)
    except KeyError:
        logging.error("获取不到变量值: >>>{}".format(var))
    return case


def replace_func(case):
    """
    替换请求报文中的函数变量值 $(f函数名)
    :param case:
    :return:
    """
    if re.search('\$\(f.*?\)', case) is not None:
        res = re.findall('\$\(f.*?\)', case)
    else:
        return case
    try:
        for index in range(len(res)):
            func_params = res[index].split('(', 1)[1].split(')', 1)[0]
            if "::" in func_params:  # 带参函数
                func_name, params = func_params.split("::")
                func = func_name + '(' + params + ')'
            else:  # 不带参函数
                func = func_params + '()'
            func = eval('sysFunc.' + func)
            case = case.replace(res[index], func, 1)
    except AttributeError:
        logging.error("获取不到系统函数: >>>{}".format(func))
    return case


def replace_user_func(case):
    """
    替换请求报文中的函数变量值 $(u函数名)
    :param case:
    :return:
    """
    if re.search('\$\(u.*?\)', case) is not None:
        res = re.findall('\$\(u.*?\)', case)
    else:
        return case
    try:
        for index in range(len(res)):
            func_params = res[index].split('(', 1)[1].split(')', 1)[0]
            if "::" in func_params:  # 带参函数
                func_name, params = func_params.split("::")
                func = func_name + '(' + params + ')'
            else:  # 不带参函数
                func = func_params + '()'
            func = eval('userFunc.' + func)
            case = case.replace(res[index], func, 1)
    except AttributeError:
        logging.error("获取不到自定义函数: >>>{}".format(func))
    return case


def replace_resp(case):
    """
    从其它接口的响应报文中替换请求报文中的参数值 $Resp{接口名.变量名}
    :param case:
    :return:
    """
    if re.search('\$Resp\{.*?\}', case) is not None:
        res = re.findall('\$Resp\{.*?\}', case)
    else:
        return case
    # 测试专用
    # GolStatic.set_file_temp('test', 'response_body',
    #                         {'businessNo': '123456', 'j': [{'businessNo': '1111'}, {'businessNo': '2222'}]})
    try:
        for index in range(len(res)):
            var = res[index].split('{')[1].split('}')[0]
            filename, var_name = var.split('.', 1)
            response_body = GolStatic.get_file_temp(filename=filename, key='response_body')
            value = jsonpath(response_body, var_name)
            if value:
                case = case.replace(res[index], value[0], 1)
            else:
                case = case.replace(res[index], '', 1)
                logging.error("获取不到响应报文字段值: >>>{}".format(var_name))
    except KeyError:
        logging.error("获取不到响应报文字段值: >>>{}".format(var))
    except ValueError:
        logging.error("jsonpath表达式有误: >>>{}".format(var))
    return case


def replace_req(case):
    """
    从其它接口的请求报文中替换请求报文中的参数值 $Req{接口名.变量名}
    :param case:
    :return:
    """
    if re.search('\$Req\{.*?\}', case) is not None:
        res = re.findall('\$Req\{.*?\}', case)
    else:
        return case
    # 测试专用
    # GolStatic.set_file_temp('test', 'request_body',
    #                         {'businessNo': '123456', 'j': [{'businessNo': '1111'}, {'businessNo': '2222'}]})
    try:
        for index in range(len(res)):
            var = res[index].split('{')[1].split('}')[0]
            filename, var_name = var.split('.', 1)
            request_body = GolStatic.get_file_temp(filename=filename, key='request_body')
            value = jsonpath(request_body, var_name)
            if value:
                case = case.replace(res[index], value[0], 1)
            else:
                case = case.replace(res[index], '', 1)
                logging.error("获取不到请求报文字段值: >>>{}".format(var_name))
    except KeyError:
        logging.error("获取不到请求报文字段值: >>>{}".format(var))
    except ValueError:
        logging.error("jsonpath表达式有误: >>>{}".format(var))
    return case


if __name__ == "__main__":
    from com.util.yamlOperation import read_yaml
    from com.util.getFileDirs import APIYAML

    # file = APIYAML + '\\addInvoiceToConfirm.yaml'
    # case = read_yaml(file)
    # d = {"payTaxpayerName": "muzili", "businessNo": "123456"}
    # case = replace_uservar(case, d)
    # case = replace_func(case)
    # case = replace_user_func(case)
    # print(case)
    # case = "afafa$(unum)asdf$(fnum::5)aaaa$(fnum::length=10)nbbb"
    # if re.search('\$\(u.*?\)', case) is not None:
    #     res = re.findall('\$\(u.*?\)', case)
    #     print(res)
    # else:
    #     print("case:", case)
    # for i in range(len(res)):
    #     func_param = res[i].split('(', 1)[1].split(')', 1)[0]
    #     if "::" in func_param:
    #         funcName, param = func_param.split("::")
    #         func = funcName + '(' + param + ')'
    #     else:
    #         func = func_param + '()'
    #     func = eval('userFunc.' + func)
    #     case = case.replace(res[i], func, 1)
    #     print(case)
    case = '{"businessNo": "$Req{test.j[1].businessNo}", "payTaxpayerName": "${muzili}", "businessNo": "$Req{test.businessNo}"}'
    data = {"muzili": '12'}
    # print(replace_resp(case))
    print(replace_req(case))

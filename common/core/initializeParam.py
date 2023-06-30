# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/28 17:32
@file    :initializeParam.py
"""
import re

from common.core import replaceData
from common.util.globalVars import GolStatic
from common.util.logOperation import logger


class DisposeBody(object):
    def __init__(self):
        self.MYCONFIG = GolStatic.get_pro_var('MYCONFIG')

    def ini_request_headers(self, request_headers: dict, test_data: dict) -> dict:
        """
        请求头处理
        :param self:
        :param request_headers:
        :param test_data
        :return:
        """
        try:
            default_headers = dict(self.MYCONFIG.get_items('HEADERS'))
            default_project = dict(self.MYCONFIG.get_items('PROJECT'))
        except Exception as e:
            logger.error("配置文件request_headers 或 default_project 不存在: >>>{default_headers}, {default_project}".format(
                default_headers=default_headers, default_project=default_project))
            logger.error("报错信息: >>>{}".format(e))
            raise e
        # headers
        method = request_headers.get('Method') or default_headers.get('Method')
        content_type = request_headers.get('Content-Type') or default_headers.get('Content-Type')
        user_agent = request_headers.get('User-Agent') or default_headers.get('User-Agent')
        connection = request_headers.get('Connection') or default_headers.get('Connection')
        timeout = request_headers.get('timeout') or default_headers.get('timeout')
        base_url = request_headers.get('base_url') or default_project.get('base_url')
        logger.info("request_headers处理前: >>>{}".format(request_headers))
        try:
            header = {'Method': method, 'Content-Type': content_type, 'User-Agent': user_agent,
                      'Connection': connection,
                      'timeout': int(timeout), 'base_url': base_url}
            header = eval(replaceData.replace_user_var(str(header), test_data))
            request_headers.update(header)
        except Exception as e:
            logger.error("request_headers处理失败: >>>{}".format(e))
        logger.info("request_headers处理后: >>>{}".format(request_headers))
        return request_headers

    def ini_db_params(self, sql: str):
        """
        初始化sql
        :param self:
        :param sql:
        :return:
        """
        # 从请求报文获取参数值
        if re.search('\$Req\{.*?\}', sql) is not None:
            sql = replaceData.replace_req(sql)
        # 从响应报文获取参数值
        if re.search('\$Resp\{.*?\}', sql) is not None:
            sql = replaceData.replace_resp(sql)
        return sql

    def ini_params(self, case_body: dict) -> dict:
        """
        初始化报文
        :param self:
        :param case_body：测试报文
        :return:
        """
        logger.info("body处理前: >>>{}".format(case_body))
        """
        # 用户自定义参数化
        if re.search('\$\{.*?\}', str(test_info)) is not None:
            test_info = eval(replaceData.replace_user_var(str(test_info), test_data))
        # 系统函数参数化
        if re.search('\$\(f.*?\)', str(test_info)) is not None:
            test_info = eval(replaceData.replace_func(str(test_info)))
        # 用户自定义函数参数化
        if re.search('\$\(u.*?\)', str(test_info)) is not None:
            test_info = eval(replaceData.replace_user_func(str(test_info)))
        # 从数据库获取参数值
        if re.search('\$DB\{.*?\}', str(test_info)) is not None:
            test_info = eval(replaceData.replace_db(str(test_info), test_data))
        """
        # 从请求报文获取参数值
        if re.search('\$Req\{.*?\}', str(case_body)) is not None:
            case_body = eval(replaceData.replace_req(str(case_body)))
        # 从响应报文获取参数值
        if re.search('\$Resp\{.*?\}', str(case_body)) is not None:
            case_body = eval(replaceData.replace_resp(str(case_body)))
        logger.info("body处理后: >>>{}".format(case_body))
        return case_body

    def ini_package(self, case: dict, body_value: dict):
        """
        组装报文
        :param self:
        :param case: 用例请求体内容
        :param body_value: 用例请求体参数化内容
        :return:
        """
        case_body = self.ini_params(case.get('data'))
        self.body(case_body, body_value)
        case.update({'data': case_body})

    def body(self, case_body: dict, body_value: dict) -> None:
        """
        处理dict字段值
        :param self:
        :param case_body:
        :param body_value:
        :return:
        """
        if case_body is None:
            logger.info("body: case_body为None, 不做参数化处理")
        # dict为空, 直接替换
        elif len(case_body) == 0:
            case_body.update(body_value)
        else:
            for key, value in body_value.items():
                if isinstance(value, dict):
                    self.body(case_body.get(key), value)
                elif isinstance(value, list):
                    self.body_list(case_body.get(key), value)
                else:
                    case_body.__setitem__(key, value)

    def body_list(self, case_body: list, body_value: list) -> None:
        """
        处理list字段值
        :param self:
        :param case_body:
        :param body_value:
        :return:
        """
        if case_body is None:
            logger.info("body_list: case_body为None, 不做参数化处理")
        else:
            for index, value in enumerate(body_value):
                if len(case_body).__eq__(0):
                    # list为空, 直接替换
                    case_body.extend(body_value)
                    break
                if isinstance(value, dict):
                    try:
                        self.body(case_body[index], value)
                    except IndexError:
                        # 下标溢出直接添加报文
                        case_body.append(value)
                elif isinstance(value, list):
                    try:
                        self.body_list(case_body[index], value)
                    except IndexError:
                        # 下标溢出直接添加报文
                        case_body.append(value)
                else:
                    case_body[index] = value


if __name__ == '__main__':
    ...

# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/25 16:50
@file    :globalVars.py
"""
from typing import Any

from common.util.logOperation import logger


class GolStatic(object):
    # 存放接口执行的请求报文与响应报文
    _file_var = dict()
    # 存放案例变量
    _case_var = dict()
    # 存放脚本的变量
    _script_var = dict()
    # 存放项目运行变量
    _project_var = dict()

    @classmethod
    def set_file_var(cls, filename: Any, key: Any, value: Any) -> None:
        """
        设置一个全局变量
        :param filename:
        :param key:
        :param value:
        :return:
        """
        if cls._file_var.get(filename) is None:
            cls._file_var[filename] = {key: value}
        else:
            cls._file_var[filename].update({key: value})

    @classmethod
    def get_file_var(cls, filename: Any, key: Any) -> Any:
        """
        获得一个全局变量,不存在则返回 None
        :param filename: 文件名
        :param key: 变量名
        :return:
        """
        value = None
        try:
            value = cls._file_var[filename][key]
        except KeyError:
            logger.error("变量值不存在，获取失败：>>> key={}".format(key))
        finally:
            return value

    @classmethod
    def get_case_var(cls, filename: Any) -> Any:
        """
        获取案例文件的变量
        :param filename:
        :return:
        """
        value = None
        try:
            value = cls._case_var[filename]
        except KeyError:
            logger.error("文件案例变量值不存在，获取失败：>>> filename={}".format(filename))
        finally:
            return value

    @classmethod
    def set_case_var(cls, filename: Any, value: Any) -> None:
        """
        存放案例文件的变量
        :param filename:
        :param value:
        :return:
        """
        if cls._case_var.get(filename) is None:
            cls._case_var[filename] = [value]
        else:
            cls._case_var[filename].append(value)

    @classmethod
    def set_script_var(cls, filename: Any, value: Any) -> None:
        """
        存放脚本文件的变量
        :param filename: 接口名
        :param value:
        :return:
        """
        if cls._script_var.get(filename) is None:
            cls._script_var[filename] = [value]
        else:
            cls._script_var[filename].append(value)

    @classmethod
    def get_script_var(cls, filename: Any) -> Any:
        """
        获取脚本文件的变量
        :param filename:
        :return:
        """
        value = None
        try:
            value = cls._script_var[filename]
        except KeyError:
            logger.error("脚本文件变量值不存在，获取失败：>>> filename={}".format(filename))
        finally:
            return value

    @classmethod
    def get_this_script_var(cls, filename: Any) -> list:
        """
        获取指定脚本的变量
        :param filename:
        :return:
        """
        key_list = cls._script_var.keys()
        value_list = list()
        filename = filename + '_'
        if len(key_list) > 0:
            for key in key_list:
                if filename in key:
                    value_list.append(cls._script_var.get(key))
        return value_list

    @classmethod
    def set_pro_var(cls, key: Any, value: Any) -> None:
        """
        设置一个全局变量
        :param key:
        :param value:
        :return:
        """
        cls._project_var[key] = value

    @classmethod
    def get_pro_var(cls, key: Any) -> Any:
        """
        获取项目运行设置的全局变量
        :param key:
        :return:
        """
        value = None
        try:
            value = cls._project_var[key]
        except KeyError:
            logger.error("项目运行全局变值不存在，获取失败：>>> key={}".format(key))
        finally:
            return value


if __name__ == "__main__":
    pass

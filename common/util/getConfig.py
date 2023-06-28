# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/25 15:24
@file    :getConfig.py
"""
import configparser
import os
from typing import Any

from common.util.filePath import CONFDIR, CONFDIRENV
from common.util.logOperation import logger


class MyConfigParser(configparser.ConfigParser):

    def __init__(self, defaults: Any = None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    # 重新optionxform方法，父类optionxform方法默认返回字符串转小写
    def optionxform(self, optionstr: str) -> str:
        return optionstr


class MyConfig(object):

    def __init__(self, path: str = CONFDIR):
        if not os.path.exists(path):
            logger.error('配置文件不存在: {}'.format(path))
            raise FileNotFoundError("配置文件不存在！")
        self.cf = MyConfigParser()
        self.path = path
        self.cf.read(self.path, encoding='utf8')
        self.config_dic = dict()

    def get_config(self, section: Any, item: Any) -> str:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = self.config_dic[section][item]
        except KeyError:
            value = self.cf.get(section, item)
            self.config_dic[section][item] = value
        finally:
            return value

    def get_config_int(self, section: Any, item: Any) -> int:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = self.config_dic[section][item]
        except KeyError:
            value = self.cf.getint(section, item)
            self.config_dic[section][item] = value
        finally:
            return value

    def get_config_float(self, section: Any, item: Any) -> float:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = self.config_dic[section][item]
        except KeyError:
            value = self.cf.getfloat(section, item)
            self.config_dic[section][item] = value
        finally:
            return value

    def get_config_bool(self, section: Any, item: Any) -> bool:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = self.config_dic[section][item]
        except KeyError:
            value = self.cf.getboolean(section, item)
            self.config_dic[section][item] = value
        finally:
            return value

    def get_sections(self) -> list:
        """
        :return: 以列表形式返回所有的section
        """
        return self.cf.sections()

    def get_options(self, section: Any) -> list:
        """
        :param section:
        :return: 得到指定section的所有option
        """
        value = None
        try:
            value = self.cf.options(section)
        except configparser.NoSectionError:
            logger.error("section不存在: >>>{}".format(section))
        finally:
            return value

    def get_items(self, section: Any) -> Any:
        """
        :param section:
        :return: 得到指定section的所有键值对
        """
        value = None
        try:
            value = self.cf.items(section)
        except configparser.NoSectionError:
            logger.error("section不存在: >>>{}".format(section))
        finally:
            return value

    def add_section(self, section: Any) -> bool:
        """
        :param section: 添加一个新的section
        :return: 添加成功返回True
        """
        flag = False
        try:
            self.cf.add_section(section)
            self.cf.write(open(self.path, "w"))
            flag = True
        except FileNotFoundError:
            logger.error("No such file or directory: >>>{}".format(self.path))
        finally:
            return flag

    def set_config(self, section: Any, option: Any, value: Any) -> bool:
        """
        :param section: 原有的 section
        :param option: 新增或修改 key 的 value 值
        :param value: 新的 value
        :return: 添加成功返回True
        """
        flag = False
        try:
            self.cf.set(section, option, value)
            self.cf.write(open(self.path, "w"))
            flag = True
        except configparser.NoSectionError:
            logger.error("section不存在: >>>{}".format(section))
        finally:
            return flag

    def remove_section(self, section: Any) -> bool:
        """
        :param section: 删除一个 section
        :return: 删除成功返回True
        """
        flag = False
        try:
            self.cf.remove_section(section)
            self.cf.write(open(self.path, "w"))
            flag = True
        except FileNotFoundError:
            logger.error("No such file or directory: >>>{}".format(self.path))
        finally:
            return flag

    def remove_option(self, section: Any, option: Any) -> bool:
        """
        :param section: 原有的 section
        :param option: 要删除的 option
        :return: 删除成功返回True
        """
        flag = False
        try:
            self.cf.remove_option(section, option)
            self.cf.write(open(self.path, "w"))
            flag = True
        except configparser.NoSectionError:
            logger.error("section不存在: >>>{}".format(section))
        finally:
            return flag


if __name__ == "__main__":
    ...

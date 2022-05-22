# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/21 12:55
@Auth ： muzili
@File ： fileOperation.py
@IDE  ： PyCharm
"""
import os
import logging


def get_all_file(path):
    """
    获取所有文件路径
    :param path:
    :return:
    """
    files_path = []
    try:
        files = os.listdir(path)
        for f in files:
            f_path = os.path.join(path, f)
            files_path.append(f_path)
    except FileNotFoundError:
        logging.error("找不到指定的文件路径>>>{}".format(path))
    return files_path


def get_file_name(path):
    """
    获取文件名字
    :param path:
    :return:
    """
    return os.path.split(path)[1]


if __name__ == "__main__":
    pass

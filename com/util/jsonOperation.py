# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/30 12:09
@file    :jsonOperation.py
"""
import os
import logging
import json


def read_json(file, is_str=True):
    """
    读取json文件内容
    :param file:
    :param is_str: 为False时返回dict
    :return: 默认返回str
    """
    if not os.path.exists(file):
        logging.error("文件不存在, 获取数据失败: >>>{}".format(file))
        return None
    with open(file=file, encoding='utf-8') as f:
        content = json.load(f)
    if is_str:
        return str(content)
    else:
        return content


if __name__ == "__main__":
    from com.util.getFileDirs import APIJSON
    path = APIJSON + '\\' + 'api.json'
    print(read_json(path, is_str=False))
    print(type(read_json(path, is_str=False)))
    pass

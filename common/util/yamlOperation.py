# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/26 10:06
@file    :yamlOperation.py
"""
import os
from typing import Any

import yaml

from common.util.logOperation import logger


def read_yaml(file: str, is_str: bool = True) -> Any:
    """
    读取yaml文件内容
    :param file:
    :param is_str: 为False时返回dict
    :return: 默认返回str
    """
    if not os.path.exists(file):
        logger.error("文件不存在, 获取数据失败: >>>{}".format(file))
        return None
    with open(file=file, encoding='utf-8') as f:
        content = yaml.load(f, yaml.FullLoader)
    if is_str:
        return str(content)
    else:
        return content


def write_yaml(file: str, obj: object) -> bool:
    """
    将python对象写入yaml文件
    :param file:
    :param obj:
    :return:
    """
    # sort_keys=False字段表示不改变原数据的排序
    # allow_unicode=True 允许写入中文，必须以字节码格式写入
    if not os.path.exists(file):
        logger.error("文件不存在, 写入数据失败: >>>{}".format(file))
        return False
    with open(file=file, mode="w", encoding='utf-8') as f:
        yaml.dump(data=obj, stream=f, sort_keys=False, allow_unicode=True)
    return True


if __name__ == "__main__":
    ...

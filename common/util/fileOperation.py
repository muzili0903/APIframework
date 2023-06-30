# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/26 10:17
@file    :fileOperation.py
"""
import os

from common.util.excelOperation import ReadExcel
from common.util.filePath import ensure_path_sep
from common.util.logOperation import logger
from common.util.yamlOperation import write_yaml


def get_all_file(path: str) -> list:
    """
    获取所有文件路径
    :param path:
    :return:
    """
    files_path = []
    try:
        files = os.listdir(path)
        for f in files:
            f_path = ensure_path_sep(os.path.join(path, f))
            files_path.append(f_path)
    except FileNotFoundError:
        logger.error("找不到指定的文件路径: >>>{}".format(path))
    except NotADirectoryError:
        logger.error("目录名称无效: >>>{}".format(path))
    return files_path


def get_file_name(path: str) -> str:
    """
    获取文件名字
    :param path:
    :return:
    """
    return os.path.split(path)[1]


def get_file_path(path: str) -> str:
    """
    获取文件所在路径
    :param path:
    :return:
    """
    return os.path.split(path)[0]


def single_excel_to_yaml(sheetname: str, interface: str = '',
                         path: str = r"..\..\testData\pro\APIAutoTestDataModel.xlsx") -> None:
    """
    单表单或单接口转为yaml文件
    :param path: 路径
    :param sheetname: 表table名
    :param interface: 接口名
    """
    datas = ReadExcel(filename=path, sheet_name=sheetname).read_to_dict()
    yamlPath = get_file_path(path) + '\\' + sheetname + '\\'
    if interface.__eq__(''):
        for filename, data in datas.items():
            yamlPath += filename + '.yaml'
            write_yaml(ensure_path_sep(yamlPath), data)
    else:
        for filename, data in datas.items():
            if interface.__eq__(filename):
                yamlPath += filename + '.yaml'
                write_yaml(ensure_path_sep(yamlPath), data)
                break
        else:
            print("接口不存在")


if __name__ == '__main__':
    print(single_excel_to_yaml('model'))
    ...

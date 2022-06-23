# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/21 12:55
@Auth ： muzili
@File ： fileOperation.py
@IDE  ： PyCharm
"""
import os
import logging

from com.util.getFileDirs import APIJSON, APIYAML
from com.util.jsonOperation import read_json
from com.util.yamlOperation import write_yaml


def json_to_yaml(con):
    """
    json文件转为yaml文件
    :param con:
    :return:
    """
    json_all_file = get_all_file(APIJSON)
    yaml_all_file = get_all_file(APIYAML)
    yaml_file_list = list()
    for yaml_file in yaml_all_file:
        yaml_file_name = get_file_name(yaml_file).split('.')[0]
        yaml_file_list.append(yaml_file_name)
    for json_file in json_all_file:
        json_file_name = get_file_name(json_file)
        # 预期结果的文件不转换
        if '_response.json' in json_file_name:
            pass
        else:
            json_file_name = json_file_name.split('.')[0]
            # 已存在yaml文件的不转换
            if con.get_config('API', 'exist_json_to_yaml').capitalize() and json_file_name in yaml_file_list:
                pass
            # 指定json文件转yaml文件, 没有指定默认转全部
            elif len(eval(con.get_config('API', 'json_to_yaml_file'))):
                if json_file_name in eval(con.get_config('API', 'json_to_yaml_file')):
                    yaml_file_name = APIYAML + '\\' + json_file_name + '.yaml'
                    content = read_json(json_file, is_str=False)
                    write_yaml(yaml_file_name, content)
                else:
                    pass
            # 指定json文件不转yaml文件, 没有指定默认转全部
            elif len(eval(con.get_config('API', 'json_not_to_yaml_file'))):
                if json_file_name in eval(con.get_config('API', 'json_not_to_yaml_file')):
                    pass
                else:
                    yaml_file_name = APIYAML + '\\' + json_file_name + '.yaml'
                    content = read_json(json_file, is_str=False)
                    write_yaml(yaml_file_name, content)
            else:
                yaml_file_name = APIYAML + '\\' + json_file_name + '.yaml'
                content = read_json(json_file, is_str=False)
                write_yaml(yaml_file_name, content)


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
        logging.error("找不到指定的文件路径: >>>{}".format(path))
    except NotADirectoryError:
        logging.error("目录名称无效: >>>{}".format(path))
    return files_path


def get_file_name(path):
    """
    获取文件名字
    :param path:
    :return:
    """
    return os.path.split(path)[1]


if __name__ == "__main__":
    from com.util.getConfig import Config
    con = Config()
    print(len(eval(con.get_config('API', 'json_to_yaml_file'))) == 0)
    if con.get_config('API', 'json_to_yaml'):
        json_to_yaml(con)
    pass

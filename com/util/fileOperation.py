# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/21 12:55
@Auth ： muzili
@File ： fileOperation.py
@IDE  ： PyCharm
"""
import os
import logging
import zipfile

from com.util.getFileDirs import APIJSON, APIYAML, HISTORY
from com.util.jsonOperation import read_json
from com.util.sysFunc import ftime, fdate
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


def make_zip(source_dir, output_filename=None):
    """
    打包目录为zip文件（未压缩）
    :param source_dir:
    :param output_filename:
    :return:
    """
    if output_filename is None:
        output_filename = HISTORY + '\\' + fdate() + ftime() + '.zip'
    with zipfile.ZipFile(output_filename, 'w') as zip_file:
        pre_len = len(os.path.dirname(source_dir))
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zip_file.write(pathfile, arcname)


def un_zip(file_name):
    """
    解压目录为zip文件
    :param file_name:
    :return:
    """
    with zipfile.ZipFile(file_name) as zip_file:
        if os.path.isdir(file_name + "_files"):
            pass
        else:
            os.mkdir(file_name + "_files")
        for names in zip_file.namelist():
            zip_file.extract(names, file_name + "_files/")


if __name__ == "__main__":
    # from com.util.getConfig import Config
    # from com.util.getFileDirs import REPORT, HISTORY
    #
    # path = HISTORY + '\\test.zip'
    # # make_zip('1')
    # # get_all_file('1')
    # un_zip(path)

    # con = Config()
    # print(len(eval(con.get_config('API', 'json_to_yaml_file'))) == 0)
    # if con.get_config('API', 'json_to_yaml'):
    #     json_to_yaml(con)
    pass

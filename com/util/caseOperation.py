# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/21 17:34
@Auth ： muzili
@File ： caseOperation.py
@IDE  ： PyCharm
"""
import logging

from com.util.getFileDirs import APISCENE, APISCRIPT, APIDATA
from com.util.fileOperation import get_all_file, get_file_name
from com.util.yamlOperation import read_yaml
from com.util.getConfig import Config


def get_scene(path):
    """
    获取场景用例
    :param path:
    :return:
    """
    scene_all_file = get_all_file(path)
    scene = list()
    for scene_file in scene_all_file:
        scene_file_name = get_file_name(scene_file)
        # print('scene_file:', scene_file_name)
        scene_file = Config(scene_file)
        scene_name = scene_file.get_sections()
        scene_api = dict()
        for name in scene_name:
            scene_api_name = scene_file.get_items(name)
            scene_api_script = api_to_script(scene_file_name, scene_api_name)
            # scene_api_data = get_case_data(scene_file_name, scene_api_name)
            # print(scene_api_data)
            # print(scene_api_name)
            scene_api.update({name: scene_api_script})
        scene.append({scene_file_name: scene_api})
    print(scene)
    return scene


def get_script(file):
    """
    获取接口脚本文件内容
    :param file:
    :return:
    """
    path = APISCRIPT + '\\' + file + '.yaml'
    yaml_content = read_yaml(path, is_str=False)
    if yaml_content is not None:
        try:
            request_header = yaml_content.__getitem__('request_header')
            request_body = yaml_content.__getitem__('request_body')
            return {'script': {"request_header": request_header, "request_body": request_body}}
        except Exception as e:
            logging.error("script脚本格式有误>>>{}".format(file))
            logging.error("获取接口脚本文件内容>>>{}".format(e))
    return None


def api_to_script(scene_file_name, scene_api_name):
    """
    替换接口名对应的接口script脚本
    :param scene_api_name: 场景下的接口名
    :return:
    """
    temp = list()
    for api_name in scene_api_name:
        api_name_list = list(api_name)
        api_name_list[1] = get_script(api_name[1])
        print(type(api_name_list[1]))
        # print("api_name_list:", api_name_list)
        # print("api_name_list:", {api_name_list[0]: api_name_list[1]})
        api_data = get_case_data(scene_file_name, api_name[1])
        api_name_list[1].update({'data': api_data})
        # temp.append({api_name[1]: tuple(api_name_list)})
        # temp.append({api_name[1]: {api_name_list[0]: api_name_list[1]}, 'data': api_data})
        temp.append({api_name[1]: {api_name_list[0]: api_name_list[1]}})
    return temp


def get_case_data(scene_file, api_name):
    """
    获取用户自定义参数化变量值
    :param scene_file:
    :param api_name:
    :return:
    """
    # temp = list()
    path = APIDATA + '\\' + scene_file
    scene_file_data = Config(path)
    # temp.append({scene_api_name: scene_file_data.get_items(scene_api_name)})
    return dict(scene_file_data.get_items(api_name))


if __name__ == "__main__":
    get_scene(APISCENE)
    pass
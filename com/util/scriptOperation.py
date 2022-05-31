# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/31 12:16
@file    :scriptOperation.py
"""
import logging

import pytest
from com.util.caseOperation import get_scene
from com.util.getFileDirs import APISCENE


def write_pytest_header():
    pass


def write_pytest_content():
    pass


def write_pytest_tail():
    pass


def write_scene_script(path):
    """
    文件路径
    :param path:
    :return:
    """
    scene_all_list = get_scene(path)
    for scene_list in scene_all_list:
        for key_scene, scene in scene_list.items():
            for key, value in scene.items():
                scene_file_name = key_scene.split('.')[0] + key.capitalize()
                yield [scene_file_name, value]


def write_script():
    scene_script = write_scene_script(APISCENE)
    while True:
        try:
            script_file_name, contents = scene_script.__next__()
            for content in contents:
                print(content)
        except StopIteration:
            break


if __name__ == "__main__":
    write_script()
    pass

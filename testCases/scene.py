# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/31 8:26
@file    :scene.py
"""
import logging

import pytest
from com.util.caseOperation import get_scene
from com.util.getFileDirs import APISCENE

# scene_all_list = get_scene(APISCENE)
# for scene_list in scene_all_list:
#     for key_scene, scene in scene_list.items():
#         for key, value in scene.items():
#             print(key_scene.split('.')[0] + key.capitalize())
#             print(key, value)
#             print(key, type(value))


def write_scene_script(path):
    scene_all_list = get_scene(path)
    for scene_list in scene_all_list:
        for key_scene, scene in scene_list.items():
            for key, value in scene.items():
                scene_file_name = key_scene.split('.')[0] + key.capitalize()
                yield [scene_file_name, value]


if __name__ == "__main__":
    scene_script = write_scene_script(APISCENE)
    while True:
        try:
            print(scene_script.__next__())
        except StopIteration:
            break
    pass

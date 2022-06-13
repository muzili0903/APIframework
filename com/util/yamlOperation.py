"""
@Time ： 2022/5/18 21:09
@Auth ： muzili
@File ： yamlOperation.py
@IDE  ： PyCharm
"""
import yaml
import os
import logging


def read_yaml(file, is_str=True):
    """
    读取yaml文件内容
    :param file:
    :param is_str: 为False时返回dict
    :return: 默认返回str
    """
    if not os.path.exists(file):
        logging.error("文件不存在, 获取数据失败: >>>{}".format(file))
        return None
    print(file)
    with open(file=file, encoding='utf-8') as f:
        content = yaml.load(f, yaml.FullLoader)
    if is_str:
        return str(content)
    else:
        return content


def write_yaml(file, obj):
    """
    将python对象写入yaml文件
    :param file:
    :param obj:
    :return:
    """
    # sort_keys=False字段表示不改变原数据的排序
    # allow_unicode=True 允许写入中文，必须以字节码格式写入
    with open(file=file, mode="w", encoding='utf-8') as f:
        yaml.dump(data=obj, stream=f, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    from com.util.getFileDirs import APIJSON, APIYAML
    import json
    file = APIJSON + '\\login.json'
    with open(file=file, mode="r", encoding="utf-8") as f:
        content = json.load(f)
    fileName = APIYAML + '\\login.yaml'
    write_yaml(fileName, content)

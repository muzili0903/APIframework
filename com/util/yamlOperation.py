"""
@Time ： 2022/5/18 21:09
@Auth ： muzili
@File ： yamlOperation.py
@IDE  ： PyCharm
"""
import yaml
import os
import logging


def read_yaml(file):
    """
    读取yaml文件内容
    :param file:
    :return:
    """
    if not os.path.exists(file):
        logging.error("文件不存在, 获取数据失败>>>{}".format(file))
        return None
    with open(file=file, encoding='utf-8') as f:
        content = yaml.load(f, yaml.FullLoader)
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
    apiData = {
        "page": 1,
        "msg": "地址",
        "data": [{
            "id": 1,
            "name": "学校"
        }, {
            "id": 2,
            "name": "公寓"
        }, {
            "id": 3,
            "name": "流动人口社区"
        }]
    }
    write_yaml(r"E:\project\APIframework\config\test1.yaml", apiData)
    data = read_yaml(r"E:\project\APIframework\config\test1.yaml")
    print(data)
    pass

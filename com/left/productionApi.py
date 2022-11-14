# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/3 13:53
@Auth ： muzili
@File ： productionApi.py
@IDE  ： PyCharm
"""
import logging

from com.left import fieldsDispose
from com.util.excelOperation import ReadExcel
from com.util.getFileDirs import LEFT


def production(path, api_name='apiname'):
    """
    处理报文字段
    :param path:
    :param api_name: 接口名称
    :return:
    """
    excel = ReadExcel(path, sheet_name='api_name')
    header = excel.get_rows(row_x=1)
    api = dict()
    for i in range(3, excel.get_max_row()):
        field = dict(zip(header, excel.get_rows(row_x=i)))
        if field.get('type').lower().__eq__('int'):
            api.update({field.get('field'): fieldsDispose.dispose_int(field)})
        elif field.get('type').lower().__eq__('float'):
            api.update({field.get('field'): fieldsDispose.dispose_float(field)})
        elif field.get('type').lower().__eq__('string'):
            api.update({field.get('field'): fieldsDispose.dispose_string(field)})
        elif field.get('type').lower().__eq__('list'):
            api.update({field.get('field'): fieldsDispose.dispose_list(field)})
        elif field.get('type').lower().__eq__('object'):
            api.update({field.get('field'): fieldsDispose.dispose_object(field)})
        else:
            logging.error("字段类型不正确: >>>{}".format(field.get('type')))


if __name__ == "__main__":
    path = LEFT + '\\' + 'testLeft.xlsx'
    production(path)

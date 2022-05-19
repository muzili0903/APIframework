"""
@Time ： 2022/5/19 20:25
@Auth ： muzili
@File ： glo.py
@IDE  ： PyCharm
"""


class GolStatic(object):
    # 存放案例执行临时变量
    __file_temp = dict()
    # 存放案例变量
    __case_temp = dict()
    # 存放脚本的变量
    __script_temp = dict()

    @classmethod
    def set_file_temp(cls, filename, key, value):
        """
        设置一个全局变量
        :param filename:
        :param key:
        :param value:
        :return:
        """
        if cls.__file_temp.get(filename) is None:
            cls.__file_temp[filename] = {key: value}
        else:
            cls.__file_temp[filename].update({key: value})

    @classmethod
    def get_file_temp(cls, filename, key):
        """
        获得一个全局变量,不存在则返回None
        :param filename: 文件名
        :param key: 变量名
        :param def_value:
        :return:
        """
        value = None
        try:
            value = cls.__file_temp[filename][key]
        except KeyError:
            pass
        return value

    @classmethod
    def get_case_temp(cls, filename):
        """
        获取案例文件的变量
        :param filename:
        :return:
        """
        try:
            value = cls.__case_temp[filename]
        except KeyError:
            value = None
        return value

    @classmethod
    def set_case_temp(cls, filename, value):
        """
        存放案例文件的变量
        :param filename:
        :param value:
        :return:
        """
        if cls.__case_temp.get(filename) is None:
            cls.__case_temp[filename] = [value]
        else:
            cls.__case_temp[filename].append(value)

    @classmethod
    def get_script_temp(cls, filename):
        """
        获取脚本文件的变量
        :param filename:
        :return:
        """
        try:
            value = cls.__script_temp[filename]
        except KeyError:
            value = None
        return value

    @classmethod
    def get_this_script_temp(cls, filename):
        """
        获取指定脚本的变量
        :param filename:
        :return:
        """
        key_list = cls.__script_temp.keys()
        print('key_list: ', key_list)
        value_list = list()
        filename = filename + '_'
        if len(key_list) > 0:
            for key in key_list:
                if filename in key:
                    value_list.append(cls.__script_temp.get(key))
        return value_list

    @classmethod
    def set_script_temp(cls, filename, value):
        """
        存放脚本文件的变量
        :param filename:
        :param value:
        :return:
        """
        if cls.__script_temp.get(filename) is None:
            cls.__script_temp[filename] = [value]
        else:
            cls.__script_temp[filename].append(value)


if __name__ == "__main__":
    pass

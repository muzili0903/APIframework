"""
@Time �� 2022/5/19 20:25
@Auth �� muzili
@File �� glo.py
@IDE  �� PyCharm
"""


class GolStatic(object):
    # ��Ű���ִ����ʱ����
    __file_temp = dict()
    # ��Ű�������
    __case_temp = dict()
    # ��Žű��ı���
    __script_temp = dict()

    @classmethod
    def set_file_temp(cls, filename, key, value):
        """
        ����һ��ȫ�ֱ���
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
        ���һ��ȫ�ֱ���,�������򷵻�None
        :param filename: �ļ���
        :param key: ������
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
        ��ȡ�����ļ��ı���
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
        ��Ű����ļ��ı���
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
        ��ȡ�ű��ļ��ı���
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
        ��ȡָ���ű��ı���
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
        ��Žű��ļ��ı���
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

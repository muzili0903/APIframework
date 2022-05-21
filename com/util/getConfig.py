"""
@Time ： 2022/5/18 22:04
@Auth ： muzili
@File ： getConfig.py
@IDE  ： PyCharm
"""
import configparser

from com.util.getFileDirs import CONFDIR


class Config(object):
    config_dic = {}

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(CONFDIR, encoding='utf8')

    def get_config(self, section, item) -> str:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = Config.config_dic[section][item]
        except KeyError:
            value = self.cf.get(section, item)
            Config.config_dic[section][item] = value
        finally:
            return value

    def get_config_int(self, section, item) -> int:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = Config.config_dic[section][item]
        except KeyError:
            value = self.cf.getint(section, item)
            Config.config_dic[section][item] = value
        finally:
            return value

    def get_config_float(self, section, item) -> float:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = Config.config_dic[section][item]
        except KeyError:
            value = self.cf.getfloat(section, item)
            Config.config_dic[section][item] = value
        finally:
            return value

    def get_config_bool(self, section, item) -> bool:
        """
        :param section: 配置内容
        :param item: 配置key
        :return:
        """
        value = None
        try:
            value = Config.config_dic[section][item]
        except KeyError:
            value = self.cf.getboolean(section, item)
            Config.config_dic[section][item] = value
        finally:
            return value

    def get_sections(self) -> list:
        """
        :return: 以列表形式返回所有的section
        """
        return self.cf.sections()

    def get_options(self, section) -> list:
        """
        :param section:
        :return: 得到指定section的所有option
        """
        value = None
        try:
            value = self.cf.options(section)
        except configparser.NoSectionError:
            return value
        return value

    def get_items(self, section):
        """
        :param section:
        :return: 得到指定section的所有键值对
        """
        value = None
        try:
            value = self.cf.items(section)
        except configparser.NoSectionError:
            return value
        return value

    def add_section(self, section):
        """
        :param section: 添加一个新的section
        :return:
        """
        try:
            self.cf.add_section(section)
            self.cf.write(open(CONFDIR, "w"))
        except FileNotFoundError:
            print("No such file or directory: %s" % CONFDIR)

    def set_config(self, section, option, value):
        """
        :param section: 原有的 section
        :param option: 新增或修改 key 的 value 值
        :param value: 新的 value
        :return:
        """
        try:
            self.cf.set(section, option, value)
            self.cf.write(open(CONFDIR, "w"))
        except configparser.NoSectionError:
            print("No section: %s" % section)

    def remove_section(self, section):
        """
        :param section: 删除一个 section
        :return:
        """
        try:
            self.cf.remove_section(section)
            self.cf.write(open(CONFDIR, "w"))
        except FileNotFoundError:
            print("No such file or directory: %s" % CONFDIR)

    def remove_option(self, section, option):
        """
        :param section: 原有的 section
        :param option: 要删除的 option
        :return:
        """
        try:
            self.cf.remove_option(section, option)
            self.cf.write(open(CONFDIR, "w"))
        except configparser.NoSectionError:
            print("No section: %s" % section)


if __name__ == "__main__":
    config = Config()
    print(config.get_config('MySql', 'host'))
    print(config.get_sections())
    print(config.get_items('project'))
    print(config.get_config_int('MySql', 'port'))

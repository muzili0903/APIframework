# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/31 12:16
@file    :scriptOperation.py
"""
import logging

from com.util.caseOperation import get_scene
from com.util.fileOperation import get_all_file, get_file_name
from com.util.getFileDirs import APISCENE, TESTCASES


def write_pytest_header(path):
    """
    写pytest文件头部
    :param path: pytest文件保存的路径
    :return:
    """
    with open(path, "w", encoding='utf-8') as f_write:
        f_write.writelines("""#!/usr/bin/python\n# -*- coding: UTF-8 -*-\n# author: muzili\n""")
        f_write.write("import logging\n")
        f_write.write("import allure\n")
        f_write.write("import pytest\n\n")
        f_write.write("from com.core.checkResult import check_res\n")
        f_write.write("from com.core.initializeParam import ini_package\n")
        f_write.write("from com.core import reqSends\n")
        f_write.write("from com.core import reqSend\n\n")


def write_pytest_content(path, function_name, test_case):
    """
    写pytest文件内容
    :param path:
    :param function_name: 函数名
    :param test_case: 案例数据
    :return:
    """
    test_case = 'test_case = ' + str(test_case)
    content = """
\n
@pytest.mark.parametrize("test_case", test_case)
@allure.story("test_{function_name}")
def test_{function_name}(login_manage, test_case):
    api_name = list(test_case.keys())[0]
    api_content = list(test_case.values())[0]
    api_step = list(api_content.keys())[0]
    api_step_content = list(api_content.values())[0]
    test_info = api_step_content['script']
    test_data = api_step_content['data']
    expect_data = test_info.get('check_body')
    api_info = ini_package(test_info, test_data)
    if api_info.get('is_login'):
        request = login_manage
        result = reqSends.requestSend(request, api_step, api_name, api_info)
    else:
        result = reqSend.requestSend(api_step, api_name, api_info)
    assert True == check_res(result, expect_data)
    """.format(function_name=function_name)
    with open(path, "a+", encoding='utf-8') as f_write:
        f_write.writelines(test_case)
        f_write.writelines(content)


def write_pytest_tail(path, file_name):
    """
    写pytest文件尾部
    :param path: pytest文件保存的路径
    :param file_name:
    :return:
    """
    with open(path, "a+", encoding='utf-8') as f_write:
        f_write.writelines("""\n\n""")
        f_write.writelines("""if __name__ == '__main__':\n""")
        f_write.writelines("    pytest.main(['-v', './{}'])\n".format(file_name))


def write_scene_script(path):
    """
    获取场景文件
    :param path:
    :return:
    """
    scene_all_list = get_scene(path)
    for scene_list in scene_all_list:
        for key_scene, scene in scene_list.items():
            for key, value in scene.items():
                # 场景文件名 + 场景名
                scene_file_name = 'test_' + key_scene.split('.')[0] + '_' + key.capitalize()
                yield [scene_file_name, key, value]


def write_script(con):
    """
    写pytest脚本文件
    :param con:
    :return:
    """
    scene_script = write_scene_script(APISCENE)
    # 获取已存在的pytest脚本文件
    test_cases = get_all_file(TESTCASES)
    test_cases_file = list()
    for cases in test_cases:
        if cases.endswith('.py'):
            cases_file_name = get_file_name(cases).split('.')[0]
            test_cases_file.append(cases_file_name)
    while True:
        try:
            script_file_name, function_name, contents = scene_script.__next__()
            # 存在的pytest脚本文件不重新生成
            if not con.get_config('TESTCASES', 'exist_script_refresh').capitalize() \
                    and script_file_name in test_cases_file:
                pass
            else:
                test_file_name = TESTCASES + script_file_name + '.py'
                write_pytest_header(test_file_name)
                write_pytest_content(test_file_name, function_name, contents)
                write_pytest_tail(test_file_name, script_file_name)
        except StopIteration:
            break


if __name__ == "__main__":
    from com.util.getConfig import Config

    con = Config()
    write_script(con)
    # print(not con.get_config('TESTCASES', 'exist_script_refresh').capitalize())
    pass

"""
@Time ： 2022/5/18 22:03
@Auth ： muzili
@File ： getFileDirs.py
@IDE  ： PyCharm
"""
import os

# 基本路径
dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 测试案例路径
CASE = os.path.join(dir, 'case')
# 配置文件
CONFDIR = os.path.join(dir, 'config\\APIframework.ini')
# 接口API文件
API = os.path.join(dir, 'api')
# 接口json文件
APIJSON = os.path.join(dir, 'api\\json')
# 接口yaml文件
APIYAML = os.path.join(dir, 'api\\yaml')
# 报告文件
REPORT = os.path.join(dir, 'reports')
# 测试文件
TESTCASES = os.path.join(dir, 'testCases\\')
# 日志文件
LOGS = os.path.join(dir, 'logs')

if __name__ == "__main__":
    print(LOGS)
    pass

"""
@Time ： 2022/5/18 22:03
@Auth ： muzili
@File ： getFileDirs.py
@IDE  ： PyCharm
"""
import os

# 基本路径
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试案例路径
DATADIR = os.path.join(dir, 'datas')
# 配置文件
CONFDIR = os.path.join(dir, 'configs\\config.ini')
# 浏览器驱动文件
BROWSERDRIVER = os.path.join(dir, 'drivers')
# 截图文件
SCREENSHOTS = os.path.join(dir, 'results\\screenpicture')
# 报告文件
REPORT = os.path.join(dir, 'results\\reports')
# 测试文件
TESTS = os.path.join(dir, 'tests\\')
# 业务文件路径
SCRIPTS = os.path.join(dir, 'scripts')
# 日志文件
LOGS = os.path.join(dir, 'logs')
print(LOGS)

if __name__ == "__main__":
    pass

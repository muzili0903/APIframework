"""
@Time ： 2022/9/13 19:45
@Auth ： muzili
@File ： replaceData.py
@IDE  ： PyCharm
"""
import re
from functools import lru_cache

from kazoo.client import KazooClient
from urllib.parse import unquote
import telnetlib
import json
import urllib
import random
import sys
import os
from functools import reduce

sys.path.append(reduce(lambda x, _: os.path.dirname(x), list(range(1, 4)), __file__))


class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'
    coding = 'utf-8'

    def __init__(self, host=None, port=0, timeout=10):
        super().__init__(host, port, timeout)
        self.write(b'\n')

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data

    def invoke(self, service_name, method_name, arg):
        arg_str = None

        if isinstance(arg, (dict, list)):
            arg_str = json.dumps(arg)
        if isinstance(arg, tuple):
            arg_str = str(arg).replace("(", "").replace(")", "")

        command_str = "invoke {0}.{1}({2})".format(service_name, method_name, arg_str)

        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = data.decode("GBK", errors='ignore').split('\n')
        return data

    def queryDTO(self, service_name, method_name):
        command_str = f"ls -l {service_name}"

        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = data.decode("utf-8", errors='ignore').split('\n')
        print('Dto', data)
        for i in data:
            if method_name in i:
                p = re.compile(r'[(](.*?)[)]', re.S)  # 最小匹配
                dto = re.findall(p, i)
        if len(dto) == 1:
            return dto[0]


class DubboUtils(object):
    # 初始化传入zk_service地址，interface服务类路径
    def __init__(self, zk_service, interface):
        self.zk_service = zk_service
        self.interface = interface

    @lru_cache(maxsize=10)
    def _get_dubbo(self, server_name):
        """
        获取单个dubbo服务
        :param server_name:服务名
        :return:{"service": service, "paths": paths, "method": method}
        """
        zk = KazooClient(hosts="{}".format(self.zk_service))
        zk.start()
        urls = []
        # 获取zk注册的全部dubbo服务
        service_list = zk.get_children("dubbo")
        # 迭代判断调用的服务是否在注册的全部dubbo服务里
        for i in service_list:
            if server_name in i:
                try:
                    # 获取服务发布方
                    providers = zk.get_children(
                        "/dubbo/{}/providers".format(i))
                    if providers:
                        for provider in providers:
                            url = urllib.parse.unquote(provider)
                            if url.startswith('dubbo:'):
                                urls.append(url.split('dubbo://')[1])
                except Exception as e:
                    print(f"异常：{e}")
        paths = []
        for i in urls:
            try:
                # 切割获取服务方ip，端口
                path, temp = i.split('/', 1)
                # 切割获取服务类
                service = temp.split('?')[0]
                # 切割获取全部方法
                method = temp.split('methods=')[1].split('&')[0].split(',')
                paths.append(path)
            except Exception as e:
                print(f"异常：{e}")
                return None
        services = {"service": service, "paths": paths, "method": method}
        return services

    def requests_dubbo(self, method, param):
        """
        请求dubbo接口
        :param method: dubbo接口的方法
        :param param: 请求参数
        :return:
        """
        res = self._get_dubbo(self.interface)

        if res == None:
            return {"result": "fail", "data": "该service查询不到对应的信息"}
        else:
            # 判断调用方法是否在服务方提供的方法中
            methods = res.get("method")
            if method not in methods:
                raise NameError(f"{method} not in {methods}")

            paths = res.get("paths")
            # 如果服务方有多节点，随机取其中一个
            if len(paths) > 1:
                paths = paths[random.randint(0, len(paths) - 1)]
                # paths = paths[-1]
            else:
                paths = paths[0]

            ip, port = paths.split(":")

            con = Dubbo(ip, port)
            result = con.invoke(service_name=self.interface, method_name=method, arg=param)

            try:
                return {"result": "success", "data": json.loads(result[0])}
            except Exception as e:
                return {"result": e, "data": result}


class DubboRun:
    def __init__(self):
        # 从环境配置文件获取zk地址
        self.zkAddress = get_config("dubbo", "zk")

    def run(self, service, method, paramtype, params):
        """
        service-> 服务
        method->方法
        paramtype-> 入参类型 （不写这个参数 可能导致找不到该method的错误）
        params-> 入参
        """
        params["class"] = paramtype
        # logger.info(f"服务类:{service}")
        # logger.info(f"方法:{method}")
        # logger.info(f"参数类型:{paramtype}")
        # logger.info(f"请求报文:{params}")
        myDubbo = DubboUtils(self.zkAddress, service)
        res = myDubbo.requests_dubbo(method, params)
        # logger.info(f"响应报文:{res}")
        return res


if __name__ == '__main__':
    service = "com.midea.jr.gfp.gbep.api.bill.instruct.service.BillSaveInstructionsService"
    dto = "com.midea.jr.gfp.gbep.api.base.Request"
    dubboApi = "saveApproveInstruct"
    params = {
        "data": {
            "class": "com.midea.jr.gfp.gbep.api.bill.instruct.bo.BillApproveBO",
            "acceptAmt": 80.41,
            "accepterAccNo": "0",
            "accepterCnaps": "907581000070",
            "accepterName": "美的集团财务有限公司",
            "bailRate": 0,
            "batchNo": "0000276278",
            "batchNum": 1,
            "billAttr": "2",
            "billCode": "0000276279",
            "billNo": "0000276279",
            "billSerialNumber": "PZLWH07095304",
            "billType": "AC01",
            "drawerAccNo": "1011100758233011",
            "drawerCnaps": "907581000070",
            "drawerName": "广东美的制冷设备有限公司",
            "drawerOrgId": "72547107-X",
            "drawerType": "RC01",
            "dueDate": 1653926400000,
            "duePayPromise": "CC00",
            "issueDate": 1653494400000,
            "orgCode": "100758",
            "originalApplyNo": "EDROP07095305",
            "payInCautionAcctNo": "1115610075805001",
            "payeeAccNo": "1115610075701002",
            "payeeCnaps": "907581000070",
            "payeeName": "广东美的制冷设备有限公司",
            "receivedKey": "3d5c1809128443ccb90af149490ed5ac",
            "sourceReceiptNo": "PKPSL07095305",
            "sourceSystemCode": "GEBL",
            "transFlag": "EM00"
        },
        "registerCode": "piaoju111",
        "systemCode": "GEBL"
    }
    resp = DubboRun().run(service=service, method=dubboApi, paramtype=dto, params=params)
    print(resp)

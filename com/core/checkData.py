# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/26 12:24
@file    :checkData.py
"""
import logging

# from com.core import replaceData
from com.core.replaceData import query_db


def check_code(response_code: int, expect_code: int) -> bool:
    """
    校验响应码
    :param response_code:
    :param expect_code:
    :return:
    """
    if response_code != expect_code:
        logging.info("请求状态码校验不通过: 预期code: >>>{} 实际code: >>>{}".format(response_code,
                                                                      expect_code))
        return False
    else:
        return True


def check_type(type: str) -> bool:
    """
    检查校验方式
    :param type:
    :return:
    """
    if type not in ['perfect_match', '==', 'partial_match', 'in']:
        logging.info("预期结果校验方式不存在: >>>{}".format(type))
        return False
    else:
        return True


def check_value(respone_value, expect_value) -> bool:
    """
    校验值
    :param respone_value:
    :param expect_value:
    :return:
    """
    try:
        if isinstance(expect_value, str):
            if expect_value != str(respone_value):
                return False
        elif isinstance(expect_value, int):
            if expect_value != int(respone_value):
                return False
        elif isinstance(expect_value, float):
            if expect_value != float(respone_value):
                return False
        else:
            if expect_value != respone_value:
                return False
        return True
    except Exception as e:
        logging.info("值校验, 预期结果: >>>{}与响应结果: >>>{}值不一致".format(expect_value, respone_value))
        logging.info("值校验报错: >>>{}".format(e))
        return False


def check_list(response_body: list, expected_body: list, checked_type) -> bool:
    """
    校验列表字段值
    :param response_body: 响应结果
    :param expected_body: 预期结果
    :param checked_type: 校验值的方式
    :return:
    """
    result = list()
    if checked_type in ['perfect_match', '==']:
        if response_body.__len__() != expected_body.__len__():
            return False
    try:
        response_body.sort()
        expected_body.sort()
    except Exception as e:
        logging.info("'<' not supported between instances of 'dict' and 'int'")
        logging.info("list排序报错：>>>{}".format(e))
    try:
        for index, value in enumerate(expected_body):
            print(index, value)
            if isinstance(value, dict):
                result.append(check_resp(response_body[index], value, checked_type))
                # response_body.remove(value)
                # expect_body.remove(value)
            elif isinstance(value, list):
                result.append(check_list(response_body[index], value, checked_type))
                # 这两行代码是否需要删除？
                # response_body.remove(value)
                # expect_body.remove(value)
            else:
                result.append(check_value(response_body[index], value))
                # if str(value) == str(response_body[index]):
                #     pass
                # else:
                #     return False
                # if isinstance(value, str):
                #     if str(value) == str(response_body[index]):
                #         result = True
                #     else:
                #         result = False
                # if value in response_body:
                #     response_body.remove(value)
                #     expect_body.remove(value)
                # else:
                #     return False
                # else:
                #     if value == response_body:
                #         response_body.remove(value)
                #         expect_body.remove(value)
                #     else:
                #         result = False
        else:
            if checked_type in ['perfect_match', '==']:
                if response_body.__len__() != expected_body.__len__():
                    return False
                else:
                    pass
    except Exception as e:
        logging.info("JSON格式校验, 预期结果: >>>{}与响应结果: >>>{}值不一致".format(expected_body, response_body))
        logging.info("值校验报错: >>>{}".format(e))
        return False
    if False not in result:
        return True
    else:
        return False


def check_resp(response_body: dict, expected_body: dict, checked_type) -> bool:
    """
    校验响应报文，预期结果json文件格式
    :param response_body:
    :param expected_body:
    :param checked_type:
    :return:
    check_type: perfect_match
    expected_result: addInvoiceToConfirm_response.json
    """
    result = list()
    # resp = False
    if isinstance(expected_body, dict):
        for key, value in expected_body.items():
            if key not in response_body:
                logging.info("JSON格式校验, 关键字: >>>{}不在响应结果: >>>{}中".format(key, response_body))
                return False
            else:
                if isinstance(value, dict) and isinstance(response_body.get(key), dict):
                    # resp = check_resp(value, response_body.get(key), check_type)
                    result.append(check_resp(response_body.get(key), value, checked_type))
                elif not isinstance(value, type(response_body.get(key))):
                    logging.info(
                        "JSON格式校验, 关键字: >>>{}预期结果: >>>{}与响应结果: >>>{}类型不符".format(key, value, response_body.get(key)))
                    return False
                else:
                    if isinstance(value, list):
                        # resp = check_list(response_body.get(key), value, check_type)
                        result.append(check_list(response_body.get(key), value, checked_type))
                    else:
                        result.append(check_value(response_body.get(key), value))
    else:
        logging.info("JSON校验内容非dict格式: >>>{}".format(expected_body))
        return False
    if False not in result:
        return True
    else:
        return False


def check_db(checked_sql: list, expected_body: dict) -> bool:
    """
    数据库校验
    :param checked_sql:
    :param expected_body:
    :return:
    """
    res = list()
    sql_result = query_db(sql_list=checked_sql)
    if isinstance(expected_body, dict):
        for key, value in expected_body.items():
            for result in sql_result:
                if key in list(result.keys()) and result.__getitem__(key) is not None:
                    res.append(check_value(result.__getitem__(key), value))
                else:
                    logging.info("数据库校验, 关键字: >>>{}预期结果: >>>{}".format(key, value))
                    logging.info("数据库校验, sql查询结果: >>>{}".format(sql_result))
                    return False
    else:
        logging.info("数据库校验内容非dict格式: >>>{}".format(expected_body))
        return False
    if False not in res:
        return True
    else:
        return False


def check_one_to_many(response_body: list, expected_body):
    """
    校验预期值与实际列表值全匹配, 适用于查询结果校验
    :param response_body:
    :param expected_body:
    :return:
    """
    logging.info("响应报文: >>>{}".format(response_body))
    logging.info("预期结果: >>>{}".format(expected_body))
    logging.info("校验方式: >>>perfect_match")

    result = list()
    for response in response_body:
        if response != expected_body:
            result.append(False)
            break
    if all(result):
        return True
    else:
        return False


if __name__ == "__main__":
    # test {'test': {"test": 1}} {'test': [1]]}}
    # test = {'test': [{"test1": 2}, {"test": [33, 11]}]}
    # test1 = {'test': [{"test1": 2}, {"test": [33, 11]}]}
    # test2 = {'test1': [{"test1": [3, 11]}, {"test": 2}, [1, 2]], 'test2': "221"}
    # test3 = {'test1': [{"test1": [3, 11]}, {"test": 2}], 'test2': "221"}
    # # print(check_resp(test, test1, 'partial_match'))
    # expect_result = {'isSuccess': True, 'data': {'total': 1}}
    # response_result = {'isSuccess': True, 'errorCode': None, 'message': None, 'isPinCode': None,
    #                    'data': {'total': 1, 'pageNum': 1, 'pageSize': 10, 'pages': 1, 'hasPreviousPage': False,
    #                             'hasNextPage': False, 'rows': [
    #                            {'pageNumber': None, 'pageSize': None, 'returnflag': False, 'id': 1090036,
    #                             'bizId': 'IVMG1655265673788VTVQ', 'invoiceType': '1', 'batchNo': None, 'sysSource': 0,
    #                             'sourceRemarks': None, 'ouCode': '', 'ouName': '', 'provinceCentre': None,
    #                             'erpCustCode': '', 'recTaxpayerId': 269, 'recTaxpayerCode': '440001999999260',
    #                             'recTaxpayerName': '百鸣鸟装饰有限公司', 'recUnitAddress': '中欧',
    #                             'recFixedPhoneNumber': '13688889999', 'recBankName': '中国农商银行佛山北滘支行',
    #                             'recBankAccount': '12353154656665', 'openMan': '孙悟空', 'reviewer': '沙和尚',
    #                             'receiver': '猪八戒', 'invoiceAmt': 300.0, 'noTaxInvoiceAmt': 265.49,
    #                             'operator': 'shirui4', 'invoiceHead': 1, 'payTaxpayerId': None, 'payTaxpayerCode': '',
    #                             'payTaxpayerName': 'muzili', 'payUnitAddress': '220610',
    #                             'payFixedPhoneNumber': '220610', 'payBankName': '220610', 'payBankAccount': '220610',
    #                             'mail': '220610', 'provinceCode': None, 'messagePhone': '220610', 'remarks': '220610',
    #                             'status': 3, 'invoiceId': 1492439, 'businessNos': '202206151201139953',
    #                             'createDateStartStr': None, 'createDateEndStr': None, 'createBy': 'shirui4',
    #                             'createDate': '2022-06-15 12:01:14', 'updateBy': 'system',
    #                             'updateDate': '2022-06-15 12:01:16', 'invoiceDate': None, 'autoSendFlag': 0,
    #                             'totalAmtContainTax': None, 'totalAmtNotContainTax': None, 'totalTaxAmt': 34.51,
    #                             'valid': '1', 'redFlag': '1', 'taxRule': None, 'redList': [], 'blueList': [
    #                                {'pageNumber': None, 'pageSize': None, 'returnflag': False, 'id': 1492439,
    #                                 'bizId': None, 'transId': None, 'draftId': None, 'invoiceRedBlue': None,
    #                                 'invId': None, 'invoiceType': '1', 'batchNo': '20220615120114wEJ4M2Abdw',
    #                                 'source': None, 'ouCode': '', 'ouName': '', 'provinceCentre': None,
    #                                 'erpCustCode': '', 'recTaxpayerId': None, 'recTaxpayerCode': '440001999999260',
    #                                 'recTaxpayerName': '百鸣鸟装饰有限公司', 'recUnitAddress': '中欧',
    #                                 'recFixedPhoneNumber': '13688889999', 'recBankName': '中国农商银行佛山北滘支行',
    #                                 'recBankAccount': '12353154656665', 'openMan': '孙悟空', 'reviewer': '沙和尚',
    #                                 'receiver': '猪八戒', 'invoiceAmt': 300.0, 'invoiceCode': '044001800211',
    #                                 'invoiceNo': '44501789', 'invoiceDate': '2022-06-15 12:07:09', 'checkCode': None,
    #                                 'pdfUrl': 'http://aisinogd.com:5000/InvSys_test/getPdf.html?id=eUZpS25WeTlKK3FnZlNQWEdxSUZoS0xkYTJxYzFCZGx5VEFYTHAzU2lzamw4eCtzZFFVMUlTMVAxU0xYQVpnU0NGZ29LQjBHMmpyZHc1TUZsUTNPR1hPTkh2R0cvVmxFNFppTTJKMzZGVjA9',
    #                                 'picUrl': None, 'printId': None, 'redRushId': None, 'rushBizId': None,
    #                                 'redRushCode': None, 'redRushInfoNo': None, 'operator': 'system', 'invoiceHead': 1,
    #                                 'payTaxpayerId': None, 'payTaxpayerCode': '', 'payTaxpayerName': 'muzili',
    #                                 'payUnitAddress': '220610', 'payFixedPhoneNumber': '220610',
    #                                 'payBankName': '220610', 'payBankAccount': '220610', 'mail': '220610',
    #                                 'remarks': '220610', 'status': 2, 'invoiceFailReason': '',
    #                                 'redRushFailReason': None, 'delFlag': None, 'createBy': 'system',
    #                                 'createDate': None, 'updateBy': 'system', 'updateDate': None,
    #                                 'pdfAttchmentId': None, 'pdfFileName': None, 'printedFlag': None,
    #                                 'requestChannel': None, 'deviceType': None, 'canRetry': None, 'redList': None,
    #                                 'redShowFlag': False, 'provinceCode': None, 'applyDateStartStr': None,
    #                                 'applyDateEndStr': None, 'businessNos': None, 'messagePhone': None,
    #                                 'redRushFlag': False, 'reInvoiceFlag': False, 'downloadBlueInvoiceFlag': False,
    #                                 'downloadRedInvoiceFlag': False, 'invoiceReturnFlag': False, 'ids': None,
    #                                 'allCount': None, 'allAmt': None, 'allAmtNotContainTax': None, 'allTaxAmt': None,
    #                                 'invoicePrintStatus': None, 'checkListPrintStatus': None, 'checkListMark': None,
    #                                 'blueInvoiceNo': None, 'blueInvoiceCode': None, 'filter': None, 'totalCount': None,
    #                                 'valid': False, 'pid': None, 'pbizId': None, 'invoiceHeadStr': None}],
    #                             'invoiceByHandFlag': 1, 'amount': 0, 'redStatus': None, 'printedFlag': None,
    #                             'redRushInfoNo': None, 'redBizId': None, 'requestChannel': 'HX',
    #                             'blueInvoiceCode': None, 'blueInvoiceNo': None, 'filter': None, 'totalCount': None,
    #                             'invoiceHeadStr': None}]}}
    # print(check_resp(response_result, expect_result, 'in'))
    # # bug 待解决
    # # print(check_list([{"test1": 2}, [1, 22]], [{"test1": 2}, [1, 22]], 'perfect_match'))
    # pass
    check_sql = ["select biz_detail_id, biz_id from t_invoice_to_confirm_detail where business_no = '2022061516273647'"]
    expect_body = {"biz_detail_id": "DTIVMG1655281656982XSJT0hlMGE", "biz_id": "IVMG165581656982XSJT"}
    print(check_db(check_sql, expect_body))

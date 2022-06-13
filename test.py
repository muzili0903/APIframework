# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/1 16:56
@file    :test.py
"""
import logging
import re
from time import sleep
import requests

request_header = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

url1 = r'https://efssit.midea.com/admin/'

# request = requests.session()

res1 = requests.get(url=url1, headers=request_header, verify=False)
# print(res1.status_code)
print(res1.cookies.get_dict())
# print(res1.headers)


test = {
    'url': 'https://signinuat.midea.com/login?service=https://efssit.midea.com/admin/',
    'header': {'Content-Type': 'application/x-www-form-urlencoded'},
    'data': {'username': 'libl6',
             'password': '2uQptrz/K7yEpld+sRp3vQ==',
             'execution': 'e1s1',
             '_eventId': 'submit',
             'geolocation': ''}
}

# test.get('data').update({'Cookie': res1.cookies.get_dict()})

res = requests.post(url=test.get('url'), headers=test.get('header'), data=test.get('data'), cookies=res1.cookies.get_dict())
print(res.cookies.get_dict())
print(res.status_code)
# print(res.json())

if __name__ == "__main__":
    pass

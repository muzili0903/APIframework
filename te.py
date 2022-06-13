# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/13 17:18
@file    :te.py
"""
import requests

test = {
    'url': 'https://signinuat.midea.com/login?service=https://efssit.midea.com/admin/',
    'header': {'Content-Type': 'application/x-www-form-urlencoded'},
    'data': {'username': 'libl6',
             'password': '2uQptrz/K7yEpld+sRp3vQ==',
             'execution': 'e1s1',
             '_eventId': 'submit',
             'geolocation': ''}
}

res = requests.post(url='https://signinuat.midea.com/login?service=https://efssit.midea.com/admin/', data=test.get('data'))
print(res.status_code)
print(res.cookies)
print(res.headers)
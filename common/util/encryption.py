# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/25 18:19
@file    :encryption.py
"""
import json

from cryptography.fernet import Fernet


def encrypt_password(password: str, key: str) -> str:
    # 使用AES算法对密码进行加密
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password.decode('utf-8')


def decrypt_password(encrypted_password: str, key: str) -> str:
    # 使用AES算法对密码进行解密
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode('utf-8'))
    return decrypted_password.decode('utf-8')


if __name__ == '__main__':

    class BytesEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, bytes):
                return obj.decode('utf-8')  # 将字节字符串解码为Unicode字符串
            return super().default(obj)


    """
    # 向key文件添加key或更新key的时候使用
    key = Fernet.generate_key()
    password = '12313546'
    # 将加密后的密码放在config.ini文件上
    en_password = encrypt_password(password, key)
    print(en_password)
    with open(r'E:\APIAutoTestModel\key.json', 'r') as f:
        data = json.load(f)

    # 用户名为键, key为值
    data['muzili'] = key

    with open(r'E:\cs_eis_autotest\key.json', 'w+') as f:
        json.dump(data, f, cls=BytesEncoder)
    """

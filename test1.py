# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/30 16:46
@file    :test1.py
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2584167983@qq.com"  # 用户名
mail_pass = "jctcwqoxyisuebaa"  # 授权码而非邮箱密码
receivers = ['lyh2584167983@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

msg = MIMEMultipart()  # 创建一个带附件的实例
msg["Subject"] = "Tomorrow is another day"  # 指定邮件主题
msg["From"] = mail_user  # 邮件发送人
msg["To"] = ','.join(receivers)  # 邮件接收人，如果存在多个收件人，可用join连接

# ---文字部分---
part = MIMEText("请查收，谢谢！")
msg.attach(part)

# ---附件部分---
part = MIMEApplication(open(r'E:\project\APIframework\history\20220630164851.zip', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="20220630164851.zip")
msg.attach(part)


try:
    s = smtplib.SMTP("smtp.qq.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
    s.login(mail_user, mail_pass)  # 登陆服务器
    s.sendmail(mail_user, receivers, msg.as_string())  # 发送邮件
    s.close()
except Exception as e:
    print("error:", e)

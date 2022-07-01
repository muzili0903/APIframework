# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/7/1 9:02
@file    :mailOperation.py
"""
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from com.util.fileOperation import get_file_name


def send_mail(con, file):
    """
    发送邮件
    :param con:
    :param file:
    :return:
    """
    mail_config = dict(con.get_items('mail'))
    # 设置服务器
    mail_host = eval(mail_config.get('mail_host')) or 'smtp.qq.com'
    # 发件人
    sender = eval(mail_config.get('sender')) or '2584167983@qq.com'
    # 发件人授权码而非邮箱密码
    sender_pass = eval(mail_config.get('sender_pass')) or 'jctcwqoxyisuebaa'
    # 收件人
    receivers = eval(mail_config.get('receivers')) or ['lyh2584167983@163.com']
    # 邮件主题
    subject = eval(mail_config.get('subject')) or 'auto test report'
    # 邮件内容
    content = eval(mail_config.get('content')) or '请查收'

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # 邮件主题
    msg["Subject"] = subject
    msg["From"] = sender
    # 多个收件人，可用join连接
    msg["To"] = ','.join(receivers)

    # ---文字部分---
    part = MIMEText(content)
    msg.attach(part)

    # ---附件部分---
    filename = get_file_name(file)
    part = MIMEApplication(open(file, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(part)

    logging.info("发件人: >>>{}".format(sender))
    logging.info("收件人: >>>{}".format(receivers))
    logging.info("邮件内容: >>>{}".format(content))
    logging.info("附件名称: >>>{}".format(filename))
    try:
        # 连接smtp邮件服务器,端口默认是25
        mail = smtplib.SMTP(mail_host, timeout=30)
        # 登陆服务器
        mail.login(sender, sender_pass)
        # 发送邮件
        mail.sendmail(sender, receivers, msg.as_string())
        mail.close()
    except Exception as e:
        logging.error("发送邮件失败: >>>{}".format(e))


if __name__ == "__main__":
    pass
    # from com.util.getConfig import Config
    #
    # con = Config()
    # send_mail(con, r'E:\APIframework\history\20220701091434.zip')

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

sender = 'qhyy@mail.zhucx.top'    # 发件人邮箱账号

receivers = ('56240949@qq.com;linna0129@163.com')  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receiver = receivers.split(';')

def mail():
    ret = True
    try:
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
        message['From'] = formataddr(["菜鸟教程",sender])   # 发送者
        message['To'] =  ",".join(receiver)        # 接收者

        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj = smtplib.SMTP('192.168.0.251')
        smtpObj.sendmail(sender, receiver, message.as_string())      
    except smtplib.SMTPException:
        ret = False
    return ret

ret = mail()

if ret :
    print ("邮件发送成功")
else:
    print ("邮件发送失败")


#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import time

# 直连外网服务器发送邮件
def SendMail(MailText):
    
    # 外网直连邮件服务器设置
    sender='qhyy@mail.zhucx.top'    # 发件人邮箱账号
    passwd = 'rF635akmhxDFX5neYUbd'              # 发件人邮箱密码
    receivers = ('56240949@qq.com;')  # 接收邮件,多邮箱用分号分割
    receiver = receivers.split(';')                    #分号切片

    try:
        msg=MIMEText(MailText,'plain','utf-8')
        msg['From']=formataddr(["From在线投诉与建议",sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        #msg['To']=formataddr(["FK",receivers])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = ",".join(receiver)
        msg['Subject']="有一个客服反馈待处理"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtpdm.aliyun.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender,receiver,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("send success")
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("error")

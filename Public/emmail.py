# -*- coding: utf-8 -*-
# @Author  : leizi
import smtplib, time, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml


def load_emil_setting():  # 从配置文件中加载获取email的相关信息
    filepath = os.path.join(os.path.join(os.getcwd(), 'config'), 'email.yaml')

    data_file = open(filepath, "r")
    datas = yaml.load(data_file, Loader=yaml.FullLoader)
    data_file.close()
    return (datas['foremail'], datas['password'], datas['toeamil'], datas['title'])


def sendemali(filepath):  # 发送email
    from_addr, password, mail_to, mail_body = load_emil_setting()
    msg = MIMEMultipart()
    msg['Subject'] = '接口自动化测试报告'
    msg['From'] = '自动化测试平台'
    msg['To'] = mail_to
    msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    att = MIMEText(open(r'%s' % filepath, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="pyresult.html"'
    txt = MIMEText("这是测试报告的邮件，详情见附件", 'plain', 'gb2312')
    msg.attach(txt)
    msg.attach(att)
    smtp = smtplib.SMTP()
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, mail_to, msg.as_string())
    server.quit()

# encoding: utf-8
"""
@author: lileilei
@file: run_http_excel_re.py
@time: 2017/6/9 12:45
"""
from  Public.pyreport_excel import create
import os,datetime
from  Public.Dingtalk import send_ding
from testCase.case import testinterface
from  Public.get_excel import datacel
def start_excel_report_http():
    m=datetime.datetime.now().strftime("%Y%m%d")
    basdir = os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '\\test_case_data\\case.xlsx'
    listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel(path)
    listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi =testinterface()
    filepath = os.path.join(basdir + '\\test_Report\\%s-result.xls'%m)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    create(filename=filepath,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey,listconeents=listconeent, listfangshis=listfangshi, listqiwangs=listqiwang,
           listids=listid, listrelust=listrelust, listnames=listname)
    contec = 'dubbo接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    list_pass, list_fail, list_exption, list_weizhi, filepath)
    send_ding(content=contec)
if __name__ == '__main__':
    start_excel_report_http()
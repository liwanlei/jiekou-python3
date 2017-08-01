# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: main_excel_report.py
@time: 2017/6/9 12:45
"""
from  Public.pyreport_excel import create
import unittest,os,threading,datetime
from testCase.test_case import testinterface
from Public.emmail import  sendemali
from  Public.get_excel import datacel
def start():
    listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel()
    listrelust,list_fail, list_pass, list_json =testinterface()
    filepath =r'C:\Users\Administrator\Desktop\xuexi\jiejko\test_Report\relult.xls'
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    create(filename=filepath,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey,listconeents=listconeent, listfangshis=listfangshi, listqiwangs=listqiwang,
           listids=listid, listrelust=listrelust, listnames=listname)
def teThread():
    st = datetime.datetime.now()
    m = threading.Thread(target=start, args=())
    m.run()
    end = datetime.datetime.now()
    print(end - st)
if __name__ == '__main__':
    start()
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
from testCase.test_case import Testinface
from Public.emmail import  sendemali
def start():
    suite = unittest.TestSuite()
    suite.addTest(Testinface("testinterface"))
    me=Testinface()
    list_fail, list_pass, list_json, listurls, listkeys, listconeents, listfangshis, listqiwangs, listids, listrelust, listnames=me.testinterface()
    filepath =r'C:\Users\Administrator\Desktop\jiejko\test_Report\relult.xls'
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    create(filepath,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurls, listkeys=listkeys,listconeents=listconeents, listfangshis=listfangshis, listqiwangs=listqiwangs, listids=listids, listrelust=listrelust, listnames=listnames)
    # sendemali(filepath)
def testThread():
    st = datetime.datetime.now()
    m = threading.Thread(target=start, args=())
    m.run()
    end = datetime.datetime.now()
    print(end - st)


if __name__ == '__main__':
    testThread()
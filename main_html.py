# -*- coding: utf-8 -*-
# @Author  : leizi
import unittest,os,datetime,time
from testCase.test_case import Testinface
from Public.py_Html import createHtml
from  Public.emmail import  sendemali
import  threading
def stast():
    starttime=datetime.datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(Testinface("testinterface"))
    me=Testinface()
    list_fail, list_pass, list_json, listurls, listkeys, listconeents, listfangshis, listqiwangs, listids, listrelust, listnames=me.testinterface()
    filepath =r'C:\Users\Administrator\Desktop\jiejko\test_Report\relult.html'
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime=datetime.datetime.now()
    createHtml(titles='接口测试报告',filepath=filepath,starttime=starttime,endtime=endtime,passge=list_pass,fail=list_fail,id=listids,name=listnames,key=listkeys,coneent=listconeents,url=listurls,meth=listfangshis,yuqi=listqiwangs,json=list_json,relusts=listrelust)
    # sendemali(filepath)
def testThread():
    st=datetime.datetime.now()
    m=threading.Thread(target=stast,args=())
    m.run()
    end=datetime.datetime.now()
    print(end-st)
if __name__ == '__main__':
    testThread()





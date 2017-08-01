# -*- coding: utf-8 -*-
# @Author  : leizi
import unittest,os,datetime,time
from testCase.test_case import testinterface
from Public.py_Html import createHtml
from Public.get_excel import datacel
from  Public.emmail import  sendemali
import  threading
def stast():
    starttime=datetime.datetime.now()
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel()
    listrelust, list_fail, list_pass, list_json = testinterface()
    filepath =r'C:\Users\Administrator\Desktop\xuexi\jiejko\test_Report\relult.html'
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime=datetime.datetime.now()
    createHtml(titles='接口测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust)
    # sendemali(filepath)
def tThread():
    st=datetime.datetime.now()
    m=threading.Thread(target=stast,args=())
    m.run()
    end=datetime.datetime.now()
if __name__ == '__main__':
    tThread()





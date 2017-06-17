# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @Site    : 
# @File    : test_case.py
# @Software: PyCharm
import unittest
from  Interface.testFengzhuang import TestApi
from  Public.get_excel import datacel
from  Public.tsest_log import log_re
listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel()
title='测试日志'
log_can=log_re(title)
class Testinface(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testinterface(self):
        list_pass = 0
        list_fail = 0
        list_json = []
        listrelust=[]
        listurls=[]
        listkeys=[]
        listids=[]
        listconeents=[]
        listfangshis=[]
        listqiwangs=[]
        listnames=[]
        for i in range(len(listurl)):
            api=TestApi(url=listurl[i],key=listkey[i],connent=listconeent[i],fangshi=listfangshi[i])
            apicode=api.getcode()
            apijson=api.getJson()
            log_can.info_log('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s'%(listconeent[i],listurl[i],apijson,listqiwang[i]))
            if apicode==int(listqiwang[i]):
                listids.append(listid[i])
                listurls.append(listurl[i])
                listkeys.append(listkey[i])
                listconeents.append(listconeent[i])
                listfangshis.append(listfangshi[i])
                listqiwangs.append(listqiwang[i])
                listnames.append(listname[i])
                list_json.append((apijson))
                listrelust.append('pass')
                list_pass += 1
            else:
                listids.append(listid[i])
                listurls.append(listurl[i])
                listkeys.append(listkey[i])
                listconeents.append(listconeent[i])
                listfangshis.append(listfangshi[i])
                listqiwangs.append(listqiwang[i])
                listnames.append(listname[i])
                list_fail+=1
                listrelust.append('fail')
                list_json.append((apijson))
        return  list_fail,list_pass,list_json,listurls,listkeys,listconeents,listfangshis,listqiwangs,listids,listrelust,listnames

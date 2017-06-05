# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @Site    : 
# @File    : ceshiyongli.py
# @Software: PyCharm
import unittest,os
from  Public import BSTestRunner
from  Interface.get_excel import datacel
from  Interface.testFengzhuang import TestApi
listid,listkey,listconeent,listurl,listfangshi,listqiwang=datacel()

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
        for i in range(len(listurl)):
            api=TestApi(url=listurl[i],key=listkey[i],connent=listconeent[i],fangshi=listfangshi[i])
            apicode=api.getcode()
            apijson=api.getJson()
            if apicode==int(listqiwang[i]):
                list_json.append((apijson))
                listrelust.append('pass')
                list_pass += 1
            else:
                list_fail+=1
                listrelust.append('fail')
                list_json.append((apijson))
        return  list_fail,list_pass,list_json
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
listkey,listconeent,listurl,listfangshi,listqiwang=datacel()
class Testinface(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testinterface(self):
        for i in range(len(listurl)):
            api=TestApi(url=listurl[i],key=listkey[i],connent=listconeent[i],fangshi=listfangshi[i])
            apicode=api.getcode()
            apijson=api.getJson()
            if apicode==int(listqiwang[i]):
                print('%s:测试成功。json数据为:%s'%(i + 1 ,apijson))
            else:
                print('%s:测试失败.json数据为:%s'%(i + 1 ,apijson))

# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @File    : case.py
from  Interface.testFengzhuang import TestApi
from  Public.get_excel import datacel
from  Public.log import LOG,logger
listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel()
from Public.panduan import assert_in
@logger('测试')
def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust=[]
    list_weizhi=0
    list_exption=0
    for i in range(len(listurl)):
        api=TestApi(url=listurl[i],key=listkey[i],connent=listconeent[i],fangshi=listfangshi[i])
        apijson=api.getJson()
        if apijson['code']==0:
            LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s'%(listconeent[i],listurl[i],apijson,listqiwang[i]))
            assert_re=assert_in(asserqiwang=listqiwang[i],fanhuijson=apijson)
            if assert_re['code']==0:
                list_json.append(apijson['result'])
                listrelust.append('pass')
                list_pass += 1
            elif assert_re['code']==1:
                list_fail+=1
                listrelust.append('fail')
                list_json.append(apijson['result'])
            elif assert_re['code']==2:
                list_exption+=1
                listrelust.append('exception')
                list_json.append(assert_re['result'])
            else:
                list_weizhi+=1
                listrelust.append('未知错误')
                list_json.append('未知错误')
        else:
            list_exption += 1
            listrelust.append('exception')
            list_json.append(apijson['result'])
            continue
    return  listrelust,list_fail,list_pass,list_json,list_exption,list_weizhi
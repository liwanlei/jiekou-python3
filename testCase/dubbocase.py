""" 
@author: lileilei
@file: dubbocase.py 
@time: 2018/3/29 12:47 
"""
from Interface.dubbo_feng import DubboInterface
from public.log import LOG, logger
from public.panduan import assert_in
from public.get_excel import datacel
import os

path = os.path.join(os.path.join(os.getcwd(), 'test_case_data'), 'dubbocase.xlsx')
listid, listurl, listinterface, listmeth, listfobject, listparam, listassert = datacel(path)


@logger('dubbo接口测试')
def testdubbointerface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    list_weizhi = 0
    list_exption = 0
    for i in range(len(listid)):
        dubboapi = DubboInterface(url=listurl, interface=listinterface[i], method=listmeth[i], param=listfobject[i],
                                  **(eval(listparam[i])))
        dubboapireslu = dubboapi.getresult()
        if dubboapireslu['code'] == 0:
            LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listparam[i], listurl[i], dubboapireslu, listassert[i]))
            assert_re = assert_in(asserassert=listassert[i], returnjson=dubboapireslu)
            if assert_re['code'] == 0:
                list_json.append(dubboapireslu['result'])
                listrelust.append('pass')
                list_pass += 1
            elif assert_re['code'] == 1:
                list_fail += 1
                listrelust.append('fail')
                list_json.append(dubboapireslu['result'])
            elif assert_re['code'] == 2:
                list_exption += 1
                listrelust.append('exception')
                list_json.append(assert_re['result'])
            else:
                list_weizhi += 1
                listrelust.append('未知错误')
                list_json.append('未知错误')
        else:
            list_exption += 1
            listrelust.append('exception')
            list_json.append(dubboapireslu['result'])
            continue
        return listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi

# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @File    : case.py
from Interface.testFengzhuang import TestApi
from public.get_excel import datacel
from public.log import LOG, logger
import os
from config.config import Config_Try_Num, TestPlanUrl

path = os.path.join(os.path.join(os.getcwd(), 'test_case_data'), 'case.xlsx')

listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path)
from public.panduan import assert_in


@logger('测试')
def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    list_weizhi = 0
    list_exption = 0
    error_num = 0
    for i in range(len(listurl)):
        while error_num <= Config_Try_Num + 1:
            parem = {'key': listkey[i]}
            parem.update({'info': eval(listconeent[i])})
            #parem=eval(data_test[listconeent[i])
            api = TestApi(url=TestPlanUrl + listurl[i], parame=parem, method=listfangshi[i])
            apijson = api.getJson()
            if apijson['code'] == 0:
                LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listconeent[i], listurl[i], apijson, listqiwang[i]))
                assert_re = assert_in(asserassert=listqiwang[i], returnjson=apijson)
                if assert_re['code'] == 0:
                    list_json.append(apijson['result'])
                    listrelust.append('pass')
                    list_pass += 1
                    error_num = 0
                    continue
                elif assert_re['code'] == 1:
                    if error_num <= Config_Try_Num:
                        error_num += 1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num = 0
                        list_fail += 1
                        listrelust.append('fail')
                        list_json.append(apijson['result'])
                        break
                elif assert_re['code'] == 2:
                    if error_num < Config_Try_Num:
                        error_num += 1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num = 0
                        list_exption += 1
                        listrelust.append('exception')
                        list_json.append(assert_re['result'])
                        break
                else:
                    if error_num < Config_Try_Num:
                        error_num += 1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num = 0
                        list_weizhi += 1
                        listrelust.append('未知错误')
                        list_json.append('未知错误')
                        break
            else:
                if error_num < Config_Try_Num:
                    error_num += 1
                    LOG.info('失败重试中')
                else:
                    LOG.info('失败重试中次数用完，最后结果')
                    error_num = 0
                    list_exption += 1
                    listrelust.append('exception')
                    list_json.append(apijson['result'])
                    break
    return listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi

# -*- coding: utf-8 -*-
# @Author  : leizi
import os, datetime, time
from testCase.case import testinterface
from public.py_Html import createHtml
from public.get_excel import datacel
from public.create_report import save_result
import threading


def stast():
    starttime = datetime.datetime.now()
    day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    path = os.path.join(os.path.join(os.getcwd(), 'test_case_data'), 'case.xlsx')
    basdir = os.path.abspath(os.path.dirname(__file__))
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path)
    listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi = testinterface()
    filepath = os.path.join(os.path.join(basdir, 'test_Report'), '%s-result.html' % day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    save_result(starttime, len(listrelust), ((list_pass)), list_fail)
    endtime = datetime.datetime.now()
    createHtml(titles='接口测试报告', filepath=filepath, starttime=starttime,
               endtime=endtime, passge=list_pass, fail=list_fail,
               id=listid, name=listname, key=listkey, coneent=listconeent, url=listurl, meth=listfangshi,
               yuqi=listqiwang, json=list_json, relusts=listrelust, exceptions=list_exption, weizhi=list_weizhi)
    # sendemali(filepath)


def tThread():
    m = threading.Thread(target=stast, args=())
    m.run()


if __name__ == '__main__':
    tThread()

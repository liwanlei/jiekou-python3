# encoding: utf-8
"""
@author: lileilei
@file: run_excel_re.py
@time: 2017/6/9 12:45
"""
from public.pyreport_excel import create
import os, threading, datetime
from testCase.case import testinterface
from public.get_excel import datacel
from public.create_report import save_result


def start():
    starttime = datetime.datetime.now()
    mtime = datetime.datetime.now().strftime("%Y%m%d")
    basdir = os.path.abspath(os.path.dirname(__file__))

    path = os.path.join(os.path.join(os.getcwd(), 'test_case_data'), 'case.xlsx')
    listid, listkey, listconeent, listurl, listmethod, listqiwang, listname = datacel(path)
    listrelust, list_fail, list_pass, list_json, list_weizhi, listone = testinterface()
    filepath = os.path.join(os.path.join(basdir, 'test_Report'), '%s-result.xls' % mtime)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    save_result(starttime, len(listrelust), ((list_pass)), list_fail)
    create(filename=filepath, list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey, listconeents=listconeent, listfangshis=listmethod,
           listqiwangs=listqiwang,
           listids=listid, listrelust=listrelust, listnames=listname)


def teThread():
    m = threading.Thread(target=start, args=())
    m.run()


if __name__ == '__main__':
    teThread()

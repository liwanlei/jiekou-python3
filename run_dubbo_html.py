# -*- coding: utf-8 -*-
# @Author  : leizi
import os,datetime,time
from testCase.dubbocase import testdubbointerface
from Public.py_Html import createHtml
from Public.get_excel import datacel
from Public.create_report import save_result
def stast():
    starttime=datetime.datetime.now()
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir=os.path.abspath(os.path.dirname(__file__))
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel()
    listrelust, list_fail, list_pass, list_json,list_exption,list_weizhi = testdubbointerface()
    filepath =os.path.join(basdir+'\\test_Report\\%s-result.html'%day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    save_result(starttime,len(listrelust),((list_pass)),list_fail)
    endtime=datetime.datetime.now()
    createHtml(titles='dubbo接口测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)
if __name__ == '__main__':
    stast()
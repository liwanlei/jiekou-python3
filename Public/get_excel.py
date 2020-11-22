# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
import xlrd,os
from Public.log import LOG, logger


# @logger('解析测试用例文件')
def datacel(filrpath):
    try:
        file = xlrd.open_workbook(filrpath)
        me = file.sheets()[0]
        nrows = me.nrows
        listid = []
        listkey = []
        listconeent = []
        listurl = []
        listfangshi = []
        listqiwang = []
        listrelut = []
        listname = []
        for i in range(1, nrows):
            listid.append(me.cell(i, 0).value)
            listkey.append(me.cell(i, 2).value)
            listconeent.append(me.cell(i, 3).value)
            listurl.append(me.cell(i, 4).value)
            listname.append(me.cell(i, 1).value)
            listfangshi.append((me.cell(i, 5).value))
            listqiwang.append((me.cell(i, 6).value))
        return listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s' % e)
        return
@logger('生成数据驱动所用数据')
def makedata():
    path = os.getcwd() + '//test_case_data//case.xlsx'
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname=datacel(path)
    i=0
    make_data=[]
    for i in range(len(listid)):
        make_data.append({'url':listurl[i],'key':listkey[i],'coneent':listconeent[i],'fangshi':listfangshi[i],'qiwang':listqiwang[i]})
        i+=1
    return make_data

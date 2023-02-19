# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
import xlrd, os
from public.log import LOG, logger


@logger('解析测试用例文件')
def datacel(filepath):
    try:
        file = xlrd.open_workbook(filepath)
        print(file)
        rslut = file.sheets()[0]
        nrows = rslut.nrows
        listid = []
        listkey = []
        listconeent = []
        listurl = []
        listmethod = []
        listassert = []
        listname = []
        for i in range(1, nrows):
            listid.append(rslut.cell(i, 0).value)
            listkey.append(rslut.cell(i, 2).value)
            listconeent.append(rslut.cell(i, 3).value)
            listurl.append(rslut.cell(i, 4).value)
            listname.append(rslut.cell(i, 1).value)
            listmethod.append((rslut.cell(i, 5).value))
            listassert.append((rslut.cell(i, 6).value))
        return listid, listkey, listconeent, listurl, listmethod, listassert, listname
    except Exception as e:
        print(e)
        LOG.info('打开测试用例失败，原因是:%s' % e)
        return


@logger('生成数据驱动所用数据')
def makedata():
    path = os.path.join(os.path.join(os.getcwd(), 'test_case_data'), 'case.xlsx')
    listid, listkey, listconeent, listurl, listmethod, listassert, listname = datacel(path)
    make_data = []
    for i in range(len(listid)):
        make_data.append({'url': listurl[i], 'key': listkey[i],
                          'coneent': listconeent[i], 'method': listmethod[i],
                          'assertconnect': listassert[i],
                          'id': listid[i]},
                         )
        i += 1
    return make_data

# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
# @Software: PyCharm
import xlrd,xlwt
import unittest,sys
from xlutils.copy import copy
from Interface.test_requests import reques
def datacel():
	filepath='.\\test_Data\\test_Data.xlsx'
	file=xlrd.open_workbook(filepath)
	me=file.sheets()[0]
	nrows=me.nrows
	listid=[]
	listkey=[]
	listconeent=[]
	listurl=[]
	listfangshi=[]
	listqiwang=[]
	listrelut=[]
	listname=[]
	for i in range(1,nrows):
		listid.append(me.cell(i,0).value)
		listkey.append(me.cell(i,2).value)
		listconeent.append(me.cell(i,3).value)
		listurl.append(me.cell(i,4).value)
		listname.append(me.cell(i,1).value)
		listfangshi.append((me.cell(i,5).value))
		listqiwang.append((me.cell(i,6).value))
	return listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname
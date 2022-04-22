""" 
@author: lileilei
@file: get_excel_new.py 
@time: 2018/4/30 11:04 
"""
'''读取Excel'''
import xlrd


def datacel(filrpath):
    all_case = []
    file = xlrd.open_workbook(filrpath)
    me = file.sheets()[0]
    nrows = me.nrows
    for i in range(1, nrows):
        all_case.append({"id": me.cell(i, 0).value, 'key': me.cell(i, 2).value,
                         'coneent': me.cell(i, 3).value, 'url': me.cell(i, 4).value,
                         'name': me.cell(i, 1).value, 'fangshi': me.cell(i, 5).value,
                         'assert': me.cell(i, 6).value})
    return all_case

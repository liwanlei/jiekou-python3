# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: pyreport_excel.py
@time: 2017/6/7 8:47
"""
import xlrd ,os,xlwt,yaml,xlsxwriter #导入库
from xlwt import *
def yangshi1():
    style = XFStyle()
    fnt = Font()
    fnt.name = u'微软雅黑'
    fnt.bold = True
    style.font = fnt
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment  # 给样式添加文字居中属性
    style.font.height = 430  # 设置字体大小
    return style
def yangshi2():
	style1 = XFStyle()
	alignment = xlwt.Alignment()
	alignment.horz = xlwt.Alignment.HORZ_CENTER
	alignment.vert = xlwt.Alignment.VERT_CENTER 
	style1.alignment = alignment  # 给样式添加文字居中属性
	style1.font.height = 330  # 设置字体大小
	return style1
def yangshi3():
	style1 = XFStyle()
	style1.font.height = 330  # 设置字体大小
	return style1
def yangshique(me):
	if me =='pass':
		style=yangshi1()
		Pattern=xlwt.Pattern()
		Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
		Pattern.pattern_fore_colour=xlwt.Style.colour_map['green']
		style.pattern=Pattern
	else :
		style=yangshi2()
		Pattern=xlwt.Pattern()
		Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
		Pattern.pattern_fore_colour=xlwt.Style.colour_map['red']
		style.pattern=Pattern
	return style
def create(filename,list_pass,list_fail,listids,listnames,listkeys,listconeents,listurls,listfangshis,listqiwangs,list_json,listrelust):
    filepath = open(r'.\config\test_report.yaml', encoding='utf-8')
    file_config = yaml.load(filepath)
    file = Workbook(filename)
    table = file.add_sheet('测试结果',cell_overwrite_ok=True)
    style=yangshi1()
    for i in range(0, 7):
        table.col(i).width = 380*20
    style1=yangshi2()
    table.write_merge(0,0,0,6,'测试报告',style=style)
    table.write_merge(1,1,0,6,'',style=style)
    table.write_merge(2,3,0,6,'测试详情',style=style1)
    table.write(4,0,'项目名称',style=style1)
    table.write(5,0,'接口版本',style=style1)
    table.write(6,0,'提测时间',style=style1)
    table.write(7,0,'提测人',style=style1)
    table.write(4,2,'测试人',style=style1)
    table.write(5,2,'测试时间',style=style1)
    table.write(6,2,'审核人',style=style1)
    table.write(4,4,'通过',style=style1)
    table.write(5,4,'失败',style=style1)
    table.write(6,4,'成功率',style=style1)
    table.write(4, 1, (file_config['projectname']),style=style1)
    table.write(5, 1, file_config['interfaceVersion'],style=style1)
    table.write(6, 1, file_config['tijiao_time'],style=style1)
    table.write(7, 1, file_config['tijiao_person'],style=style1)
    table.write(4, 3, file_config['ceshi_person'],style=style1)
    table.write(5, 3, file_config['ceshi_time'],style=style1)
    table.write(6, 3, file_config['shenhename'],style=style1)
    table.write(4, 5, (list_pass), style=style1)
    table.write(5, 5, (list_fail), style=style1)
    table.write(6, 5, ('%.2f%%'%((list_pass)/(len(listrelust)))), style=style1)
    table1 = file.add_sheet('测试详情',cell_overwrite_ok=True)
    table1.write_merge(0,0,0,8,'测试详情',style=style)
    for i in range(0, 8):
        table1.col(i).width = 400*20
    table1.write(1,0,'用例ID',style=yangshi3())
    table1.write(1,1,'用例名字',style=yangshi3())
    table1.write(1,2,'key',style=yangshi3())
    table1.write(1,3,'请求内容',style=yangshi3())
    table1.write(1,4,'	url',style=yangshi3())
    table1.write(1,5,'请求方式',style=yangshi3())
    table1.write(1,6,'预期',style=yangshi3())
    table1.write(1,7,'实际返回',style=yangshi3())
    table1.write(1,8,'结果',style=yangshi3())
    for i in range(len(listids)):
        table1.write(i+1, 0, listids[i],style=yangshi3())
        table1.write(i+1, 1, listnames[i],style=yangshi3())
        table1.write(i+1, 2, listkeys[i],style=yangshi3())
        table1.write(i+1, 3, listconeents[i],style=yangshi3())
        table1.write(i+1, 4, listurls[i],style=yangshi3())
        table1.write(i+1, 5, listfangshis[i],style=yangshi3())
        table1.write(i+1, 6, listqiwangs[i],style=yangshi3())
        table1.write(i+1, 7, str(list_json[i]),style=yangshi3())
        table1.write(i+1, 8, listrelust[i], style=yangshique(listrelust[i]))
    file.save(filename)
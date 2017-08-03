# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: py_Html.py
@time: 2017/6/5 17:04
"""
import  os
titles='接口测试'
def title(titles):
	title='''<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>%s</title>
		<style type="text/css">
			td{ width:40px; height:50px;}
		</style>
	</head>
	<body>
	'''%(titles)
	return title
connent='''
<div style='width: 1170px;margin-left: 15%'>
<h1>接口测试的结果</h1>'''
def time(starttime,endtime,passge,fail):
	beijing='''
		<p><strong>开始时间:</strong> %s</p>
		<p><strong>结束时间:</strong> %s</p>
		<p><strong>耗时:</strong> %s</p>
		<p><strong>结果:</strong>
			<span >Pass: <strong >%s</strong>
			Fail: <strong >%s</strong>
			        </span></p>                  
			    <p ><strong>测试详情如下</strong></p>  </div> '''%(starttime,endtime,(endtime-starttime),passge,fail)
	return beijing
shanghai='''


        <p>&nbsp;</p>
        <table border='2'cellspacing='1' cellpadding='1' width='1100'align="center" >
		<tr >
            <td ><strong>用例ID&nbsp;</strong></td>
            <td><strong>用例名字</strong></td>
            <td><strong>key</strong></td>
            <td><strong>请求内容</strong></td>
            <td><strong>url</strong></td>
            <td><strong>请求方式</strong></td>
            <td><strong>预期</strong></td>
            <td><strong>实际返回</strong></td>  
            <td><strong>结果</strong></td>
        </tr>
    '''
def passfail(tend):
    if tend =='pass':
        htl=' <td bgcolor="green">pass</td>'
    elif tend =='fail':
        htl=' <td bgcolor="fail">fail</td>'
    else:
        htl='<td bgcolor="#8b0000">error</td>'
    return htl
def ceshixiangqing(id,name,key,coneent,url,meth,yuqi,json,relust):
    xiangqing='''
        <tr>
            <td>%s</td>
            <td>%s</td>
       
            <td>%s</td>
            <td>%s
           </td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            %s
        </tr>
        
    '''%(id,name,key,coneent,url,meth,yuqi,json,passfail(relust))
    return xiangqing
weibu='''
	</table>
    </body>
    </html>'''
def relust(titles,starttime,endtime,passge,fail,id,name,key,coneent,url,meth,yuqi,json,relust):
    if type(name) ==list:
        relus=' '
        for i in range(len(name)):
            relus+=(ceshixiangqing(id[i],name[i],key[i],coneent[i],url[i],meth[i],yuqi[i],json[i],relust[i]))
        text=title(titles)+connent+time(starttime,endtime,passge,fail)+shanghai+relus+weibu
    else:
        text=title(titles)+connent+time(starttime,endtime,passge,fail)+shanghai+ceshixiangqing(id,name,key,coneent,url,meth,yuqi,json,relust)+weibu
    return text
def createHtml(filepath,titles,starttime,endtime,passge,fail,id,name,key,coneent,url,meth,yuqi,json,relusts):
	texts=relust(titles,starttime,endtime,passge,fail,id,name,key,coneent,url,meth,yuqi,json,relusts)
	with open(filepath,'wb') as f:
		f.write(texts.encode())

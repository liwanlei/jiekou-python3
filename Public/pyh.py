# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: pyh.py
@time: 2017/6/5 17:04
"""
titles='接口测试'
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

connent='''
<div style='width: 1170px;margin-left: 15%'>
<h1>接口测试的结果</h1>'''
beijing='''
    <p><strong>开始时间:</strong> %s</p>
    <p><strong>花费时间:</strong> %s</p>
    <p><strong>结果:</strong>
        <span >Pass: <strong >%s</strong>
        Fail: <strong >%s</strong>'''%(1,2,3,4)
shanghai='''
        </span></p>
    <p ><strong>测试详情如下</strong></p>
        <p>&nbsp;</p>
        <table border='2'cellspacing='1' cellpadding='1' width='1100' >
    '''
xiangqing='''<tr >
        <td ><strong>用例ID&nbsp;</strong></td>
        <td><strong>用例名字</strong></td>
        <td><strong>类型</strong></td>
        <td><strong>key</strong></td>
        <td><strong>coneent</strong></td>
        <td><strong>url</strong></td>
        <td><strong>请求方式</strong></td>
        <td><strong>预期</strong></td>
        <td><strong>结果</strong></td>
    </tr>
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s
       </td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td >%s</td>
    </tr>
    </table>
</div>
</body>
</html>'''%(1,2,3,4,5,6,7,8,8)
print(title+connent+beijing+shanghai+xiangqing)
# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 21:54:08
# @Author  : lileilei
m={
'key':'APIKEY',
'info': '今天天气怎么样',
'loc':'北京市中关村',
'userid':'123456'
}
me='userid=123456&info=今天天气怎么样'
if len(me.split('=')) > 1:
    data = me.split('&')
    result = dict([(item.split('=')) for item in data])
value1=([(m[key]) for key in result.keys()])
value2=([(value) for value in result.values()])
if value1==value2:
    print('pass')
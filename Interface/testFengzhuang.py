# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
# @Software: PyCharm
from Interface.feng import reques
reques=reques()
class TestApi(object):
	def __init__(self,url,key,connent,fangshi):
		self.url=url
		self.key=key
		self.connent=connent
		self.fangshi=fangshi
	def testapi(self):
		if self.fangshi=='POST':
			self.parem = {'key': self.key, 'info': self.connent}
			r=reques.post(self.url,self.parem)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			r = reques.post(self.url, self.parem)
		return r
	def getcode(self):
		code=self.testapi()['code']
		return code
	def getJson(self):
		json_data = self.testapi()
		return json_data
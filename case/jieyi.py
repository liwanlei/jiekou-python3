import xlrd,xlwt
import unittest,sys
from xlutils.copy import copy
from fengzhuang.feng import reques
def datacel():
	filepath='C:\\Users\\Administrator\\Desktop\\jiekou\\data\\data.xlsx'
	file=xlrd.open_workbook(filepath)
	me=file.sheets()[0]
	nrows=me.nrows
	listkey=[]
	listconeent=[]
	listurl=[]
	listfangshi=[]
	listqiwang=[]
	for i in range(1,nrows):
		listkey.append(me.cell(i,2).value)
		listconeent.append(me.cell(i,3).value)
		listurl.append(me.cell(i,4).value)
		listfangshi.append((me.cell(i,5).value))
		listqiwang.append(int(me.cell(i,6).value))
	return listkey,listconeent,listfangshi,listqiwang,listurl
class TestTuling(unittest.TestCase):
	def setup(self):
		self.listkey,self.listconeent,self.listfangshi,self.listqiwang,self.listurl=datacel()
	def tearDown(self):
		sys.exit()
	def testpost1(self):
		try:
			self.url=self.listurl[0]
			self.key=self.listkey[0]
			self.coneent=self.listconeent[0]
			self.fangshi=self.listfangshi[0]
			self.code=self.listqiwang
			self.parem={'key':self.key,'info':self.coneent}
			if self.fangshi == 'POST':
				self.me=reques.post(url=self.url,params=self.parem)
				self.assertEqual(self.me['code'],self.code,msg='接口返回标识符有误')
			else:
				print('用例1执行失败!请求方式不正确')
		except Exception as e:
			print('用例1测试失败,原因:%s'%e)

if __name__ == '__main__':
	un=unittest.TestSuite()
	un.addTest(Test_tuling('test_post1'))
	ren=unittest.runner()
	ren.run(un)
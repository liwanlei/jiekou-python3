# -*- coding: utf-8 -*-
# @Author  : leizi
import os,time,unittest
from Case.ceshiyongli import Testinface
'''
这里你可以分开执行上面你case里面包含的用例。也可以单独执行里面
的某一个的测试用例
'''
from Case.post import Test_tuling
from Public import BSTestRunner
from  Interface.emmail import sendemali
if __name__ == '__main__':
	# suite = unittest.TestSuite()
	# suite.addTest(Test_tuling("test_post4"))
	# suite.addTest(Test_tuling('test_post3'))
	# suite.addTest(Test_tuling('test_post2'))
	# suite.addTest(Test_tuling('test_post1'))
	# filedir=".\\report\\"
	# filename="pyresult.html"
	# filepath=filedir+filename
	# if os.path.exists(filepath) is False:
	# 	os.system(r'touch %s' % filename)
	# fp=open(filepath,'wb')
	# runner= BSTestRunner.BSTestRunner(stream=fp, title=u'接口测试的结果', description='这是post接口测试报告，如下')
	# runner.run(suite)
	# # sendemali(filepath)#这里的路径需要时需要填写路径，
	suite = unittest.TestSuite()
	suite.addTest(Testinface("testinterface"))
	filedir = ".\\report\\"
	filename = "pyresult.html"
	filepath =filedir+filename
	if os.path.exists(filepath) is False:
		os.system(r'touch %s' % filename)
	fp = open(filepath, 'wb')
	runner = BSTestRunner.BSTestRunner(stream=fp, title=u'接口测试的结果', description='这是post接口测试报告，如下')
	runner.run(suite)

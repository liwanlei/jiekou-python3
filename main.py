# -*- coding: utf-8 -*-
# @Author  : leizi
from report.emmail import sendemali
import time,unittest
from report import HTMLTestRunner
'''
这里你可以分开执行上面你case里面包含的用例。也可以单独执行里面
的某一个的测试用例
'''
from case.post import Test_tuling
from report import  BSTestRunner
if __name__ == '__main__':
	project_path=r'C:\Users\Administrator\Desktop\jiekou'
	suite = unittest.TestSuite()
	suite.addTest(Test_tuling("test_post4"))
	suite.addTest(Test_tuling('test_post3'))
	suite.addTest(Test_tuling('test_post2'))
	suite.addTest(Test_tuling('test_post1'))
	filedir=project_path+"\\report\\"
	filename="pyresult.html"
	filepath=filedir+filename
	fp=open(filepath,'wb')
	runner=BSTestRunner.BSTestRunner(stream=fp,title=u'接口测试的结果',description='这是post接口测试报告，如下')
	runner.run(suite)
	time.sleep(2)

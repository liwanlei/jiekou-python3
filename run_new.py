# -*- coding: utf-8 -*-
# @Author  : leizi
from testCase.ddt_case import MyTest
import unittest, time, os
from Public import BSTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    now = time.strftime('%Y-%m%d', time.localtime(time.time()))
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'test_Report')
    file = os.path.join(file_dir, (now + '.html'))
    re_open = open(file, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='接口测试报告', description='测试结果')
    runner.run(suite)

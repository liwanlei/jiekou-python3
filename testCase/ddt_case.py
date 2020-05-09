from Interface.testFengzhuang import TestApi
from Public.get_excel import datacel, makedata
from Public.log import LOG, logger
from Public.panduan import assertre
import ddt, unittest, time, os

data_test = makedata()


@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @ddt.data(*data_test)
    def test_api(self, data_test):
        api = TestApi(url=data_test['url'], key=data_test['key'], connent=data_test['coneent'],
                      fangshi=data_test['fangshi'])
        LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'], data_test['coneent'],
                                                       LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (
                                                       data_test['url'], data_test['key'], data_test['coneent'],
                                                       data_test['fangshi']))))
        apijson = api.getJson()
        LOG.info('返回结果:%s' % apijson)
        qingwang = assertre(asserqingwang=data_test['qiwang'])
        self.assertNotEqual(dict(qingwang), dict(apijson), msg='预期和返回不一致')

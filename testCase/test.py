from  Interface.testFengzhuang import TestApi
from  Public.get_excel import datacel,makedata
from  Public.log import LOG,logger
import ddt,unittest
data_test=makedata()
@logger('执行测试用例')
@ddt.ddt
class ApiTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data(*data_test)
    def test_api(self,data_test):
        api = TestApi(url=data_test['url'], key=data_test['key'], connent=data_test['coneent'], fangshi=data_test['fangshi'])
        LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s'%(data_test['url'],data_test['key'],data_test['coneent'],        LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s'%(data_test['url'],data_test['key'],data_test['coneent'],data_test['fangshi']))))
        apijson = api.getJson()
        LOG.info('返回结果:%s'%apijson)
        self.assertEqual(data_test['qiwang'],apijson,msg='预期和返回不一致')


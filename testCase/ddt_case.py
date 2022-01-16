import ddt, unittest,os,yaml
from Interface.testFengzhuang import TestApi
from Public.get_excel import makedata
from Public.log import LOG
from Public.panduan import assertre
from  config.config import TestPlanUrl

file_dir = os.path.join(os.getcwd(), 'test_Report')
file_reslut = os.path.join(file_dir, 'caseresult.yaml')

data_test = makedata()

def write(data):
    with open(file_reslut, 'a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
def read(data):
    f = open(file_reslut, 'r', encoding='utf-8')
    d = yaml.load(f, Loader=yaml.FullLoader)
    return d[data]


@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @ddt.data(*data_test)
    def test_api(self, data_test):
        '''
        1.处理参数
        2.判断参数是否有依赖
        3.依赖用例参数从本地获取
        4.获取失败，用例失败
        5.拼接后请求
        '''
        parem = {'key': data_test['key']}
        try:
            parem_dict=eval(data_test['coneent'])
            for key,value in parem_dict.items():
                if str(value).startswith("&"):
                    try:
                        reply_key_id=str(value).split("&")[-1].split("=")
                        reply_keyid=reply_key_id[0]
                        reply_key_key=reply_key_id[1]
                        reslut=read(reply_keyid)
                        if reslut is None:
                            self.assertTrue(False,'依赖用例获取失败')
                        get_value=reslut[reply_key_key]
                        if get_value is None:
                            self.assertTrue(False, '依赖参数获取失败，不存在')
                        parem_dict[key]=get_value
                    except Exception as e:
                        LOG.info("用例依赖执行失败："+str(e))
                        self.assertTrue(False,'用例依赖执行失败')

            parem.update({'info':parem_dict})
        except:
            self.assertTrue(False,msg="参数格式不对")

        # try:
            #parem=eval(data_test['coneent'])
        # except:
        #     self.assertTrue(False, msg="参数格式不对")
        api = TestApi(url=TestPlanUrl+data_test['url'],
                      parame=parem,
                      method=data_test['fangshi'])
        LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'], data_test['coneent'],
                                                       LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (
                                                           data_test['url'], data_test['key'], data_test['coneent'],
                                                           data_test['fangshi']))))
        apijson = api.getJson()
        reslut={}
        reslut[data_test['id']]=apijson
        write(reslut)
        LOG.info('返回结果:%s' % apijson)
        assertall = assertre(asserqingwang=data_test['qiwang'])
        self.assertNotEqual(dict(assertall), dict(apijson), msg='预期和返回不一致')

'''
  @Description      
  @auther         leizi
'''
from Interface.testFengzhuang import TestApi
from public.log import LOG
from public.panduan import assertre
from  config.config import TestPlanUrl
import pytest
import  os
import  yaml
from public.get_excel import makedata
file_dir = os.path.join(os.getcwd(), 'test_Report')
file_reslut = os.path.join(file_dir, 'caseresult.yaml')

def write(data):
    with open(file_reslut, 'a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
def read(data):
    f = open(file_reslut, 'r', encoding='utf-8')
    d = yaml.load(f, Loader=yaml.FullLoader)
    return d[data]

data_test = makedata()
@pytest.mark.parametrize(data_test)
class TestParametrize(object):
    def test_parame(self):
        parem = {'key': data_test['key']}
        try:
            parem_dict = eval(data_test['coneent'])
            for key, value in parem_dict.items():
                if str(value).startswith("&"):
                    try:
                        reply_key_id = str(value).split("&")[-1].split("=")
                        reply_keyid = reply_key_id[0]
                        reply_key_key = reply_key_id[1]
                        reslut = read(reply_keyid)
                        if reslut is None:
                            assert False
                        get_value = reslut[reply_key_key]
                        if get_value is None:
                            assert False
                        parem_dict[key] = get_value
                    except Exception as e:
                        LOG.info("用例依赖执行失败：" + str(e))
                        assert  False
            parem.update({'info': parem_dict})
        except:
            assert False

        api = TestApi(url=TestPlanUrl + data_test['url'],
                      parame=parem,
                      method=data_test['fangshi'])
        LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'], data_test['coneent'],
                                                       LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (
                                                           data_test['url'], data_test['key'], data_test['coneent'],
                                                           data_test['fangshi']))))
        apijson = api.getJson()
        reslut = {}
        reslut[data_test['id']] = apijson
        LOG.info('返回结果:%s' % apijson)
        assertall = assertre(asserassert=data_test['qiwang'])

        assert dict(assertall) == dict(apijson)

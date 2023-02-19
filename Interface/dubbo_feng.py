""" 
@author: lileilei
@file: dubbo_feng.py 
@time: 2018/3/29 12:26 
"""
from pyhessian.client import HessianProxy
from pyhessian import protocol
from public.log import LOG, logger


@logger('dubbo接口')
class DubboInterface:
    def __init__(self, url, interface, method, param, **kwargs):
        self.url = url
        self.interface = interface
        self.method = method
        self.param = param
        self.interfaceparam = protocol.object_factory(self.param, **kwargs)

    def getresult(self):
        try:
            result = HessianProxy(self.url + self.interface)
            return_result = getattr(result, self.method)(self.interfaceparam)
            LOG.info('测试返回结果:%s' % return_result)
            res = {'code': 0, 'result': return_result}
        except Exception as e:
            LOG.info('测试失败，原因：%s' % e)
            res = {'code': 1, 'result': e}
        return res

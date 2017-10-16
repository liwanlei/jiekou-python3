# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 21:54:08
# @Author  : lileilei
from .log import LOG,logger
@logger('断言测试结果')
def assert_in(asserqiwang,fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(fanhuijson[key])) for key in result.keys()])
        value2=([(str(value)) for value in result.values()])
        if value1==value2:
            return  'pass'
        else:
            return 'fail'
    else:
        LOG.info('填写测试预期值')
        raise ('请填写期望值')

# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
from public.test_requests import requ


class TestApi(object):
    def __init__(self, url, parame, method):
        self.url = url
        self.parame = parame
        self.method = method
        self.reques = requ()

    def testapi(self):
        if self.method == 'POST':
            self.response = self.reques.post(self.url, self.parame)
        elif self.method == "GET":
            self.response = self.reques.get(url=self.url, params=self.parame)
        elif self.method == "PUT":
            self.response = self.reques.putparams(url=self.url, params=self.parame)
        elif self.method == "DELETE":
            self.response = self.reques.delparams(url=self.url, params=self.parame)
        return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data

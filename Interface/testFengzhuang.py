# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
from Public.test_requests import requ

reques = requ()


class TestApi(object):
    def __init__(self, url, parame, method):
        self.url = url
        self.parame = parame
        self.method = method

    def testapi(self):
        if self.method == 'POST':
            self.response = reques.post(self.url, self.parame)
        elif self.method == "GET":
            self.response = reques.get(url=self.url, params=self.parame)
        elif self.method == "PUT":
            self.response = reques.putparams(url=self.url, params=self.parame)
        elif self.method == "DELETE":
            self.response = reques.delparams(url=self.url, params=self.parame)

        return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data

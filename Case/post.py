# -*- coding: utf-8 -*-
# @Author  : leizi
from Interface.feng import reques
import yaml,unittest
reques=reques()
class Test_tuling(unittest.TestCase):
    def setUp(self):
        self.data_file = open(r".\data\data.yaml","r",encoding= "utf-8")
        self.data = yaml.load(self.data_file)
        self.post_data=self.data['post']
    def tearDown(self):
        pass
    def test_post1(self):
        self.url=self.post_data['post1']['url']
        self.key=self.post_data['post1']['key']
        self.coneent=self.post_data['post1']['coneent']
        self.fangshi=self.post_data['post1']['fangshi']
        self.code=self.post_data['post1']['code']
        self.parem={'key':self.key,'info':self.coneent}
        self.me=reques.post(url=self.url,params=self.parem)
        self.assertEqual(self.me['code'],int(self.code),msg='接口返回标识符有误')
    def test_post2(self):
        self.url=self.post_data['post2']['url']
        self.key=self.post_data['post2']['key']
        self.coneent=self.post_data['post2']['coneent']
        self.fangshi=self.post_data['post2']['fangshi']
        self.code=self.post_data['post2']['code']
        self.parem={'key':self.key,'info':self.coneent}
        self.me=reques.post(url=self.url,params=self.parem)
        self.assertEqual(self.me['code'],int(self.code),msg='接口返回标识符有误')
    def test_post3(self):
        self.url=self.post_data['post3']['url']
        self.key=self.post_data['post3']['key']
        self.coneent=self.post_data['post3']['coneent']
        self.fangshi=self.post_data['post3']['fangshi']
        self.code=self.post_data['post3']['code']
        self.parem={'key':self.key,'info':self.coneent}
        self.me=reques.post(url=self.url,params=self.parem)
        self.assertEqual(self.me['code'],int(self.code),msg='接口返回标识符有误')
    def test_post4(self):
        self.url=self.post_data['post4']['url']
        self.key=self.post_data['post4']['key']
        self.coneent=self.post_data['post4']['coneent']
        self.fangshi=self.post_data['post4']['fangshi']
        self.code=self.post_data['post4']['code']
        self.parem={'key':self.key,'info':self.coneent}
        self.me=reques.post(url=self.url,params=self.parem)
        self.assertEqual(self.me['code'],int(self.code),msg='接口返回标识符有误')
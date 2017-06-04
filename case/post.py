# -*- coding: utf-8 -*-
# @Author  : leizi
from fengzhuang.feng import reques
import yaml,unittest

class Test_tuling(unittest.TestCase):
    def setUp(self):
        title=u'登陆测试'
        self.data_file = open(r"C:\\Users\\Administrator\\Desktop\\jiekou\\data\\data.yaml","r",encoding= "utf-8")
        self.data = yaml.load(self.data_file)
        self.post_data=self.data['post']
    def tearDown(self):
        pass
    def test_post1(self):
        try:
            self.url=self.post_data['post1']['url']
            self.key=self.post_data['post1']['key']
            self.coneent=self.post_data['post1']['coneent']
            self.fangshi=self.post_data['post1']['fangshi']
            self.code=self.post_data['post1']['code']
            self.parem={'key':self.key,'info':self.coneent}
            if self.fangshi == 'POST':
                self.me=reques.post(url=self.url,params=self.parem)
                self.assertEqual(self.me['code'],self.code,msg='接口返回标识符有误')
            else:
                print('不支持%s方式请求'%self.fangshi)
        except Exception as e:
            print('用例1测试失败,原因:%s'%e)

    def test_post2(self):
        try:
            self.url=self.post_data['post2']['url']
            self.key=self.post_data['post2']['key']
            self.coneent=self.post_data['post2']['coneent']
            self.fangshi=self.post_data['post2']['fangshi']
            self.code=self.post_data['post2']['code']
            self.parem={'key':self.key,'info':self.coneent}
            if self.fangshi == 'POST':
                self.me=reques.post(url=self.url,params=self.parem)
                self.assertEqual(self.me['code'],self.code,msg='接口返回标识符有误')
            else:
                print('不支持%s方式请求'%self.fangshi)
        except Exception as e:
            print('用例2测试失败,原因:%s'%e)
    def test_post3(self):
        try:
            self.url=self.post_data['post3']['url']
            self.key=self.post_data['post3']['key']
            self.coneent=self.post_data['post3']['coneent']
            self.fangshi=self.post_data['post3']['fangshi']
            self.code=self.post_data['post3']['code']
            self.parem={'key':self.key,'info':self.coneent}
            if self.fangshi == 'POST':
                self.me=reques.post(url=self.url,params=self.parem)
                self.assertEqual(self.me['code'],self.code,msg='接口返回标识符有误')
            else:
                print('不支持%s方式请求'%self.fangshi)
        except Exception as e:
            print('用例3测试失败,原因:%s'%e)
    def test_post4(self):
        try:
            self.url=self.post_data['post4']['url']
            self.key=self.post_data['post4']['key']
            self.coneent=self.post_data['post4']['coneent']
            self.fangshi=self.post_data['post4']['fangshi']
            self.code=self.post_data['post4']['code']
            self.parem={'key':self.key,'info':self.coneent}
            if self.fangshi == 'POST':
                self.me=reques.post(url=self.url,params=self.parem)
                self.assertEqual(self.me['code'],self.code,msg='接口返回标识符有误')
            else:
                print('不支持%s方式请求'%self.fangshi)
        except Exception as e:
            print('用例4测试失败,原因:%s'%e)

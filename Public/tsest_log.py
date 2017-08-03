# -*- coding: utf-8 -*-
# @Time    : 2017/6/17 15:56
# @Author  : lileilei
# @File    : tsest_log.py
# @Software: PyCharm
import  logging,time,os
class log_re():
    def __init__(self,title):
        self.day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        self.logger = logging.Logger(title)
        # basdir = os.path.abspath(os.path.dirname(__file__))
        # filepath=os.path.join(basdir+'\\TestLog\\%s.log'%self.day)
        filepath = '%s.log'% self.day
        # if os.path.exists(filepath) is False:
        #     os.system(r'touch %s' % filepath)
        self.logger.setLevel(logging.INFO)
        self.logfile = logging.FileHandler(filepath)
        self.logfile.setLevel(logging.INFO)
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)
    def debugInfo(self, message):
        self.logger.debug(message)
    def info_log(self, message):
        self.logger.info(message)
    def ware_log(self, message):
        self.logger.warn(message)
    def error_log(self, message):
        self.logger.error(message)

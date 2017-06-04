# -*- coding: utf-8 -*-
# @Author  : leizi
import logging,os,time
class log_message:
	def __init__(self,title):
		# time
		self.day=time.strftime("%Y%m%d",time.localtime(time.time()))
		#创建一个logger
		self.logger=logging.getLogger(title)
		self.logger.setLevel(logging.INFO)
		#创建Heandler 用于写入文件
		self.logfile=logging.FileHandler(r'C:\Users\Administrator\Desktop\te_blogf\lo\%s.log'%self.day)
		self.logfile.setLevel(logging.INFO)
		#创建Heandler 用于显示控制台
		self.control=logging.StreamHandler()
		self.control.setLevel(logging.INFO)
		#定义输出格式
		self.formatter=logging.Formatter("%(key)s - %(coneent)s - %(coneent)s - %(message)s")
		self.logfile.setFormatter(self.formatter)
		self.control.setFormatter(self.formatter)
		#给logger添加handler
		self.logger.addHandler(self.logfile)
		self.logger.addHandler(self.control)
	def debug_log(self,message):
		self.logger.debug(message)
	def info_log(self,message):
		self.logger.info(message)
	def ware_log(self,message):
		self.logger.ware(message)

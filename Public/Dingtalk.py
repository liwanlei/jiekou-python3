""" 
@author: lileilei
@file: Dingtalk.py 
@time: 2017/12/26 17:34 
"""
'''封装钉钉群发消息'''
import requests, json
from config.config import Dingtalk_access_token


def send_ding(content):
    url = Dingtalk_access_token
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "isAtAll": True
    }
    headers = {
        'Content-Type': 'application/json'
    }
    f = requests.post(url, data=json.dumps(pagrem), headers=headers)
    if f.status_code == 200:
        return True
    else:
        return False

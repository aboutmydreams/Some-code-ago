import requests
def get_content(url):
	resp = requests.get(url,allow_redirects=False)
	return resp.text
url='http://www.phei.com.cn/'
content = get_content(url)
content_len=len(content)
print('前20字符：', content[:1120], content_len)

import  requests
import json
#url='http://fanyi.baidu.com/'
#response=requests.get(url)
#print(response.status_code)#状态码 200 成功
#response.encoding='utf-8'#指定编码
#print(response.text)
url='http://fanyi.baidu.com/?aldtype=85#en/zh/word%20is%20lads'
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://fanyi.baidu.com/?aldtype=85#en/zh/word%20is%20lads')
elements = driver.find_element_by_class_name('ordinary-output target-output clearfix')#假设有个‘nav’的类
InnerElement = elements.get_attribute('innerHTML')
print('InnerElement')



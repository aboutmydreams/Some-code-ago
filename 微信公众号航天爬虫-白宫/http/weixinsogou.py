#! -*- encoding:utf-8 -*-
import re
import json
import requests
from bs4 import BeautifulSoup

def ali_proxies(targetUrl):
    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HT2520U04Z19W00D"
    proxyPass = "0BE22F9E31998CC6"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }

    response = requests.get(targetUrl, proxies=proxies)
    print (response.status_code)
    # print(response.text)
    return response.text


url = 'http://mp.weixin.qq.com/profile?src=3&timestamp=1536053272&ver=1&signature=YoKNZ47R0SQs*ieS-0LUlT14271ZKUYmDnv-WRysqUZnkj3yRgXAVVgxgU9XegauowqeDXGaHwSLCPk9mcO70g=='
side = 'weui_media_title'
res = ali_proxies(url)
soup = BeautifulSoup(res,'html.parser')
soup1 = BeautifulSoup(res,'lxml')
if '安全' in str(soup):
    print ('需要验证码了')
try:
    name_id = soup.select('body > div.page_profile_info > div.page_profile_info_inner > div.profile_info_area > div.profile_info_group > div > p ')
    print (name_id[0].get_text()[4:])

    title = soup.findAll("script", {"type": "text/javascript"}, text = re.compile('.*var msgList.*'))
    # print(title)
    json1 = json.loads(re.findall('var msgList.*?\n', str(title))[0][14:-2])
    # print(re.findall('"content_url":".*?"', re.findall('var msgList.*?\n', str(title))[0][14:-2]))
    # print(re.findall('"title":".*?"', re.findall('var msgList.*?\n', str(title))[0][14:-2]))
    # aaa= re.findall('"content_url":".*?"', re.findall('var msgList.*?\n', str(title))[0][14:-2])
    # print (str(aaa).replace(';','&'))
    json2 = json.loads(re.findall('var msgList.*?\n', str(title))[0][14:-2])
    the_url = json2['list'][1]['app_msg_ext_info']['content_url'].replace(';','&')
    the_title = json2['list'][1]['app_msg_ext_info']['title']
    # print (json2['list'][3])
    # print (len(json2['list']))
    lin = ''
    for i in json2['list']:
        the_url = i['app_msg_ext_info']['content_url'].replace(';','&')
        the_title = i['app_msg_ext_info']['title']
        lin = (
            f'{lin}【标题】：{the_title}'
            + '\n'
            + '【标题链接】：https://mp.weixin.qq.com'
            + the_url
            + '\n'
        )

        print (lin)
except:
    pass
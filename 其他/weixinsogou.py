# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup



url = f'http://weixin.sogou.com/weixin?type=1&query={id_name}&ie=utf8&s_from=input&_sug_=y&_sug_type_='

#print(requests.get(url).text)#测试是否包含需要的数据

res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')
id_position = '#sogou_vr_11002301_box_0 > div > div.img-box > a'
id_link = soup.select(id_position)
#print(id_link[0].get("href").replace(';','&'))#测试连接有效性 有效

one_link = id_link[0].get("href").replace(';','&')
all_links = [one_link]














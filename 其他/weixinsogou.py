# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup



# url = 'http://weixin.sogou.com/'
# s = requests.session()
# res = s.get(url)
# cookies = requests.utils.dict_from_cookiejar(res.cookies)
# print(cookies)
# res = s.get(url,headers=cookies)
# soup = BeautifulSoup(res.content,'lxml',from_encoding="UTF-8")
# tittle = soup.select('#pc_0_0 > li:nth-of-type(1) > div.txt-box > h3')
# print(tittle)
# herf= 'http://mp.weixin.qq.com/s?src=11&amp;timestamp=1535522402&amp;ver=1089&amp;signature=4g442BsYT8GVThDDiZ8LpAXJlwsBDmS7wPwVRSX7lRGFS2vrQ3c5sVf5roZLeCJW45vbmVIds62YyuVjgCRHNCpVv1iVA4x8GIjY9Xi37Uu0GpATL0fgk5dMyHHE9M0k&amp;new=1'
# ah = herf.replace(';','&')
# print(ah)


all_links = []
url = 'http://weixin.sogou.com/weixin?type=1&query={}&ie=utf8&s_from=input&_sug_=y&_sug_type_='.format(id_name)
#print(requests.get(url).text)#测试是否包含需要的数据

res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')
id_position = '#sogou_vr_11002301_box_0 > div > div.img-box > a'
id_link = soup.select(id_position)
#print(id_link[0].get("href").replace(';','&'))#测试连接有效性 有效

one_link = id_link[0].get("href").replace(';','&')
all_links.append(one_link)
return all_links














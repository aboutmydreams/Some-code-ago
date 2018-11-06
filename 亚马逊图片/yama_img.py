import requests
from bs4 import BeautifulSoup
url = 'https://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dstripbooks&field-keywords=管理学是什么'
res = requests.get(url)
Soup = BeautifulSoup(res.text,'lxml')
img = Soup.select('#result_0 > div > div.a-fixed-left-grid > div > div.a-fixed-left-grid-col.a-col-left > div > div > a')
print(img)
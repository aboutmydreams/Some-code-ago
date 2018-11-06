#用request+beautifulsoup抓取tripadvisor
print('hi')
from bs4 import BeautifulSoup
import requests
import time#为了做一个保护
#模拟登陆：
'''
headers = {
    'User-Agent':'ctrl+v'
    'Cookie':'ctrl+v'
}
url=''
wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
'''
url=('https://mp.weixin.qq.com/s/xu-rtXSKy9oWkrOc_13wqw')

def get_data(url,data=None) :#定义一个函数：一个小技巧，不需要登陆或模拟登入后写data=None就会返回data的值
    wb_data = requests.get(url)
    time.sleep(1)#这是一个重要的保护措施
    Soup = BeautifulSoup(wb_data.text,'lxml')
    print(Soup)
get_data(url)
#get_data(url)#成功
#print(urls)#链接列表 成功
#for every_url in urls:
    #get_data(every_url)#失败
'''
似乎有反爬取，。。。图片链接都一样 解决方案可以用移动端，新建一个文件 11.5,这次爬酒店的
'''
get_data(url)
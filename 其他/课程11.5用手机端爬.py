from bs4 import BeautifulSoup
import requests
url = 'https://www.tripadvisor.cn/Hotels-g293916-Bangkok-Hotels.html'
headers = {
    'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
}
mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
tittles = soup.select('div.prw_rup.prw_meta_hsx_listing_name.listing-title > h2.listing_title > a')
imgs = soup.select('div.aspect.is-hidden-tablet > div')
print(imgs)#成功
print(type(imgs))
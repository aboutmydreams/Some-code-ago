import requests
from bs4 import BeautifulSoup
url = 'http://fanyi.baidu.com/?aldtype=85#en/zh/happy'
wb_data = requests.get(url)
wb_data.encoding='utf-8'


Soup = BeautifulSoup(wb_data.text,'lxml')
#print(len(str(Soup)))
tittles = Soup.prettify()
print(tittles)

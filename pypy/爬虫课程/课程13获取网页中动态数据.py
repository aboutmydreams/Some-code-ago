'''
动态的数据 看监视器中的XHR，里面一般会有page=？
'''
from bs4 import BeautifulSoup
import requests
import time
url = 'http。。。。。page='
def get_page(url,data=None):
    wb_data = request.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('h4 > a')

def get_more_data(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)
get_page(1,10)

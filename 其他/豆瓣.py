from bs4 import BeautifulSoup
import requests
# url = 'https://book.douban.com/subject_search?search_text='
# isbn = '978-7-121-10884-6'.replace('-','')
#
# url1 = url+str(isbn)+'&cat=1001'
# print(url1)
url = 'https://m.douban.com/search/?query=%E7%8E%B0%E4%BB%A3%E5%8C%85%E8%A3%85%E8%AE%BE%E8%AE%A1%E7%90%86%E8%AE%BA%E4%B8%8E%E6%96%B9%E6%B3%95'
headers ={
    'Referer':'https://m.douban.com/search/?query=9787121108846',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'

}
def get_page(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    names = soup.select('body > div.page > div > div > ul > li:nth-of-type(2) > ul > li:nth-of-type(1) > a > div > span ')
    #print(soup)
    print(names)
get_page(url)
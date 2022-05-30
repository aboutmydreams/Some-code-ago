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
url=('https://www.tripadvisor.cn/Attractions-g293916-Activities-Bangkok.html')
urls = [
    f'https://www.tripadvisor.cn/Attractions-g293916-Activities-oa{str(i)}-Bangkok.html'
    for i in range(30, 120, 30)
]

def get_data(url,data=None) :#定义一个函数：一个小技巧，不需要登陆或模拟登入后写data=None就会返回data的值
    wb_data = requests.get(url)
    time.sleep(1)#这是一个重要的保护措施
    Soup = BeautifulSoup(wb_data.text,'lxml')
    #print(len(str(Soup)))
    tittles = Soup.select('div.listing_title > a')#可直接用div + . + css的class名称
    ranks1 = Soup.select(' div > div > div.listing_info > div.listing_rating > div')
    ranks = ranks1[2::]
    Number_of_comments = Soup.select('a.review_count')

    images = Soup.select('img.photo_image ')#('img[width="200"]')#注意要用双引号“”，全都出来了
    '''
        #images = Soup.select('#lazyload_-272293795_2') #复制来居然是id，也得不到src。可用上一（几）级div的路径，或显示width
        images = Soup.select('#taplc_attraction_coverpage_attraction_0 > div:nth-of-type(1) > div > div > div.shelf_item_container > div:nth-of-type(1) > div.poi > a ')
        #nth-of-type
        print(images)#这回有用了，下面尝试方括号
    '''
    if not Number_of_comments:
        Number_of_comments = Soup.select('div.listing_info > div.listing_rating > div > div > span.more > a')
    for tittle,rank,Number_of_comment,image in zip(tittles,ranks,Number_of_comments,images):
        data = {
            'tittle' : tittle.get_text(),
            'rank' : list(rank.stripped_strings),
            'Number_of_comment' :  Number_of_comment.get_text(),
            'image' : image.get('src')
        }
        print (data)#image的src都一样，原因是网站做了反扒的js

#get_data(url)#成功
#print(urls)#链接列表 成功
#for every_url in urls:
    #get_data(every_url)#失败
'''
似乎有反爬取，。。。图片链接都一样 解决方案可以用移动端，新建一个文件 11.5,这次爬酒店的
'''
get_data(url)
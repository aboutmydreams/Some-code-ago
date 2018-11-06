from bs4 import BeautifulSoup
import requests
import time
url = 'https://www.amazon.cn/dp/B003OXG63K/ref=sr_1_1?s=books&ie=UTF8&qid=1518615264&sr=1-1&keywords=9787532763573'
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    #'Cookie':'session-id=458-9835325-5484866; ubid-acbcn=460-4972597-9737344; x-wl-uid=1MLIPzrOf1Z30OVHbGvs67n/GF+HHd+FmUsGZ3DjTtX7nQEgaob8W/gED/65Y4kpzt7pq2pMmw0I=; session-token="3RGSwdTdUz7l5O4O1kHtLnYPtsO8kJOojD49cpGeMeuF7xE/IlLrhJWsUq2XNtVdk61jQilk4pFlCYgU4kMiE70Cursgl0R1LakjmI24xP3CTUDD6wlo8yCIZmLg6Yc4Y/88jAjzC5D9pntKJfmap+CZ99vrrVrmzAqk8bhkLr5wd3tNbA2eaDCAETtVQbarErqBJFnGTa9UViDOKT4QyGOzRxdlJEMNbg8Y3QOv8P8DzoNKut3p3A=="; csm-hit=NBXN1FQY423ZX4CRGEPF+s-EC1HY60E8SMV0H3V9DVH|1518615286121; session-id-time=2082729601l',
    'Host':'www.amazon.cn',
    'Referer':'https://www.amazon.cn/dp/B003OXG63K/ref=sr_1_1?s=books&ie=UTF8&qid=1518615264&sr=1-1&keywords=9787532763573',
    'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
}
mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
tittles = soup.select('#title')
catalogs = soup.select('#productDescription_fullView > div:nth-of-type(8) > p')
ps = soup.select('#s_content_2 > p')
print(tittles,catalogs,ps)
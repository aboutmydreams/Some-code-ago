import requests
from PIL import Image
url = 'http://www.ncuos.com/api/user/profile/basic'
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Authorization':'passport eyJleHAiOjE1MTg1ODk0ODEsImlhdCI6MTUxODU4NjQ4MSwiYWxnIjoiSFMyNTYifQ.eyJpZCI6IjY2OTIzOTkxMTUifQ.vRrU1Zuc8WDadFE77bLavziRlVGixc2gbsg50-KiU90',
    'Connection':'keep-alive',
    'Cookie':'_ga=GA1.2.847620956.1518578955; _gid=GA1.2.540648614.1518578955; _bl_uid=a3jXjdLXmtti2dp0C90sd2jfbdXv',
    'Hos':'www.ncuos.com',
    'Referer':'http://www.ncuos.com/index/person',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
response = requests.get(url,headers=headers)
print(response.text[36:42])

# def getinformation(token):
#     url = 'https://www.ncuos.com/api/user/profile/basic'
#     url2 = 'https://www.ncuos.com/api/user/profile/school_roll'
#     headers = {
#         'content-type': 'application/json',
#         'Authorization':r'passport '+ token
#     }
#     e = requests.get(url,headers=headers)
#     i = requests.get(url2,headers=headers)
#     rule = re.compile(r"\D(\d\d)")
#     nj = rule.findall(i.json()['school_roll'][0]['bjmc'])
#     information = {
#                 'xm':e.json()['base_info']['xm'],
#                 'xb':e.json()['base_info']['xb']['mc'],
#                 'xy':i.json()['school_roll'][0]['xy'],
#                 'nj':nj[0]
#     }
#     return information
# getinformation( "eyJleHAiOjE1MTg1ODk0ODEsImlhdCI6MTUxODU4NjQ4MSwiYWxnIjoiSFMyNTYifQ.eyJpZCI6IjY2OTIzOTkxMTUifQ.vRrU1Zuc8WDadFE77bLavziRlVGixc2gbsg50-KiU90")
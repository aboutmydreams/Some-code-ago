import requests
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'#name:translate_o?smartresult=dict&smartresult=rule
#http://fanyi.youdao.com/bbk/translate_m.do#name:translate_m.do
data={
    'i':'中',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1518077713426',
    'sign':'9b35ebfe9ecc26e40daef2e2e289326d',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult':'false'
}

session=requests.Session()#session可以保持cookie
session.cookies.set('OUTFOX_SEARCH_USER_ID','-1990956921@59.111.179.155')#前面是key，后面是植，不要忘了：FG'='1
response=session.post(url,data=data)#第一个data是web端请求内容，第二个是上面写的数据，发送请求。
response.encoding='utf-8'
print(response.text)
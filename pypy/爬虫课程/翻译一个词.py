import  requests
import json
#url'=''http://fanyi.baidu.com/'
#response'='requests.get(url)
#print(response.status_code)#状态码 200 成功
#response.encoding'=''utf-8'#指定编码
#print(response.text)
url='http://fanyi.baidu.com/v2transapi'#api接口
data={
    'from':'en',
    'to':'zh',
    'query':'word',
    'simple_means_flag':'3',
    'sign':'924944.720417',#js加密
    'token':'decd37b5578132fd462193b3ae316424'
}#数据
session=requests.Session()#session可以保持cookie
session.cookies.set('BAIDUID','5E0BC240B6855194825BC38744EC3374:FG=1')#前面是key，后面是植，不要忘了：FG'='1
response=session.post(url,data=data)#第一个data是web端请求内容，第二个是上面写的数据，发送请求。
response.encoding='utf-8'
print(json.loads(response.text))
fi=json.loads(response.text)
print(fi['trans_result']['data'][0]['dst'])


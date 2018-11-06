import requests
import base64
# 获取token
host =  'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ir3vbkVgKHywSDrzLASDpFAT&client_secret=ctvu2kbwBSX3C5kGiXC66F1fRp1VcoiI'
# 填入 自己的APIKEY 和SK
headers = {
    'Content-Type':'application/json;charset=UTF-8'
}

res = requests.get(url=host,headers=headers).json()
print(res)
print(res['access_token'])

data = {}
data['access_taken'] = res['access_token']
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic' + 'user/add?access_token=' +res['access_token']
#读取图片
file=open('1.png','rb')
image= file.read()
file.close()

data['image'] = base64.b64encode(image)
headers={
    "Content-Type":"application/x-www-form-urlencoded",
}

res = requests.post(url=url,headers=headers,data=data)
result = res.json()
# print(type(result))
# print(result)
wod = result["words_result"]
for i in wod:
    print(i['words'])

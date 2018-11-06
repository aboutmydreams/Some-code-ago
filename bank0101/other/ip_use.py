import requests

url = 'http://hao123.com'
testip = '122.96.93.158:49435'
px = requests.get(url,proxies={'http':'http://{}'.format(testip)})
print (px.text)

import requests
from bs4 import BeautifulSoup
def alert_psd():
    url = 'http://jwc103.ncu.edu.cn/jsxsd/xk/CheckPwd'
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'18',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'UM_distinctid=161dcbfe6883e2-08b6b6d88e17bd-d35346d-15f900-161dcbfe6893c6; JSESSIONID=FC1C020A6F2770A95EA2E87B1AA2C656',
        'Host':'jwc103.ncu.edu.cn',
        'Origin':'http://jwc103.ncu.edu.cn',
        'Referer':'http://jwc103.ncu.edu.cn/jsxsd/enteruserid.jsp',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    }
    data = {
        'account':'7901117101',
        'sfzjh':'362229199908180039',
    }
    response = requests.post(url,data=data,headers=headers)
    print(response.text)
    print(response.status_code)
def new_psd():


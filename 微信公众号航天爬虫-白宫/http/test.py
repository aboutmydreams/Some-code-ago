import requests,re,json,time
from bs4 import BeautifulSoup
def ali_proxies(targetUrl,header=None):
    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HT2520U04Z19W00D"
    proxyPass = "0BE22F9E31998CC6"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }
    if header:
        response = requests.get(targetUrl,headers=header, proxies=proxies)
        print (response.status_code)
        # print(response.text)
        return response
    else:
        response = requests.get(targetUrl, proxies=proxies)
        print (response.status_code)
        # print(response.text)
        return response
# print (resp.text)



cookies1 = requests.utils.dict_from_cookiejar(res.cookies)
cookie2 = str(cookies1)[2:-2].replace("': '","=").replace("', '",';')

def ten_links(url):
        time.sleep(2.7)
        res = ali_proxies(url)
        soup1 = BeautifulSoup(res.text,'html.parser')
        print(soup1)
        title = soup1.findAll("script", {"type": "text/javascript"}, text = re.compile('.*var msgList.*'))
        # json1 = json.loads(re.findall('var msgList.*?\n', str(title))[0][14:-2])
        if '验证' in str(soup1):
            print('用户您好，访问公众号{}过于频繁')
            return '用户您好，您的访问过于频繁'
        else:
        #try:
            json2 = json.loads(re.findall('var msgList.*?\n', str(title))[0][14:-2])
            # links = json.dumps(lnks)#, indent = 2, separators = {',', ': '})
            lin = ''
            for i in json2['list']:
                the_url = i['app_msg_ext_info']['content_url'].replace(';','&')
                the_title = i['app_msg_ext_info']['title']
                the_title = i['app_msg_ext_info']['title']
                lin = lin+'【标题】：'+ the_title + '\n' + '【标题链接】：https://mp.weixin.qq.com' + the_url + '\n'
            return lin
ten_links('http://mp.weixin.qq.com/profile?src=3&timestamp=1536228696&ver=1&signature=LidTFfBQsdMjdA9Qx5LcB7qcLgA81b2LTqrfMdpevCKYhkyKqCpuVd9iuC3A7CZFJe*0Bw4hCob1ek2V0Gkxxw==')
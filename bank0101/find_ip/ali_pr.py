import requests
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
        if response.status_code is 503:
            return ali_proxies(targetUrl,header)
    else:
        response = requests.get(targetUrl, proxies=proxies)
        if response.status_code is 503:
            return ali_proxies(targetUrl)
    # print(response.text)
    return response
#! -*- encoding:utf-8 -*-
import requests,re,json,time
from bs4 import BeautifulSoup
from urllib.parse import quote
what_name = open('id_list.txt', 'r', encoding='utf-8')
id_list = eval(str(what_name.readlines()).replace('\\n','').replace('\\ufeff',''))#读取数据为元组
print (id_list)
# 要访问的目标页面
# targetUrl = "http://weixin.sogou.com/"



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

#返回coki
'''
def login():
    coki = open('login.txt','r')
    new_coki = coki.readlines()
    cook = str(new_coki).replace("', '",'').replace(' ','').replace('\\n','').replace('锘縖','[')
    ccc = eval(cook.replace('false','False').replace('true','True'))
    ccc1 = eval(ccc[0])
    # print (ccc1[0])
    all_coki = ''
    for x in ccc1:
        pass
        all_coki = all_coki + x['name'] + "=" + x['value'] + ';'
    return all_coki
'''

#输入搜索名称 返回页数
def get_page_num(id_name):
    url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query={}'.format(id_name)
    res = ali_proxies(url)
    soup = BeautifulSoup(res.text,'lxml')
    #print (soup)
    num_site = '#pagebar_container > div'
    weixin_id = soup.select('#sogou_vr_11002301_box_0 > div > div.txt-box > p.info > label')
    # print (soup)
    if '免责声明' in str(soup):
        try:
            nm = int(soup.select(num_site)[0].get_text()[3:-3])
            num = int(nm/10)
            print ('共有多少面-------------------' +str(nm))
            return str(num+1)
        except IndexError:
            return str(1)
    else:
        print (id_name,"没有约找到多少")
        # print (soup)
        return str(1)





def collect_links(id_name,page,cookie=None):
    if not cookie:
        cookie = ''
    one_paper = ''
    one1_link = ''
    page_n = 1
    for i in range(1,int(page)+1):
        print ('第' + str(page_n)+'页--------------'+id_name)
        page_n = page_n+1
        url = 'https://weixin.sogou.com/weixin?query={}&s_from=input&type=1&page={}&ie=utf8'.format(id_name,str(i))
        # url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&_sug_type_=&s_from=input&_sug_=n&type=1&page={}'.format(id_name,str(i))
        #print(requests.get(url).text)#测试是否包含需要的数据
        header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0.3',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                # 'Referer': 'http://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=7528&sst0=1536407158589&lkt=1%2C1536407158486%2C1536407158486'.format(id_name),
                'Cookie' : '{}'.format(cookie),
                'Host': 'weixin.qq.com',
                'Referer': 'http://weixin.sogou.com/weixin?type=1&s_from=input&query={}'.format(quote(id_name)),
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',

        }
        # print (header)
        res = ali_proxies(url)
        soup = BeautifulSoup(res.text,'lxml')
        # print (soup)
        if '404 Not Found' in str(soup):
            print ('404')
        if  '只显示100' in str(soup):
            print('只显示100(要登陆)')
            return '只显示100'+one_paper
        else:
            id_position = 'div > div.txt-box > p.tit > a'#微信号和链接 #sogou_vr_11002301_box_0 > div > div.txt-box > p.tit > a
            id_link = soup.select(id_position)
            # print (id_link)#数据
            weixin_id = soup.select('#sogou_vr_11002301_box_0 > div > div.txt-box > p.info > label')
            # print(soup)查看数据的有无
            if id_link == []:
                print ('没有')
                return str(i)+'没有相关公众号 已跳过'
            try:
                # print (len(id_link))
                n = len(id_link)
                for i in range(0,n):
                    # print (i)
                    one_title = id_link[i].get_text()
                    one_paper = one_paper + one_title +'\n'
                    one_link = str(id_link[i].get("href"))#.replace(';','&')
                    one1_link = one1_link+str(one_link)+'\n'

                # print(id_link[0].get("href").replace(';','&'))#测试连接有效性 有效
                # one_title = id_link[0].get_text()
                # wi_id = str(weixin_id[0].get_text())
                # # print (wi_id)
                # # print(str(i)+" 链接是："+str(one_link)+'\n')#微信公众号<#>微信ID
                # last_all = ''
                # last_all = last_all +  one_title + '<#>' + wi_id +'\n'#字符串的拼接
                # return last_all

                # print (one_paper)
            except (TypeError or IndexError) as e:#找出报错且继续运行代码
                print(e)
                return str(i)+'没有相关公众号 已跳过'

    return one_paper,one1_link

# collect_links('北京航空大学') 测试一个爬取
# print (collect_links('大学',2))

all_links = []
last_name = '微信公众号<#>微信ID\n'
# cooki = login()
# print (cooki,len(id_list))
all_name = ''
for i in range(0,len(id_list)):
    pages = get_page_num(id_list[i])
    print (pages)
    time.sleep(1)
    last_name1 = collect_links(id_list[i],pages)
    last_txt = open('last.txt','a')
    last_txt.write(last_name1[0])
    last_txt.flush()

    links_txt = open('links.txt','a')
    links_txt.write(last_name1[1])
    links_txt.flush()
    all_name = all_name + last_name1[1]
    all_links.append(pages)

#写入文件
lastl_txt = open('aast.txt','w')
lastl_txt.write(last_name+all_name)
lastl_txt.close()
print('已成功爬取')
print (all_links)





#! -*- encoding:utf-8 -*-
import requests,re,json,time,datetime
from bs4 import BeautifulSoup
what_name = open('wx-res.txt','r')
id_list = eval(str(what_name.readlines()).replace('\\n',''))
# print(id_list)
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
    else:
        response = requests.get(targetUrl, proxies=proxies)

    print (response.status_code)
    # print(response.text)
    return response
# print (resp.text)




all_id_link = []
def collect_links(id_name,cookie=None):
    def ten_links(url,header):
        res = ali_proxies(url,header)
        soup1 = BeautifulSoup(res.text,'html.parser')
        # print(soup1)
        title = soup1.findAll("script", {"type": "text/javascript"}, text = re.compile('.*var msgList.*'))
        # json1 = json.loads(re.findall('var msgList.*?\n', str(title))[0][14:-2])
        if '验证' in str(soup1):
            print(f'用户您好，访问公众号{id_name}过于频繁')
            return '用户您好，您的访问过于频繁'
        else:
            # print (soup1)
            json2 = json.loads(re.findall('var msgList.*?\n', str(title))[0][14:-2])
            # links = json.dumps(lnks)#, indent = 2, separators = {',', ': '})
            # print (json2['list'][0]['comm_msg_info'])
            lin = ''
            for i in json2['list']:
                the_url = i['app_msg_ext_info']['content_url'].replace(';','&')
                the_title = i['app_msg_ext_info']['title']
                digest = i['app_msg_ext_info']['digest']
                a_time = i['comm_msg_info']['datetime']
                datearray = datetime.datetime.utcfromtimestamp(a_time)
                the_time= datearray.strftime("%Y--%m--%d %H: %M: %S")
                lin = (
                    f'{lin}【标题】：{the_title}'
                    + '\n'
                    + '【标题链接】：https://mp.weixin.qq.com'
                    + the_url
                    + '\n'
                    + '【摘要】：'
                    + digest
                    + '\n'
                    + '【发布时间】：'
                    + the_time
                    + '\n'
                )

            # print (lin)
            return lin
        # except IndexError as e:
        #     print (e)
        #     return '需要验证'
        # except ValueError:
        #     pass



    # s = requests.session()
    url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query={}'.format(id_name)
    #print(requests.get(url).text)#测试是否包含需要的数据
    res = ali_proxies(url)
    soup = BeautifulSoup(res.text,'lxml')
    if  '验证' in str(soup):
        print('用户您好，查询公众号过于频繁')
        return '用户您好，您的访问过于频繁'
    else:
        id_position = 'div > div.txt-box > p.tit > a'#微信号和链接
        id_link = soup.select(id_position)
        weixin_id = soup.select('#sogou_vr_11002301_box_0 > div > div.txt-box > p.info > label')
        # print(soup)
        last_f = open('new_file/{}.txt'.format(id_name),'w',encoding='utf-8')
        if id_link == []:
            return str(i)+'没有相关公众号 已跳过'
        try:
            # print(id_link[0].get("href").replace(';','&'))#测试连接有效性 有效
            # print(id_link)
            # print (soup)
            cookies1 = requests.utils.dict_from_cookiejar(res.cookies)
            cookie2 = str(cookies1)[2:-2].replace("': '","=").replace("', '",';')
            hd_coki = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0.3',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Referer': 'http://weixin.sogou.com/weixin?type=1&s_from=input&query={}',
                'Host': 'mp.weixin.qq.com',
                'Upgrade-Insecure-Requests': '1',
                'Cookie' : '{}'.format(cookie2),
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            }

            one_link = id_link[0].get("href").replace(';','&')
            one_title = id_link[0].get_text()
            wi_id = str(weixin_id[0].get_text())
            print (wi_id)
            print(str(i)+" 链接是："+str(one_link)+'\n')
            last_f.write('【微信名】：' + one_title +'\n' + '【微信id】：' + wi_id + '\n' + '\n\n'+ten_links(one_link,hd_coki))#str(one_link)+
            last_f.close()
            return one_link
        except (TypeError or IndexError) as e:
            print(e)
            return str(i)+'没有相关公众号 已跳过'
# collect_links('北京航空大学')

all_links = []
error_n = 0
for i in id_list:
    try:
        link = collect_links(i)
        all_links.append(link)
        time.sleep(1)
        if '已跳过' in link:
            error_n = error_n+1
            print(f'这是第{str(error_n)}条空的公众号，已跳过，不会保存相关txt，随便提一下，如果查询公众号中有重复只会保存一次txt')
            #time.sleep(0.6)
    except requests.exceptions.ProxyError as e:
        print (e)
print(len(all_links))



from bs4 import BeautifulSoup
import requests,random

wangzhi = 'http://www.shoujibiao.tk'

list1= [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    ]

# print(random.sample(list1,1))

headers = {
    'User-Agent':random.sample(list1,1)[0],
    'Host': 'www.xicidaili.com',
    'Referer': 'http://www.xicidaili.com/',
}

#获取网页中的ip列表
def get_ip_pool():
    ip_pool = []
    url = 'http://www.xicidaili.com/nn/'
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ips = soup.select('tr.odd > td:nth-of-type(2)')
    ports = soup.select('tr.odd > td:nth-of-type(3)')
    for ip, port in zip(ips, ports):
        data = {
            'http':ip.get_text() + ':' + port.get_text(),
        }
        ip_pool.append(ip.get_text() + ':' + port.get_text())

    # print(len(ip_pool))


    url1 = 'http://www.xicidaili.com/nt/'
    wb_data1 = requests.get(url1, headers=headers)
    soup1 = BeautifulSoup(wb_data1.text, 'lxml')
    ips1 = soup1.select('tr.odd > td:nth-of-type(2)')
    ports1 = soup1.select('tr.odd > td:nth-of-type(3)')
    for ip1, port1 in zip(ips1, ports1):
        ip_pool.append(ip1.get_text() + ':' + port1.get_text())
    return ip_pool


def get_good_ip():
    useble = []
    def ceshi(wangzhi,i):
        try:
            requests.get(wangzhi, proxies={"http":"http://" + str(i)}, timeout=3)
        except:
            print('fail')
        else:
            print (i + 'success')
            useble.append(i)
    ip_po = get_ip_pool()
    for i in (ip_po[0:12]+ip_po[50:61]):
        ceshi(wangzhi,i)
    return useble


def ip_pool():
    this_ips = str(get_good_ip())[1:]
    f = open('all_ip.txt','r')
    all_ip = f.read()
    f.close()

    last_li = []
    write_thing0 = all_ip[0:-1]+ ',' +this_ips
    # print (all_ip[0:-1])
    # print (this_ips)
    print (write_thing0)
    delete_w = eval(write_thing0)
    for i in delete_w:
        if i not in last_li:
            last_li.append(i)
    write_thing = str(last_li)

    last_txt = open('all_ip.txt','w')
    last_txt.write(write_thing)
    last_txt.close()

    f = open('all_ip.txt','r')
    all_ip = f.read()
    f.close()
    ip_list = eval(all_ip)
    print(len(ip_list))
    return ip_list

ip_pool()
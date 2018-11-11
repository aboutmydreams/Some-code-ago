import requests
wangzhi = 'http://www.shoujibiao.tk'


def get_good_ip():
    useble = []
    f = open('all_ip.txt','r')
    all_ip = f.read()
    f.close()
    ip_list = eval(str(all_ip))
    def ceshi(wangzhi,i):
        try:
            requests.get(wangzhi, proxies={"http":"http://" + str(i)}, timeout=4)
        except:
            print('fail')
        else:
            print (i + '---check--success!')
            useble.append(i)
    for i in ip_list:
        ceshi(wangzhi,i)
    return useble

def last_ip_pool():
    lll = []
    l1 = get_good_ip()
    for i in l1 :
        if i not in lll:
            lll.append(i)
    print (lll,len(lll))
    return lll

def last_good_ip():
    last_pool = last_ip_pool()
    last_ip = open('last_ip.txt','w')
    last_ip.write(str(last_pool))
    last_ip.close()
    return last_pool

# last_good_ip()
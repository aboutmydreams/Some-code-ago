import requests
import json,time
# a = input('输入cook')
# print(a)
print('开始运行收藏程序')
time_start=time.time()
def do(shop_id,coki):
    url = "http://www.dianping.com/member/jsonp/addFavor?referId={0}&favorType=1&favorTags=&_nr_force=1535360929048&callback=NR._JSONPCallback._1535360847450".format(shop_id)
    headers = {
        'Cookie': f'{coki}',
        'Host': 'www.dianping.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    r = requests.get(url=url, headers=headers)
    # print(r.status_code)
    return r.status_code


with open('data.txt','r') as a:
    al = eval(str(a.readlines()).replace('\\n','').replace('http://www.dianping.com/shop/',''))
coki = open('login.txt','r')
new_coki = coki.readlines()
cook = eval(str(new_coki).replace("', '",'').replace(' ','').replace('\\n',''))
ccc = eval(cook[0].replace('false','False').replace('true','True'))
all_coki = ''
for x in ccc:
    all_coki = all_coki + x['name'] + "=" + x['value'] + ';'
    # print(x)
# print(all_coki)

# do('20704590',all_coki)
n = 0
for i in al:
    num = do(i,all_coki)
    n = n+1
    time.sleep(0.8)
    if num is not 200:
        print('第{}条收藏 返回失败\n---------------------------------'.format(int(n)))
    else:
        print('第{}条收藏 返回成功\n---------------------------------'.format(int(n)))
time_end=time.time()
print('程序执行完成,总共用时：',time_end-time_start,'秒')
while 1 :
    pass
# if __name__ == '__main__':
#     do('16553276')






















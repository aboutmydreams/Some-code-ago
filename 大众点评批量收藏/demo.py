import requests
import json,time
# a = input('输入cook')
# print(a)
print('开始运行收藏程序')
time_start=time.time()
def do(shop_id,coki):
    url = "http://www.dianping.com/member/jsonp/addFavor?referId={0}&favorType=1&favorTags=&_nr_force=1535360929048&callback=NR._JSONPCallback._1535360847450".format(shop_id)
    headers = {
    'Cookie':'{}'.format(coki), #'_lxsdk_cuid=161097ef20cc8-026a91c539f6a9-454c092b-1fa400-161097ef20dc8; _lxsdk=161097ef20cc8-026a91c539f6a9-454c092b-1fa400-161097ef20dc8; _hc.v=c24072f3-5b28-8e83-a893-fc3924919482.1516282771; s_ViewType=10; ua=dpuser_4578030482; ctu=7316f47f76d33461338489f90afedee524be84feb919c9e52a7b665bb8d7712f; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cy=219; cye=dongguan; _dp.ac.v=8aa50786-51c2-4c90-a13e-a564ec3b4e61; thirdtoken=B52B27A8FEF0D3172B28F245DFAADA4F; uamo=18760361317; JSESSIONID=8915346D964B04291EE032DD3759859B; dper=0750d9c961196d6148a277a606607eb78b91921fff2ffd16229e1d6afaed5830e568cc55416f454de07ba3a1ea3d97428f980fc8d5f81061e4f51572438ddc417ac88a6603908a001da2590dca7adb62480a1488e56f54d5bd284dea746059f0; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=1657a82fa36-99f-f24-23f%7C%7C206',
    'Host': 'www.dianping.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
    # print(r.status_code)
    return r.status_code


a = open('data.txt','r')
al = eval(str(a.readlines()).replace('\\n','').replace('http://www.dianping.com/shop/',''))
a.close()
coki = open('login.txt','r')
new_coki = coki.readlines()
cook = eval(str(new_coki).replace("', '",'').replace(' ','').replace('\\n',''))
ccc = eval(cook[0].replace('false','False').replace('true','True'))
all_coki = ''
for x in ccc:
    pass
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






















import requests,pytesseract,time,json,random,re
from io import BytesIO
from PIL import Image,ImageDraw,ImageChops
from bs4 import BeautifulSoup



def get_coki(iii=None):#获取coki
    if iii is 0:
        url = 'http://passport2.chaoxing.com/num/code?'#'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fi.mooc.chaoxing.com%2Fspace%2Findex.shtml'
        headers0 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'passport2.chaoxing.com',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3386.1 Safari/537.36'
        }
        bd_session = requests.Session()
        what = bd_session.get(url,headers=headers0)
        #print(type(what.cookies))
        #soup = BeautifulSoup(what.text,'lxml')
        #titles = soup.select('img')
        #print(type(titles))
        #print(titles)
        #print(type(what.content))
        img = Image.open(BytesIO(what.content))
        img.show()
        aaa = input('验证码：')
        cookii = requests.utils.dict_from_cookiejar(what.cookies)
        real_coki = 'JSESSIONID='+str(cookii['JSESSIONID'])+'; route='+str(cookii['route'])#+'; fid=262; fanyamoocs=11401F839C536D9E; isfyportal=1'
        #print(real_coki)
        return str(aaa)+real_coki
    else:
        url = 'http://passport2.chaoxing.com/num/code?'#'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fi.mooc.chaoxing.com%2Fspace%2Findex.shtml'
        headers0 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'passport2.chaoxing.com',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3386.1 Safari/537.36'
        }
        bd_session = requests.Session()
        what = bd_session.get(url,headers=headers0)
        img = Image.open(BytesIO(what.content))
        im = img.convert('L')
        def initTable(threshold):
            table = []
            for i in range(256):
                if i < threshold:
                    table.append(0)
                else:
                    table.append(1)
            return table
        img1 = im.point(initTable(227), '1')
        #img1.show()
        text=pytesseract.image_to_string(img1,lang='chi_sim')
        text=text.replace('o','0')
        text=text.replace('O','0')
        text=text.replace('Q','0')
        text=text.replace(' ','')
        text=text.replace('l','1')
        text=text.replace('s','8')
        text=text.replace('!','1')
        text=text.replace('i','1')
        text = re.sub("\D", "", text)
        if len(text) != 4:
            return 4
        else:
            #aaa = input('验证码：')
            cookii = requests.utils.dict_from_cookiejar(what.cookies)
            real_coki = 'JSESSIONID='+str(cookii['JSESSIONID'])+'; route='+str(cookii['route'])#+'; fid=262; fanyamoocs=11401F839C536D9E; isfyportal=1'
            #print(real_coki)
            return str(text)+real_coki
#iii = 0 时手动输入验证码
#识别验证码


#登入
def login(user,psw,ii,iii=None):
    n = 0
    rn = 0
    rm = 0
    long_wrong = 0
    while rn < ii:
        cc = get_coki(iii)
        if cc is 4:
            long_wrong+=1
            continue
        else:
            cacha = cc[:4]
            ccc = cc[4:]
            url_login = 'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fi.mooc.chaoxing.com%2Fspace%2Findex.shtml'
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '213',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': f'{ccc}',
                'Host': 'passport2.chaoxing.com',
                'Origin': 'http://passport2.chaoxing.com',
                'Pragma': 'no-cache',
                'Referer': 'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fi.mooc.chaoxing.com%2Fspace%2Findex.shtml',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3386.1 Safari/537.36',
            }

            data = {
                'refer_0x001': 'http%3A%2F%2Fi.mooc.chaoxing.com%2Fspace%2Findex.shtml',
                'pid': '-1',
                'pidName': '',
                'fid': '-1',
                'fidName': '',
                'allowJoin': '0',
                'isCheckNumCode': '1',
                'f': '0',
                'productid': '',
                'uname': f'{user}',
                'password': f'{psw}',
                'numcode': f'{cacha}',
                'verCode': '',
            }

            new_re = requests.post(url_login,headers=headers,data=data,allow_redirects = False)#最后这个很重要
            if '验证码错误' in new_re.text:
                print('验证码错误,')
                            #return 444,444
            elif '密码错误' in new_re.text:
                print('用户名或密码错误，但至少验证码对了！')
                rn +=1
                            #return 400,400
            else:
                new_coki = requests.utils.dict_from_cookiejar(new_re.cookies)
                #print(new_coki)
                a_url = 'https://fystat-ans.chaoxing.com/log/setlog?uid=62546521&courseId=201101585&classId=3330936&encode=2c0221692a888aba6a86e1d243baaa74'
                a_coki = 'fid='+str(new_coki['fid'])+'; _uid='+str(new_coki['_uid'])+'; uf='+str(new_coki['uf'])+'; _d='+str(new_coki['_d'])+'; UID='+str(new_coki['UID'])+'; vc='+str(new_coki['vc'])+'; vc2='+str(new_coki['vc2'])+'; DSSTASH_LOG='+str(new_coki['DSSTASH_LOG'])
                a_headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Cookie': f'{a_coki}',
                    'Host': 'fystat-ans.chaoxing.com',
                    'Pragma': 'no-cache',
                    'Referer': 'https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=118675426&courseId=201101585&clazzid=3330936&enc=e4f3c70d02503adc42e2fb389ff3315d',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3386.1 Safari/537.36',
                }

                a_re = requests.get(a_url,headers=a_headers,allow_redirects = False)
                b_coki = requests.utils.dict_from_cookiejar(a_re.cookies)
                c_coki ='k8s='+str(b_coki['k8s'])+''+'fid='+str(new_coki['fid'])+'; _uid='+str(new_coki['_uid'])+'; uf='+str(new_coki['uf'])+'; _d='+str(new_coki['_d'])+'; UID='+str(new_coki['UID'])+'; vc='+str(new_coki['vc'])+'; vc2='+str(new_coki['vc2'])
                rm +=1
                rn +=1
                couse = str(random.randint(26,35))
                c_url = f'https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=1186754{couse}&courseId=201101585&clazzid=3330936&enc=e4f3c70d02503adc42e2fb389ff3315d'

                c_url0 = 'https://mooc1-1.chaoxing.com/mycourse/studentcourse?courseId=201101585&clazzid=3330936&ut=s&enc=e4f3c70d02503adc42e2fb389ff3315d'

                c_header = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Cookie': f'{c_coki}',
                    'Host': 'mooc1-1.chaoxing.com',
                    'Pragma': 'no-cache',
                    'Referer': 'http://passport2.chaoxing.com/login?refer=https%3A%2F%2Fmooc1-1.chaoxing.com%2Fmycourse%2Fstudentstudy%3FchapterId%3D118675426%26courseId%3D201101585%26clazzid%3D3330936%26enc%3De4f3c70d02503adc42e2fb389ff3315d&fid=145',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3386.1 Safari/537.36',
                }

                study = requests.get(c_url0,headers=c_header)
                if '学习进度' in study.text:#回到课程
                    nn = 1
                    print('页面成功了！！ 间隔%d秒，刷取%s次'%(nn,str(rm)))
                                    #nn = int(random.randint(0,5))
                                    #time.sleep(nn)
                else:
                    print(study.text)
                    #return c_coki,200
            n+=1
    print(
        f'验证码准确率是{str(rn/n)}',
        f'--命中率是{str(rm/n)}',
        f'长度错误有{str(long_wrong/(n+long_wrong))}%',
        f'识别准确率为{str(rn/(n+long_wrong))}',
    )
'''
def shua(username,pswd,ii,i=None):
    c_coki = login(username,pswd,ii)[1]
    n = 1
    nn = 1
    while c_coki is 200:
        c_coki = login(username,pswd)
shua('15170567059','abqqq111222',2)
'''

sta = time.clock()
#login('1827056{}'.format(random.randint(1000,9999)),'{}5648'.format(21,32142),5)
#login('15170567059','abqqq111222',3,0)#成功 0 是手动
login('15170567059','abqqq111222',2)#成功
end = time.clock()
print(f'消耗时长为 {str(end-sta)} s')








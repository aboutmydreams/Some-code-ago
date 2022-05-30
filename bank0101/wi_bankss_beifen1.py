#! -*- encoding:utf-8 -*-
import requests
import time,re,json,datetime,sys,random
from bs4 import BeautifulSoup
sys.path.append("find_ip")
import xici,ali_pr,check_ip


'''
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
'''


lll = ['农商合作', '农商青年社', '新农商网', '河南农商网', '山东农商网', '农商之家', '福建农商汇', '北农商新青年', '鄂北农商第1城', '金八桂农商大联盟', '乐清农商银行', '岑溪农商银行', '随州农商银行', '炎陵农商银行', '灵石农商银行', '松滋农商银行', '台前农商银行', '临猗农商银行', '白城农商银行', '河津农商银行', '公主岭农商银行', '路桥农商银行', '长垣农商银行', '盱眙农商银行', '桐柏农商银行', '渭滨农商银行', '衡东农商银行', '泗县农商银行', '桐城农商银行', '上虞农商银行', '德州农商银行', '湘乡农商银行', '珲春农商银行', '惠东农商银行', '宁都农商银行', '平原农商银行', '慈利农商银行', '万安农商银行', '长兴农商银行', '荆门农商银行', '景宁农商银行', '衡南农商银行', '龙泉农商银行', '六安农商银行', '乐陵农商银行', '乌拉特农商银行', '浦江农商银行', '阆中农商银行', '潜山农商银行', '五台农商银行', '惠州农商银行', '武城农商银行', '六盘水农商银行', '宜都农商银行', '仙居农商银行', '吴兴农商银行', '孟州农商银行', '咸宁农商银行', '岱山农商银行', '平江农商银行', '平利农商银行', '寿阳农商银行', '屯溪农商银行', '武乡农商银行', '太谷农商银行', '安塞农商银行', '休宁农商银行', '湘阴农商银行', '松阳农商银行', '长葛农商银行', '祁门农商银行', '紫阳农商银行', '涉县农商银行', '平顺农商银行', '托克托农商银行', '石首农商银行', '汝阳农商银行', '兴县农商银行', '岳阳农商银行', '兴山农商银行', '太白农商银行', '龙门农商银行', '怀来农商银行', '湄潭农商银行', '麻城农商银行', '孝感农商银行', '遂昌农商银行', '双峰农商银行', '黄石农商银行', '岚皋农商银行', '汝南农商银行', '常德农商银行', '麟游农商银行', '大安农商银行', '北安农商银行', '赤壁农商银行', '韶山农商银行', '益阳农商银行', '大悟农商银行', '5没有相关公众号 已跳过6没有相关公众号 已跳过只显示100农商青年', '只显示100农商青年', '只显示100襄垣农商行', '潞城农商行', '睢宁农商行', '壶关农商行', '清河农商行', '当阳农商行', '黎城农商行', '凤翔农商行', '黄梅农商行', '安化农商行', '靖安农商行', '子长农商行', '保靖农商行', '黄岩农商行', '土右农商行', '宋都农商行', '阳曲农商行黄寨支行', '阳曲农商行城关支行', '铜仁农商行江华支行', '大同北都农商行', '长治黎都农商行', '鹿城农商行卡中心', '九台农商行网络学院', '张店农商行怡海世家支行', '河源农商行时代花园社区银行', '温岭农商行团委', '东丰农商行微银行', '晋城农商行微客服', '农商行', '农商行研究', '农商行金珠', '农商行锦绣', '农商行徐小琴', '农商行体育街', '颍上农商行', '贞丰农商行', '农商行五路居分理处', '南皮农商行', '蕲春农商行', '农商行小邓', '绥芬河农商行', '农商行吉劳庆支行', '农商行小望', '茌平农商行', '长子农商行', '鸡西农商行', '吉首农商行', '利津农商行', '阜宁农商行', '农商行开县汉丰贷款中心', '晋城农商行南城行', '保康农商行', '襄垣农商行财富直通车', '凤阳农商行', '鹿农商行营业部', '农信社农商行考试', '泽州农商行金村支行', '静宁农商行简讯', '襄垣农商行城关支行', '长春农商行大马路支行', '陕坝农商行营业部', '泽州农商行营业部', '东营农商行淮河路分理处', '石林农商行', '晋城农商行东城行', '河源农商行雅居乐社区银行', '长治农商行融泰支行', '泽州农商行新市东街支行', '北京农商行天通苑财富管理', '鄂尔多斯农商行伊西', '阜南农商行天棚行', '叙永农商行放心贷', '陕坝农商行跃进支行', '繁昌农商行三山支行', '长治农商行大北街支行', '长治黎都农商行营业部', '晋城农商行总行营业部', '潜山农商行黄柏支行', '鄂尔多斯农商行祥泰', '襄垣农商行太行路支行', '临清农商行古城', '鄂尔多斯农商行创业', '长治农商行消费e贷', '萍乡农商行', '荆州农商行沙市支行', '长春农商行绿园支行', '浙江苍南农商行订阅号', '白河农商行案防', '江南农商行春江支行', '临城农商行', '乡宁农商行西坡支行', '晋城农商行景西行', '吉安农商行信贷小百科', '长治农商行延中支行', '吉安农商行微社区', '建德农商行保全中心', '鄂尔多斯农商行长青支行', '鄂尔多斯农商行东兴', '潞城农商行山化分理处', '余杭农商行崇贤支行', '只显示100乐清农商银行', '通山农商银行', '鹿邑农商银行', '郴州农商银行', '老河口农商银行', '定州农商银行', '徽州农商银行', '南漳农商银行', '榆社农商银行', '广水农商银行', '南县农商银行', '新宁农商银行', '交城农商银行', '云和农商银行', '定西农商银行', '沙县农商银行', '千阳农商银行', '偃师农商银行', '嵊泗农商银行', '只显示100淮安农村商业银行', '郯城农村商业银行', '凯里农村商业银行订阅号', '新沂农村商业银行', '广丰农村商业银行', '安顺农村商业银行', '来凤农村商业银行', '慈溪农村商业银行', '华容农村商业银行', '山阴农村商业银行', '贺兰农村商业银行', '澧县农村商业银行', '中宁农村商业银行', '安乡农村商业银行', '潜江农村商业银行', '汕尾农村商业银行', '临澧农村商业银行', '绛县农村商业银行', '民勤农村商业银行', '辉南农村商业银行', '闻喜农村商业银行', '鄂州农村商业银行', '庐江农村商业银行', '方正农村商业银行', '安图农村商业银行', '花垣农村商业银行', '晴隆农村商业银行', '宁海农村商业银行', '天柱农村商业银行', '龙山农村商业银行', '共和农村商业银行', '余杭农村商业银行', '吉林汪清农村商业银行', '贵州紫云农村商业银行', '湖北竹溪农村商业银行', '陕西陇县农村商业银行', '湖北丹江口农村商业银行', '湖北郧西农村商业银行', '湖北武当山农村商业银行', '贵州惠水农村商业银行', '江苏灌云农村商业银行', '山西襄汾农村商业银行', '山西洪洞农村商业银行', '湖南汉寿农村商业银行', '山东阳谷农村商业银行', '高要农村商业银行客户服务', '陕坝农村商业银行', '博山农村商业银行股份有限公司', '察右前旗农村商业银行', '武汉农村商业银行', '河套农村商业银行', '普陀农村商业银行', '杨凌农村商业银行', '太仆寺农村商业银行', '扶绥农村商业银行', '江陵农村商业银行', '隆昌农村商业银行', '那坡农村商业银行', '黄河农村商业银行营业部', '安徽旌德农村商业银行', '江南农村商业银行靖江支行', '江苏丰县农村商业银行', '黟县农村商业银行', '宜春农村商业银行', '利川农村商业银行', '湖北五峰农村商业银行', '双牌农村商业银行', '宣恩农村商业银行', '武威农村商业银行', '吴忠农村商业银行', '湖南桑植农村商业银行', '广东河源农村商业银行', '新乡平原农村商业银行', '通城农村商业银行', '吉林通化海科农村商业银行', '汝城延寿农村商业银行', '灌云农村商业银行微贷中心', '龙山农村商业银行苗市支行', '湖南城步农村商业银行股份有限公司', '江西共青农村商业银行', '营口农村商业银行股份有限公司', '济南农村商业银行马山支行']


def get_today_time():
    year = str(time.localtime().tm_year)
    mon = str(time.localtime().tm_mon)
    if len(mon) is 1:
        mon = f'0{mon}'
    day = str(time.localtime().tm_mday)
    if len(day) is 1:
        day = f'0{day}'
    return year+mon+day

def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    return str(today-oneday).replace('-','')


def collect_links(id_name,cookie=None):
    if not cookie:
        cookie = ''
    def ten_links(url,nnn=3,header=None):
        res = ali_pr.ali_proxies(url,header)
        soup1 = BeautifulSoup(res.text,'html.parser')
        # print(soup1)
        title = soup1.findAll("script", {"type": "text/javascript"}, text = re.compile('.*var msgList.*'))
        # json1 = json.loads(re.findall('var msgList.*?\n', str(title))[0][14:-2])
        if nnn>=5:
            return '用户您好，您的访问过于频繁'
        if '验证' in str(soup1):
            print(f'spd {id_name} again')
            time.sleep(2)
            nnn +=1
            return ten_links(url,nnn)
        else:
            years_today_title = ' '
            try:
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
                    real_time = str(the_time)[:12].replace('--', '')
                    if int(real_time) == int(getYesterday()):
                        years_today_title = years_today_title + the_title
            except IndexError:
                time.sleep(2)
                print(f'IndexError------76hang{str(soup)}')
                nnn +=1
                return ten_links(url,nnn)
                        # print (real_time)
                        # lin = lin+'【标题】：'+ the_title + '\n' + '【标题链接】：https://mp.weixin.qq.com' + the_url + '\n' + '【摘要】：' + digest + '\n' + '【发布时间】：' + the_time + '\n'
            # print (lin)
            # return lin
            return years_today_title
        # except IndexError as e:
        #     print (e)
        #     return '需要验证'
        # except ValueError:
        #     pass



    # s = requests.session()
    try:
        url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query={}'.format(id_name)
        #print(requests.get(url).text)#测试是否包含需要的数据
        res = ali_pr.ali_proxies(url)
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
                return str(id_name)+'没有相关公众号 已跳过' +str(soup)
            try:
                # print(id_link[0].get("href").replace(';','&'))#测试连接有效性 有效
                # print(id_link)
                # print (soup)
                cookies1 = requests.utils.dict_from_cookiejar(res.cookies)
                cookie2 = str(cookies1)[2:-2].replace("': '","=").replace("', '",';')
                one_link = id_link[0].get("href").replace(';','&')
                one_title = id_link[0].get_text()
                wi_id = str(weixin_id[0].get_text())
                print (wi_id)
                print(str(id_name)+" 链接是："+str(one_link)+'\n')
                #等待
                time.sleep(10+random.randint(2,5))
                yes_title = ten_links(one_link,3)
                last_f.write('【微信名】：' + one_title +'\n' + '【微信id】：' + wi_id + '\n' + yes_title+ '\n\n'+str(one_link))
                last_f.close()
                return yes_title,one_link
            except (TypeError or IndexError) as e:
                print(e)
                return str(i)+'没有相关公众号 已跳过'
    except:
    	pass
    	return '443'
# collect_links('北京航空大学')

def all_title_and_link():
    all_yes_title = ''
    all_links = []
    error_n = 0
    for i in lll[40:55]:
        try:
            link = collect_links(i)
            all_yes_title = all_yes_title+link[0]
            all_links.append(link[1])
            time.sleep(1)
            if '已跳过' in link:
                error_n = error_n+1
                print(f'这是第{str(error_n)}条空的公众号，已跳过，不会保存相关txt，随便提一下，如果查询公众号中有重复只会保存一次txt')
                print(f'也可能是ip被封 可以查看soup是否乱码：{str(link)}')
                    #time.sleep(0.6)
        except requests.exceptions.ProxyError as e:
            print (e)
        except Exception:
            print (i,lll.index(i))
            raise
        finally:
            pass
    all_links_txt = open('last_all_links.txt','a')
    all_links_txt.write(str(all_links))
    all_yes_title_txt = open('all_yes_title.txt','a')
    all_yes_title_txt.write(all_yes_title)
    return all_yes_title,all_links

#print (all_title_and_link())
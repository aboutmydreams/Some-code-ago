#! -*- encoding:utf-8 -*-
import requests,re,json,time
from bs4 import BeautifulSoup
what_name = open('wx-res.txt','r')
# id_list = ['北京航空航天大学', '航空知识', '航空知识', '看航空', '航空制造网', '郑州航空港区', '中国民用航空网', '中国航空报', '飞行总动员航空网', '航空无损检测砖家', '航空', '航空大话', '国际航空', '航空科普', '中设航空', '航空奥秘', 'i航空', '航空1909', '锐格航空', '航空航模', '航空之家', 'i看航空', '航空工业', '航空圈', '航空飞行', '航空领域', '航空技术', '航空航天港', 'Galleon航空资讯', 'Himor黑马航空', '六爷侃航空', '航空与航天', 'AS9100航空航天', 'Geyes航空影像采集', '成都翔飞航空', '星晟航空科技', '航空工业惠阳', '航空工业计算所', '复旦航空航天系', '蔚蓝航空无人机', '智翔航空科技', 'GIS航空数据处理', '三丰航空科技', '航空之家官方', '航空工业导弹院', '腾隆通用航空', '华美航空科技', '哞哞航空公司', '尊翔公务航空', '兴中航空集团', '美国联合航空', '中孚航空科技', '航空航天世界', '南方航空公司', '中国航空学会', '民航空管工会', '马来西亚航空', '雄鹰通用航空', '中海航通用航空', 'CTA外航空乘之家', '东方航空杭州', '航空工业哈飞', '德润航空科技', '空联航空电子', '宇联航空设备', '翼枫航空科技', '中国东方航空', '中国联合航空', '行翼航空科技', '国际航空快讯', 'CAUC航空航天学会', '航空器材资讯', '航空力学检测', '汕头衡山航空', '航空静电喷雾', '全球航空资讯', '柬埔寨巴戎航空', '天翔航空科技', '金丰春航空科技', '凤翔通用航空', '航空与法律政策', '桂林航空航卫', '正元航空遥感', '江弘航空器材', '航空工业强度所', '航空维修与工程', '卡塔尔航空公司', '远润航空科技', '斯里兰卡航空公司', '北部湾航空技术支援', '西安航空基地建设管理', '无人机航空遥感联盟', '安徽省航空科普协会', '陕西西北通用航空协会', '河北福尔通用航空公司', '胜景国际航空服务公司', '航空电信产业论坛', '阿姆斯壮航空科技', '广西凤翼天翔航空', '东海航空技术交流', '鬼谷通用航空政策分析', '北京通用航空公司', '通用航空产业发展联盟', 'CAUC航空发动机构造', '襄阳新纵深航空科技', '亚洲航空发展研究学会', '亚洲商务航空协会AsBAA', '珠海羽人农业航空', '艾仕达尔航空科技', '航空大都市研究院', '航空发动机转子结构', '巴西航空工业公司', '祥鹏航空运行控制部', '四川航空杭州运行基地', '民用航空技术分院', '汽车航空航天工程', '阿克苏神龙航空无人机', '华飞航空发展集团', '重庆市通用航空协会', '金丝路凤凰通用航空', '沈阳沈飞航空博览园', '鹏航航空有限公司', '通用航空产业发展联盟', '陕西腾龙航空技术装备有限公司', '中国航空技术广州有限公司', '唐山联旺通用航空有限公司', '瑞安市飞云航空服务有限公司', '四川豪芸通用航空有限公司', '山东云翼航空科技有限公司', '北京顺天通达航空服务有限公司', '中国航空安全自愿报告系统', '中国海洋航空集团有限公司', '北京航空华北汽车贸易有限公司', '成都全海航空技术有限公司', '北京亚联通用航空股份有限公司', '中航国际航空发展有限公司', '中建一局郑州航空港建设项目', '北京丽翔航空服务有限公司', 'CIBAS北京国际商务航空展览会', '成都航院航空制造工程系', '中国民用航空华北地区管理局', '青岛直升机航空有限公司', '长龙航空地面服务部现场监管', '江苏天鹰通用航空有限公司', '广东翔泰通用航空有限公司', '郑州浩普航空科技有限公司', '中国通用航空服务有限公司', '山东齐天翼航空科技有限公司', '贵州红都通用航空有限公司']
id_list = eval(str(what_name.readlines()).replace('\\n',''))#读取数据为元组
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




all_id_link = []
def collect_links(id_name,cookie=None):
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
        # print(soup)查看数据的有无
        if id_link == []:
            return str(i)+'没有相关公众号 已跳过'
        try:
            # print(id_link[0].get("href").replace(';','&'))#测试连接有效性 有效
            one_title = id_link[0].get_text()
            wi_id = str(weixin_id[0].get_text())
            # print (wi_id)
            # print(str(i)+" 链接是："+str(one_link)+'\n')#微信公众号<#>微信ID
            last_all = ''
            last_all = last_all +  one_title + '<#>' + wi_id +'\n'#字符串的拼接
            return last_all
        except (TypeError or IndexError) as e:#找出报错且继续运行代码
            print(e)
            return str(i)+'没有相关公众号 已跳过'
# collect_links('北京航空大学') 测试一个爬取




all_links = []
error_n = 0
last_name = '微信公众号<#>微信ID\n'
for i in id_list:
    try:
        link = collect_links(i)
        last_name = last_name + link
        time.sleep(0.5)
        if '已跳过' in link:
            error_n = error_n+1
            print('这是第'+ str(error_n) +'条空的公众号，已跳过，不会保存相关txt，随便提一下，如果查询公众号中有重复只会保存一次txt')#建立可读输出
        else:
            pass

    except (requests.exceptions.ProxyError or requests.exceptions.SSLError) as e:#找出报错且继续运行代码
        print (e,'断网了，请确定在有网络的环境下运行')
        pass



#写入文件
last_txt = open('last.txt','w')
last_txt.write(last_name)
last_txt.close()
print('已成功爬取')



#-*- coding: UTF-8 -*-
import time,jieba,flask
import jieba.analyse,wi_bankss

with open('all_yes_title.txt','r') as f:
    texts = f.read().replace('again1','').replace(' ','')
# print(texts)


def remove(text,topnum,weight=None):#分词、去停用词、前top n个关键词
    #第一步：分词，这里使用结巴分词全模式
    fenci_text = jieba.cut(text)
    #print("/ ".join(fenci_text))

    #第二步：去停用词
    #这里是有一个文件存放要改的文章，一个文件存放停用表，然后和停用表里的词比较，一样的就删掉，最后把结果存放在一个文件中
    stopwords = {}.fromkeys([ line.rstrip() for line in open('stopwd.txt') ])
    final = ""
    for word in fenci_text:
        if word not in stopwords and word not in ["。", "，"]:
            final = f"{final} {word}"
    print(final)

    #第三步：提取关键词
    #a=jieba.analyse.extract_tags(text, topK = 5, withWeight = True, allowPOS = ())
    if weight:
        a=jieba.analyse.extract_tags(final, topK = topnum, withWeight = True,allowPOS = ())
        print('1')
    else:
        a=jieba.analyse.extract_tags(final, topK = topnum,allowPOS = ())

    return a
    #text (final)为待提取的文本
    # topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
    # withWeight:是否一并返回关键词权重值，默认值为False。
    # allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。

'''
print(len(lines))
pbm =[]#疑问列表
for line in lines:
    line0 = line.strip().strip(' ').strip('')
    site = line0[::-1].find('】')
    line1 = line0[-site:]
    if ("?" in line1 or '吗' in line1 or '？' in line1 or '是不是' in line or '会不会' in line or '怎么' in line1) and line1[-1] != ')' and 5<len(line1)<20:
        pbm.append(line1)


toplong = len(pbm)//3
print(len(pbm))
pbmstr = ''.join(pbm)
keys = remove(pbmstr,toplong,1)#,1)
print(keys)
'''

# print(remove(texts,30,1))



def last_wd():
    wds = remove(texts,150,1)
    keyname = str(wi_bankss.getYesterday())
    print(keyname)
    with open(f'keys/{keyname}.txt', 'w') as f:
        f.write(str(wds))
    return wds


def get_lastwd():
    # 读取文本
    pythonInfo = open('all_yes_title.txt', 'r',  errors='ignore').read().replace('again1','')#encoding='utf-8',
    if len(pythonInfo)<100:
        pythonInfo = (pythonInfo+pythonInfo+pythonInfo).replace('   ','')
    print(pythonInfo)
    # 切割
    pythonCut = jieba.cut(pythonInfo, cut_all=True)
    pythonInfoList = ' '.join(pythonCut)  # 返回一个生成器对象
    try:
        keyname = str(wi_bankss.getYesterday())
        a_key=jieba.analyse.extract_tags(pythonInfo, topK = 100, withWeight = True,allowPOS = ())
        with open(f'keys/{keyname}.txt', 'w') as ks:
            ks.write(str(a_key))
        return f'<p>关键词参考：{str(a_key)}</p><br>'
    except ValueError as e:
        return '关键词太少'
    finally:
        pass
# print(last_wd(),get_lastwd())

# encoding:utf-8
import requests,json
from bs4 import BeautifulSoup
url = 'http://139.199.169.159:100/keys'
ps = requests.get(url)
soup = BeautifulSoup(ps.text,'lxml')

ppp = soup.select('body > p')
pi = 0
p_list = []
i_side = [0]
ps = len(ppp)
for i in range(ps):
    pcontent = ppp[i].get_text()
    if 'a' in pcontent:
        i_side.append(i)
    p_list.append(pcontent)
# print(i_side)
all_data = {'time': p_list[0]}
now_i = 1

for i in i_side[1:]:
    n1 = p_list[i].index('(')
    n2 = p_list[i].index(')')
    t_list = p_list[now_i+1:i]
    t_list.insert(0,p_list[i][n1+1:n2])
    all_data[f'{p_list[i][1:n1]}'] = t_list
    now_i = i

# print(all_data)
js = json.dumps(all_data, ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ':'))
# print(js)

he_data = {
    '其他':['银行','进万家','微贷','活禽','金秋','知识','积极开展','感恩','金融','活动','覆盖','系列','宣传','迎国庆','热烈庆祝','反假','岑溪','只花','挥一挥','智造','牟庄','销全','我来','','乐享','强服','新攻势','教师节','岱山','主城区','松滋','献礼','我行','荆门','年度报告','普惠','宰杀','白城','分钱','平江','德州','来袭','重磅','快报','相伴','授信','定点','中秋','专题','全县','我市','金融服务','开业','出行','三级','周年','社区','专项','轻轻地','开辟','零售','绿色','平安','商业银行','湖北','一路','典型','带动','手机','农村','体系','推进','贷款','人民币','服务','货币','正式','有限公司','成立','建设','股份','产品','工作','识破','农信','博会','五台','快讯','风采','名家','山西','众多','阖家团圆','衡南','五商','祝您','快乐','乌拉特','袭云','闪付','玩转','恭祝','签收','篮球赛','大礼包','广大客户','假币','双节','奔放','飞扬','中秋节','宜昌','第三届','社会各界','同庆','震撼','瞬间','精彩','魅力','激情','营销','职工','国庆','优惠','朋友','系统','生活','商行','进校园','公告','践行','红包','惠州','支行','温州','调研','展播','清收','丰溪','客都','德克士','恭喜发财','松阳','确权','那坡农','苍南','随贷','金燕','树正气','专题学习','超多','更容','壶行','不动户','泉溪','好礼','汤志勇','只鹿','金普月','CCCB','微信','随用','欢度国庆','竹溪','千只','大马路','浓浓','教育','边贸','临猗','廉政建设','子长','潞城','新鲜出炉','这厢','大吉大利','石首','美好生活','丰县','之恋','廉政','攻略','纪律处分','有礼','乐陵','莅临','钱袋子','反洗钱','丹江口','再出','党建','第三期','抽奖','一鼓作气','影城','共青团','服务质量','太白','贴心','飓风','中奖','放假','一曲','重阳','收下','好评','丰收','座谈会','集资','公积金','防线','全城','城南','泰山','国庆节','警示','党委书记','工地','视频','超市','本期','普及','理财产品','市委','清理','小区','非法','条例','九月','免费','防范','结算','一行','营业部','武汉','动态','中国共产党','流动','董事长','住房','理财','能量','指导','一生','每日','江苏','主题','一座','新闻','长假','清非','德慈','吉湖安武','只徽','乐哉乐','只河','停歇','钱包','事关','好消息','诚信','路上','信合','亿湖江','只凯','双江','征文','美滋滋','攻坚','当阳','百日','宝鸡','礼品','改革开放','上班','存款','疯狂','一大','正确','突破','结束','方式','银行','南安','上线','平原','接力赛','暂停','长垣','年度','校园','保卫','关于','员工','轻松','最酷','衡东','新沂','保管箱','x','压降','新汇路','破窗','巨献','降准','顺鑫','行动','祁门','召开','武乡','黟县','安全','南漳','紫云','鼓起来','大洪山','屯溪','宜都','重拳出击','选择','洗钱','借势','比武','党员干部','厚望','组织','关注','特质','全自动','倾心','全力以赴','台前','必备','注意事项','录用','淮安','新版','不良贷款','保本','分期','假日','公示','家园','守护','练兵','史诗','清算','装修','浮动','竞赛','技能','合法权益','做过','风景区','促成','流程','增添','开始','引领','节后','全民','满血','抢银行','深入','专项斗争','四季度','扫码','李建福','苏果','调度会','岭商','年化','金桐','一图','总结暨','减三健','焕新','周云荣','.%','隆利丰','共赢','海科','简章','摸准','公主岭','寒露','襄汾','睢宁','升级版','联社','河津','头条','半价','大悟','工作思路','凯里','节气','扶贫','先得','有道','安顺','鄂尔多斯','脉搏','狂欢','天神','管理工作','夯实','复活','秒杀','笔记','走访','对接','工作','火热','制服','第一天','贯彻落实','福利','先到','知道','秋天','每周','仪式','美丽','贵州','十月','宣讲','满堂红','冲刺','聚焦','旺季','周转金','初心','欲购从速','树形象','八十天','阿亮','农业户口','院级','故事','刘建鸿到','包片','名新','招新','会公','陕坝','土右农','便易贷','年股','双百','到底','郧西','四化','讲习','保康','李涛','限时','全面','右旗','深入基层','心系','动员会','大讲堂','汝阳','促发展','郯城','老房子','党委委员','新起点','取款','金红利','征程','税法','六安','习近平','会议','揭秘','帮扶','山阴','推广应用','难关','例会','高新区','汝南','缴费','十月份','抢购','哪天','不忘','银行存款','敲定','督办','慰问','点击','模块','还款','优秀','刷起','学院','天道酬勤','每周五','银监','小姐姐','喜临门','网络','拍卖公告','孝昌县','告白','党日','提质','郑德荣','德得轩','生日会','石教峰','环南','滴灌','脱贫致富','三折','广告语','九台','十堰','闻喜','抵押物','桑植','内功','电影票','活水','潜江','重阳节','征信','太仆寺','退款','一万元','政法','舒心','超高','普陀','返乡','认清','定期存款','骗局','精准','问答','修炼','联席会议','线上','那句话','陪伴','一分钟','公务','分局','河套','温馨','两张','共产党员','背叛','西瓜','奋斗','征集','园林','领取'],
    '节日':['中秋节','迎国庆','寒露','教师节','重阳节','国庆','中秋','重阳','国庆节','迎国庆','中秋节']
}
he_key = {}
for key in he_data:
    key_list = []
    for akey in he_data[key]:
        if akey in all_data:
            key_list.extend(all_data[akey][1:])
    # print(key,key_list)
    he_key[f'{key}'] = key_list
print(he_key)


#-*- coding: UTF-8 -*-
import time,datetime,json
from flask import Flask,redirect,url_for
import wordcloud #导入词云
from wordcloud import STOPWORDS  # 停止词
import jieba
import jieba.analyse
import base64
import numpy as np  # 科学计算
from matplotlib import pyplot as plt
from PIL import Image  # 图片处理
app = Flask(__name__)

lll = ['农商合作', '农商青年社', '新农商网', '河南农商网', '山东农商网', '农商之家', '福建农商汇', '北农商新青年', '鄂北农商第1城', '金八桂农商大联盟', '乐清农商银行', '岑溪农商银行', '随州农商银行', '炎陵农商银行', '灵石农商银行', '松滋农商银行', '台前农商银行', '临猗农商银行', '白城农商银行', '河津农商银行', '公主岭农商银行', '路桥农商银行', '长垣农商银行', '盱眙农商银行', '桐柏农商银行', '渭滨农商银行', '衡东农商银行', '泗县农商银行', '桐城农商银行', '上虞农商银行', '德州农商银行', '湘乡农商银行', '珲春农商银行', '惠东农商银行', '宁都农商银行', '平原农商银行', '慈利农商银行', '万安农商银行', '长兴农商银行', '荆门农商银行', '景宁农商银行', '衡南农商银行', '龙泉农商银行', '六安农商银行', '乐陵农商银行', '乌拉特农商银行', '浦江农商银行', '阆中农商银行', '潜山农商银行', '五台农商银行', '惠州农商银行', '武城农商银行', '六盘水农商银行', '宜都农商银行', '仙居农商银行', '吴兴农商银行', '孟州农商银行', '咸宁农商银行', '岱山农商银行', '平江农商银行', '平利农商银行', '寿阳农商银行', '屯溪农商银行', '武乡农商银行', '太谷农商银行', '安塞农商银行', '休宁农商银行', '湘阴农商银行', '松阳农商银行', '长葛农商银行', '祁门农商银行', '紫阳农商银行', '涉县农商银行', '平顺农商银行', '托克托农商银行', '石首农商银行', '汝阳农商银行', '兴县农商银行', '岳阳农商银行', '兴山农商银行', '太白农商银行', '龙门农商银行', '怀来农商银行', '湄潭农商银行', '麻城农商银行', '孝感农商银行', '遂昌农商银行', '双峰农商银行', '黄石农商银行', '岚皋农商银行', '汝南农商银行', '常德农商银行', '麟游农商银行', '大安农商银行', '北安农商银行', '赤壁农商银行', '韶山农商银行', '益阳农商银行', '大悟农商银行', '农商青年', '襄垣农商行', '潞城农商行', '睢宁农商行', '壶关农商行', '清河农商行', '当阳农商行', '黎城农商行', '凤翔农商行', '黄梅农商行', '安化农商行', '靖安农商行', '子长农商行', '保靖农商行', '黄岩农商行', '土右农商行', '宋都农商行', '阳曲农商行黄寨支行', '阳曲农商行城关支行', '铜仁农商行江华支行', '大同北都农商行', '长治黎都农商行', '鹿城农商行卡中心', '九台农商行网络学院', '张店农商行怡海世家支行', '河源农商行时代花园社区银行', '温岭农商行团委', '东丰农商行微银行', '晋城农商行微客服', '农商行', '农商行研究', '农商行金珠', '农商行锦绣', '农商行徐小琴', '农商行体育街', '颍上农商行', '贞丰农商行', '农商行五路居分理处', '南皮农商行', '蕲春农商行', '农商行小邓', '绥芬河农商行', '农商行吉劳庆支行', '农商行小望', '茌平农商行', '长子农商行', '鸡西农商行', '吉首农商行', '利津农商行', '阜宁农商行', '农商行开县汉丰贷款中心', '晋城农商行南城行', '保康农商行', '襄垣农商行财富直通车', '凤阳农商行', '鹿农商行营业部', '农信社农商行考试', '泽州农商行金村支行', '静宁农商行简讯', '襄垣农商行城关支行', '长春农商行大马路支行', '陕坝农商行营业部', '泽州农商行营业部', '东营农商行淮河路分理处', '石林农商行', '晋城农商行东城行', '河源农商行雅居乐社区银行', '长治农商行融泰支行', '泽州农商行新市东街支行', '北京农商行天通苑财富管理', '鄂尔多斯农商行伊西', '阜南农商行天棚行', '叙永农商行放心贷', '陕坝农商行跃进支行', '繁昌农商行三山支行', '长治农商行大北街支行', '长治黎都农商行营业部', '晋城农商行总行营业部', '潜山农商行黄柏支行', '鄂尔多斯农商行祥泰', '襄垣农商行太行路支行', '临清农商行古城', '鄂尔多斯农商行创业', '长治农商行消费e贷', '萍乡农商行', '荆州农商行沙市支行', '长春农商行绿园支行', '浙江苍南农商行订阅号', '白河农商行案防', '江南农商行春江支行', '临城农商行', '乡宁农商行西坡支行', '晋城农商行景西行', '吉安农商行信贷小百科', '长治农商行延中支行', '吉安农商行微社区', '建德农商行保全中心', '鄂尔多斯农商行长青支行', '鄂尔多斯农商行东兴', '潞城农商行山化分理处', '余杭农商行崇贤支行', '乐清农商银行', '通山农商银行', '鹿邑农商银行', '郴州农商银行', '老河口农商银行', '定州农商银行', '徽州农商银行', '南漳农商银行', '榆社农商银行', '广水农商银行', '南县农商银行', '新宁农商银行', '交城农商银行', '云和农商银行', '定西农商银行', '沙县农商银行', '千阳农商银行', '偃师农商银行', '嵊泗农商银行', '淮安农村商业银行', '郯城农村商业银行', '凯里农村商业银行订阅号', '新沂农村商业银行', '广丰农村商业银行', '安顺农村商业银行', '来凤农村商业银行', '慈溪农村商业银行', '华容农村商业银行', '山阴农村商业银行', '贺兰农村商业银行', '澧县农村商业银行', '中宁农村商业银行', '安乡农村商业银行', '潜江农村商业银行', '汕尾农村商业银行', '临澧农村商业银行', '绛县农村商业银行', '民勤农村商业银行', '辉南农村商业银行', '闻喜农村商业银行', '鄂州农村商业银行', '庐江农村商业银行', '方正农村商业银行', '安图农村商业银行', '花垣农村商业银行', '晴隆农村商业银行', '宁海农村商业银行', '天柱农村商业银行', '龙山农村商业银行', '共和农村商业银行', '余杭农村商业银行', '吉林汪清农村商业银行', '贵州紫云农村商业银行', '湖北竹溪农村商业银行', '陕西陇县农村商业银行', '湖北丹江口农村商业银行', '湖北郧西农村商业银行', '湖北武当山农村商业银行', '贵州惠水农村商业银行', '江苏灌云农村商业银行', '山西襄汾农村商业银行', '山西洪洞农村商业银行', '湖南汉寿农村商业银行', '山东阳谷农村商业银行', '高要农村商业银行客户服务', '陕坝农村商业银行', '博山农村商业银行股份有限公司', '察右前旗农村商业银行', '武汉农村商业银行', '河套农村商业银行', '普陀农村商业银行', '杨凌农村商业银行', '太仆寺农村商业银行', '扶绥农村商业银行', '江陵农村商业银行', '隆昌农村商业银行', '那坡农村商业银行', '黄河农村商业银行营业部', '安徽旌德农村商业银行', '江南农村商业银行靖江支行', '江苏丰县农村商业银行', '黟县农村商业银行', '宜春农村商业银行', '利川农村商业银行', '湖北五峰农村商业银行', '双牌农村商业银行', '宣恩农村商业银行', '武威农村商业银行', '吴忠农村商业银行', '湖南桑植农村商业银行', '广东河源农村商业银行', '新乡平原农村商业银行', '通城农村商业银行', '吉林通化海科农村商业银行', '汝城延寿农村商业银行', '灌云农村商业银行微贷中心', '龙山农村商业银行苗市支行', '湖南城步农村商业银行股份有限公司', '江西共青农村商业银行', '营口农村商业银行股份有限公司', '济南农村商业银行马山支行']


def get_timemin():
    now_time0 = '[\''+time.ctime().replace(':','\',\'').replace(' ','\',\'')+'\']'
    now_time = eval(now_time0)
    return now_time

def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=str(today-oneday).replace('-','')
    return yesterday

def day_before_Yesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=str(today-oneday-oneday).replace('-','')
    return yesterday

def get_key():
    pass
    if get_timemin()[3] in ['00','01','02','03','04','05','06','07','08','09']:
        keyname = str(day_before_Yesterday())
        f = open('keys/{}.txt'.format(keyname),'r')
        f_reads = eval(str(f.read()))
        f.close()
        return f_reads,keyname
    else:
        keyname = str(getYesterday())
        f = open('keys/{}.txt'.format(keyname),'r')
        frd = f.read()
        # print(type(frd))
        f_reads = eval(frd)
        f.close()
        return f_reads,keyname


@app.route('/keyword', methods=['GET'])
def sure_yzm():
    pass
    if get_timemin()[-4] in ['00','01','02','03','04','05','06','07','08','09']:
        keyname = str(day_before_Yesterday())
        f = open('keys/{}.txt'.format(keyname),'r')
        f_read = keyname+f.read()
        f.close()
        return f_read
    else:
        keyname = str(getYesterday())
        f = open('keys/{}.txt'.format(keyname),'r')
        f_read = keyname+f.read()
        f.close()
        return f_read

@app.route('/title', methods=['GET'])
def set_tit():
    all_tt = ''
    for i in lll:
        txt_f = open('new_file/{}.txt'.format(i),'r',encoding='UTF-8')
        txt_line = txt_f.readlines()
        #print(txt_line)
        #print(len(txt_line)) 5  or 0
        if len(txt_line)>=2:
            title0 = txt_line[2].replace('again1','').replace('\\n','').replace(' ','')
            txt_link = txt_line[3].replace('https://mp.weixin.qq.comagain1\\n','')
            # print(title0+'100000000000000000000')
            if len(title0) > 2:
                # print(title0+'100000000000000000000')
                all_tt = all_tt + i + ':' + title0 + '\n'+'<br>' + '链接：' + txt_link+ '\n'+'<br>'
            else:
                all_tt = all_tt + i + ':' + title0 + '\n'+'<br>'

    return all_tt

@app.route('/keys', methods=['GET'])
def get_key_tt():
    aaa = get_key()
    keyss = []
    las_tt = '{}<br>'.format(aaa[1])
    for aa in aaa[0]:
        keyss.append(aa[0])
    print(keyss)
    all_tt = '<!DOCTYPE html><html><head><title>关键词下的标题</title><style type="text/css">*{margin: 0;padding: 0;}</style>'
    for ii in keyss[0:20]:
        print(ii)
        begin_n = 0
        # all_tt = all_tt + '<p>{}'.format(ii) +':-------------------------------------------------------------------------------------------------------------------------------------</p>'
        for banki in lll:
            txt_f = open('new_file/{}.txt'.format(banki),'r',encoding='UTF-8')
            txt_line = txt_f.readlines()
            # print(txt_line)
            #print(len(txt_line)) 5  or 0
            if len(txt_line)>2:
                title0 = txt_line[2].replace('again1','').replace('\\n','').replace(' ','')
                txt_link = txt_line[3].replace('https://mp.weixin.qq.comagain1\\n','')
                if ii in str(title0):
                    count_n = title0.count(ii)
                    begin_n = begin_n + count_n
                    las_tit = title0
                    all_tt = all_tt +  '<p>({})'.format(banki) + '{}'.format(las_tit) + '</p>' #lianjie + '</p>'
        all_tt = all_tt + '<p>a{}({})</p>'.format(ii,str(begin_n))
    las_tt =  las_tt + all_tt
    return las_tt+'</html>'

@app.route('/keyimg', methods=['GET'])
def get_wdcloud():
    # 读取文本
    pythonInfo = open('all_yes_title.txt', 'r',  errors='ignore').read().replace('again1','').replace('农商','').replace('银行','')#encoding='utf-8',
    if len(pythonInfo)<100:
        pythonInfo = (pythonInfo+pythonInfo+pythonInfo).replace('   ','')
    print(pythonInfo)
    # 切割
    pythonCut = jieba.cut(pythonInfo, cut_all=True)
    pythonInfoList = ' '.join(pythonCut)  # 返回一个生成器对象
    try:
        backgroud = np.array(Image.open('500.png'))  # 将图片格式化成RBG数组
        myCloudword = wordcloud.WordCloud(font_path='simkai.ttf',  # 字体路径
                                          width=800, height=450,
                                          mask=backgroud,  # 字体颜色
                                          scale=1,  # 比例
                                          max_words=200,  # 最大字数
                                          min_font_size=4,  # 最小字体
                                          stopwords=STOPWORDS,  # 默认停止词
                                          random_state=50,  # 随机角度
                                          background_color='white',  # 背景颜色black
                                          max_font_size=100  # 最大字体
                                          ).generate(pythonInfoList)
        plt.imshow(myCloudword)
        # plt.show() #图片展示
        # print(myCloudword)
        # plt.figimage(myCloudword)   #绘制图片
        a_key=jieba.analyse.extract_tags(pythonInfo, topK = 100, withWeight = True,allowPOS = ())
        plt.imsave('python.png',myCloudword)  #保存图片
        with open('python.png', 'rb') as f:  # 以二进制读取图片
            data = f.read()
            encodestr = base64.b64encode(data)
            imgcd = str(encodestr,'utf-8')
            rss = str('<p>关键词参考：{}</p><br>'.format(str(a_key))+'<img src="data:image/png;base64,{}">'.format(imgcd))
        return rss
    except ValueError as e:
        return '关键词太少'
    finally:
        pass
# print(get_wdcloud())
@app.route('/yuxie', methods=['GET'])
def get_yuxie():
    return redirect('https://www.wenjuan.com/s/6bQ3If')






if __name__ == '__main__':
    app.run(port=100,debug=True)

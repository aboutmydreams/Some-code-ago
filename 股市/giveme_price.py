import requests,time,smtplib,os,json,re,random
from email.mime.text import MIMEText
from email.header import Header
from flask_mail import Mail, Message



'''

# 发送email
app = Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'a2491189079@qq.com',
    MAIL_PASSWORD = 'hsokuuoiiacjeccj',
    MAIL_DEBUG = True
)

mail = Mail(app)
#发邮件
def send_mail(QQ_num,data):
    name = str(data[0])
    price = str(data[1])
    change = str(data[2])
    change1 = str(data[3])
# sender 发送方哈，recipients 邮件接收方列表
    msg = Message("【{}】{}".format(name,price),sender='a2491189079@qq.com', recipients=[QQ_num])
# msg.body 邮件正文
    msg.body = "【{}】 现在的价格: {}，当前{}，已经靠近你的预期".format(name,price,change1)
    msg.html = "<p><strong>【{}】</strong> 现在的价格是 : <h2><strong>{}</strong></h2></p>".format(name,price)
# msg.attach 邮件附件添加
# msg.attach("文件名", "类型", 读取文件）
#     with app.open_resource("C:\\Users\\T-bao\\Desktop\\软件代码\\1.gif") as fp:
#         msg.attach("image.jpg", "image/jpg", fp.read())
    mail.send(msg)
    # print("Mail sent")

'''
#获取现在的时间，返回元组[星期，月，日，时，分，秒，年]如['Mon', 'May', '14', '13', '29', '05', '2018']
def get_time():
    now_time0 = '[\''+time.ctime().replace(':','\',\'').replace(' ','\',\'')+'\']'
    return eval(now_time0)

#发邮件
def email(QQ_num,data):
# 第三方 SMTP 服务
    name = str(data[0])
    price = str(data[1])
    change = str(data[2])
    change1 = str(data[3])
    print(change1)
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="2491189079@qq.com"    #用户名
    mail_pass="hsokuuoiiacjeccj"   #口令

    sender = '2491189079@qq.com'
    receivers = ['1097977702@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(f'<h2>【{name}】<h2> 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("mydreams", 'utf-8')#发件人
    message['To'] =  Header("测试", 'utf-8')

    subject = f'价格：{price},当前{change}，涨幅为{change1}'
    message['Subject'] = Header(subject, 'utf-8')



    server = smtplib.SMTP_SSL(mail_host,465) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()
    print ("邮件发送成功",data)


#查询 返回股票名，价格，波动，波动百分比
def get_price(gu_num=None):
    if not gu_num:
        return
    if gu_num[0] is '0' or gu_num[0] is '3':
        gu_num = f'{gu_num}2'
            #print(gu_num+'ooooo')
        fdurl = f'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd={gu_num}&sty=FDFGBTB&st=z&sr=&p=&ps=&lvl=&cb=jQuery18301703092172186509_1525869600183&js=&token=5c46f660fab8722944521b8807de07c0&_=1525869602727'

        bd_session = requests.Session()
        #res = bd_session.get(url)
        # Soup = BeautifulSoup(res.text,'lxml')
        # tittles = Soup.select('#stockname > a')
        rice = bd_session.get(fdurl)
    else:
        gu_num = f'{gu_num}1'
            #print(gu_num)
        rice = requests.get(
            f'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd={gu_num}&sty=FDFGBTB&st=z&sr=&p=&ps=&lvl=&cb=jQuery18309719162861492383_1525917294253&js=&token=5c46f660fab8722944521b8807de07c0&_=1525917296337'
        )


    #print(tittles[0].get('href'))
    #print(tittles[0].get_text()[0:-1])
    #print(rice.text)
    data = eval(rice.text[40:])
    data0 = '[\''+data[0]+'\']'
    data1 = data0.replace(',','\',\'')
    #print(data1)
    data2 = eval(data1)
    gu_name = data2[3]
    now_price = data2[4]
    change1 = data2[5]
    change2 = data2[6]
    return gu_name,now_price,change1,change2
        #JS.aspx?type=CT&cmd
# get_price('002557')
# get_price('002600')
# get_price('600549')
# get_price('603328')

#监测并发送,输入股票代号，预计价格，预计提醒价格，(加一个预计价格是为了记住当年的逻辑)
#当价格接近时，监控频率增加，一条股票一天最多连续三条邮件
def Monitor(gu_num,QQ_num,expect_price,remind_price=None):
    now_time = get_time()
    now_hour = int(now_time[3])*100
    now_min = int(now_time[4])
    now = now_hour+now_min
    if 925<now<1130 or 1255<now<1500:
        n = 0
        if not remind_price:
            remind_price = expect_price
        while n<3:
            the_info = get_price(gu_num)
            re_price = float(the_info[1])
            now_time = get_time()
            now_hour = int(now_time[3])*100
            now_min = int(now_time[4])
            now = now_hour+now_min
            print(the_info)
            if re_price >= remind_price:
                n+=1
                print(n)
                email(QQ_num,the_info)
                print(the_info,type(the_info))
                time.sleep(35)
                #return 'ok'
            else:
                #这里加 如果相差太大了 睡久一点
                time.sleep(101)
            if 1130<now<1259:
                time.sleep((12-now_hour)*3600+(59-now_min)*60)
            if now>1500:
                break
    else:
        print('500')


#@app.route('/', methods=['GET'])
def re_moni(gu_num,QQ_num,expect_price,remind_price=None):
    now_time = get_time()
    now_hour = int(now_time[3])*100
    now_min = int(now_time[4])
    now = now_hour+now_min
    if 929<=now<=1130 or 1259<=now<=1500:
        print('?')
        Monitor(gu_num,QQ_num,expect_price,remind_price)
    elif now<929 and now_min<=29:
        print('??')
        time.sleep((9-now_hour)*3600+(29-now_min)*60)
        Monitor(gu_num,QQ_num,expect_price,remind_price)
    elif now < 929:
        print('???')
        time.sleep((8-now_hour)*3600+(89-now_min)*60)
        Monitor(gu_num,QQ_num,expect_price,remind_price)
    elif 1130<now<1259:
        time.sleep((13-now_hour)*3600+(59-now_min)*60)
        Monitor(gu_num,QQ_num,expect_price,remind_price)
    else:
        print('今日已经完成！！！祝好运')


re_moni('600549','1097977702@qq.com',23.55)
#re_moni('603328','1097977702@qq.com',11.55)
#要开始学多线程了


'''
url9 = 'http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id=0025572&TYPE=r&rtntype=5&isCR=false&token=4d2cd9e55b669a2b3dec49542914281d&js=cb_1525878402738_52724054((x))&cb_1525878402738_52724054=cb_1525878402738_52724054'
bd_session = requests.Session()
dife = bd_session.get(url9)
print(eval(dife.text[25:])['info'])#时刻的数据

if __name__ == "__main__":
    app.run()
'''
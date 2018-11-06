import requests,time,smtplib
from email.mime.text import MIMEText
from email.header import Header
from flask_mail import Mail, Message

def iemail(QQ_num,data,em_name):
    # 第三方 SMTP 服务
    # name = str(data[0])
    # price = str(data[1])
    # change = str(data[2])
    # change1 = str(data[3])
    # print(change1)
    mail_host="smtp.qq.com"  #设置服务器
    

    # mail_user="2491189079@qq.com"    #用户名
    # mail_pass="hsokuuoiiacjeccj"   #口令
    # sender = '2491189079@qq.com'


    mail_user="1097977702@qq.com"   
    mail_pass="kzipicthecqhicea" 
    sender="1097977702@qq.com" 

    receivers = ['{}@qq.com'.format(QQ_num)]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('''<div style="position:absolute; width:100%; height:100%; z-index:-1; left:0; top:0;"> <img src="http://tupian.qqjay.com/u/2012/0831/4_155314_2.jpg" height="100%" width="100%" style="left:0; top:0;">      
</div> <h1>{}</h1> 邮件发送测试...<br>happy<br><br><h5>Do I send you a happy surprise today? wish you a good time in university！v^ヽ(○^㉨^)ﾉ♪</h5>'''.format(data), 'html', 'utf-8')#正文
    message['From'] = Header("1097977702@qq.com", 'utf-8')#发件人名字
    message['To'] =  Header("测试", 'utf-8')

    subject = '{}'.format(em_name)#邮件名字
    message['Subject'] = Header(subject, 'utf-8')



    server = smtplib.SMTP_SSL(mail_host,465) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()
    print ("邮件发送成功",data)
    

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

    receivers = [f'{QQ_num}@qq.com']

    message = MIMEText('''<!DOCTYPE html>
<html>
<head>
	<title>hhh</title>
	<style type="text/css">
		*{
			margin: 0;
			padding: 0;
			width: 100%;
			height: 100%;
		}
		body{
			width: 100%;
			height: 100%;
		}
		p,h1,h5{
			color: blue;
		}
		.da{
			position: fixed;width: 80%; height:30%;bottom:15%;background-color: transparent;
		}
	</style>
</head>
<body>

	<div style="da">
		<img src="https://img.zcool.cn/community/0178fc57a199730000012e7e0b9559.jpg@1280w_1l_2o_100sh.webp" height="100%" width="100%" style="left:0; top:0;">
	</div>
	<h5>happy!<br>Did I send you a happy surprise today? Wish you a good time in university！v^ヽ(○^㉨^)ﾉ♪</h5>

</body>
</html>''', 'html', 'utf-8')#正文
    message['From'] = Header("1097977702@qq.com", 'utf-8')#发件人名字
    message['To'] =  Header("测试", 'utf-8')

    subject = f'{em_name}'
    message['Subject'] = Header(subject, 'utf-8')



    server = smtplib.SMTP_SSL(mail_host,465) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()
    print ("邮件发送成功",QQ_num,data)
    
iemail()
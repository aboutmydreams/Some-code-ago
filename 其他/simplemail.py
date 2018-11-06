#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="2491189079@qq.com"    #用户名
mail_pass="hsokuuoiiacjeccj"   #口令 
 
 
sender = '2491189079@qq.com'
receivers = ['1097977702@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 

server = smtplib.SMTP_SSL(mail_host,465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(mail_user, mail_pass)
server.sendmail(sender, receivers, message.as_string())
server.quit()

'''
smtpObj = smtplib.SMTP() 
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
'''
print ("邮件发送成功")

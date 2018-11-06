from flask import Flask,request,jsonify
import random,json,sys
from flask_mail import Mail, Message
import os
import write_txt


# 发送email
app = Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    
    MAIL_USERNAME = '1097977702@qq.com',
    MAIL_PASSWORD = 'kzipicthecqhicea',
    MAIL_DEBUG = True
)

mail = Mail(app)

def send_mail(QQ_num):
    nn = str(random.randint(2010,9919))
# sender 发送方哈，recipients 邮件接收方列表
    msg = Message("Hi!This is a test ",sender='dengwenhao003@qq.com', recipients=[QQ_num])
# msg.body 邮件正文
    msg.body = "【早e点】 I give you a num : {}".format(nn)
    msg.html = "<p><strong>【早e点】</strong> I give you a num : <h2><strong>{}</strong></h2></p>".format(nn)
# msg.attach 邮件附件添加
# msg.attach("文件名", "类型", 读取文件）
#     with app.open_resource("C:\\Users\\T-bao\\Desktop\\软件代码\\1.gif") as fp:
#         msg.attach("image.jpg", "image/jpg", fp.read())
    mail.send(msg)
    # print("Mail sent")
    return nn

def set_psd():
    if request.form['yan_zm'] is nn:
        return('yes')
    else:
        return('no')

def checkpsd():
    payload = {"number":request.json['username'],"passwd":request.json['password']}
    data = str(payload['number'])+':::::'+str(payload['passwd'])
    had = write_txt.save_data(data)
    print(data)
    if had is 'have':
        return jsonify({'how':'havehad the user'})
    else:
        return jsonify({'status':'success'})

def check_data():
    payload = {"number":request.json['username'],"passwd":request.json['password']}
    data = str(payload['number'])+':::::'+str(payload['passwd'])
    f0 =  open('test.txt','r')
    f00 = f0.read()
    if data in f00:
        return jsonify({'status':'success'})
    else:
        return jsonify({'status':'error'})
    f0.close()

'''
ff = open('test\\data\\test.txt','r')
all_data = ff.read()
if data in all_data:
    return jsonify({'status':'success'})
else:
    return jsonify({'status':'error'})
'''
if __name__ == "__main__":
    app.run()

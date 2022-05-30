from flask import Flask
from flask_mail import Mail, Message
import os

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

@app.route('/')
def index():
    nn = 1000
# sender 发送方哈，recipients 邮件接收方列表
    msg = Message("Hi!This is a test ",sender='dengwenhao003@qq.com', recipients=['a2491189079@qq.com','1424027815@qq.com','406313627@qq.com','1479898303@qq.com'])
# msg.body 邮件正文
    msg.body = f"【早e点】 I give you a num : {nn}."
# msg.attach 邮件附件添加
# msg.attach("文件名", "类型", 读取文件）
#     with app.open_resource("C:\\Users\\T-bao\\Desktop\\软件代码\\1.gif") as fp:
#         msg.attach("image.jpg", "image/jpg", fp.read())
    nn+=1
    if nn is 9999:
        nn = 1000
    mail.send(msg)
    print("Mail sent")
    return("<h1>Sent successfully</h1>")

if __name__ == "__main__":
    app.run()
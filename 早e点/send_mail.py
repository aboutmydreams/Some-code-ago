from flask import Flask,request
import json
from flask_mail import Mail
from flask import render_template
import edian_def_all
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

@app.route('/', methods=['GET'])
def loginpage():
    return render_template("loginpage.html")

@app.route('/1', methods=['POST'])
def login():
    return edian_def_all.check_data()


@app.route('/mail', methods=['GET'])
def register():
    return '''<form action="/mail" method="post">
              <p><input name="username">QQ</p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/mail',methods=['POST'])
def send_qq():
    QQ_num = request.form['username']
    n = edian_def_all.send_mail(QQ_num)
    return json.dumps(n)

def sure_yzm():
    return render_template("验证码.html")
'''<form action="/setmima" method="post">
              <p><input name="yanzm">验证码</p>              
              <p><button type="submit">确认</button></p>
              </form>'''



if __name__ == "__main__":
    app.run(host='172.16.0.13')
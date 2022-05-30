from flask import Flask
from flask import request
from flask import render_template
import easy_mail
import write_QQ
app = Flask(__name__)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

@app.route('/66_DWH______NCU_Ican', methods=['GET'])
def reach_QQ():
    return render_template('iq.html')

@app.route('/icall', methods=['POST'])
def signin_form():
    QQ_num = request.form['QQ_num']
    print(f'{QQ_num}---------------------')
    write_QQ.write_qq(QQ_num)
    if is_number(QQ_num) is True:
        easy_mail.iemail(QQ_num,'happy!','邓文浩')
    if QQ_num != 'dwh':
        return render_template('icall.html')
    f2=open('data/qq.txt','r')
    f3=str(f2.read())
    return f3+str(f3.count('-'))

@app.route('/NCU_Ibaidu', methods=['GET'])
def sure_yzm():
    return render_template("baidu.html")





if __name__ == '__main__':
    app.run(debug=True)
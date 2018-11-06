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
	pass
	return render_template('iq.html')

@app.route('/icall', methods=['POST'])
def signin_form():
    QQ_num = request.form['QQ_num']
    print(QQ_num+'---------------------')
    write_QQ.write_qq(QQ_num)
    if is_number(QQ_num) is True:
        easy_mail.iemail(QQ_num,'happy!','邓文浩')
    if QQ_num=='dwh':
        f2=open('data/qq.txt','r')
        f3=str(f2.read())
        f4=f3+str(f3.count('-'))
        return(f4)
        f2.close()
    else:
        return render_template('icall.html')

@app.route('/NCU_Ibaidu', methods=['GET'])
def sure_yzm():
    pass
    return render_template("baidu.html")





if __name__ == '__main__':
    app.run(debug=True)
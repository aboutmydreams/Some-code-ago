#-*- coding: UTF-8 -*-
import os,time,datetime,json,requests,write_data
from flask import Flask,redirect,url_for,render_template,request,send_file,send_from_directory
import base64

app = Flask(__name__)
@app.route('/acset', methods=['GET'])
def loginpage():
    return render_template("loginpage.html")

@app.route('/acset', methods=['POST'])
def login():
    p1 = request.form['username']
    p2 = request.form['password']
    if p1=='123' and p2=='123':
        return render_template("houtai.html")
    #print(request.form['username'])#这是一个重要的flask用发
    if write_data.get_qian1()[0]==0:
        return redirect('/acset')
    elif write_data.get_qian1()[0]==1:
        write_data.baoming(p1,p2)
        return redirect('/acset')

@app.route('/act-time',methods=['GET'])
def get_time():
    return str(write_data.get_qian1())

@app.route('/set', methods=['POST'])
def set_it():
    ti1 = request.form['begintime']
    ti2 = request.form['lasttime']
    time1 = ti1[-4:] + ti1[:2] + ti1[3:5]
    time2 = ti2[-4:] + ti2[:2] + ti2[3:5]
    active_name = request.form['active-name']
    active_people = request.form['active-people']
    write_data.write_set(time1,time2,active_name,active_people)
    return render_template("houtai.html")

@app.route('/see', methods=['GET'])
def get_data():
    return str(write_data.get_qinkuang())


@app.route('/see', methods=['POST'])
def get_datas():
    mi = request.form['mi']
    return str(write_data.get_qinkaung()) if mi=='5201314' else '我看破，我不说'

@app.route("/data/<filename>", methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = os.getcwd()  # 假设在当前目录
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=99,debug=True)
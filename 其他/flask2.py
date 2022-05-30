from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<hi>hey</h1>'

@app.route('/1',methods=['GET'])
def getjiaohu():
  user = { 'nickname': 'Miguel' } # fake user
  posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
  return render_template("交互.html",
        title = 'Homehhh',
        user = user,
        posts = posts)

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    print(request.form['username'])#这是一个重要的flask用发
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run(debug=True)
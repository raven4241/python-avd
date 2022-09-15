from flask import Flask, request, session, redirect, url_for, render_template
 
app = Flask(__name__)
  
@app.route('/', methods=['GET', 'POST'])
def login():
  return render_template('login.html', info = 'Please Login')
  if request.method=='POST':
    usr = request.form["username"]
    pwd = request.form["password"]
    users = {"admin:password", "user:user1"}
    if usr not in users and pwd not in users:
      return render_template('login.html', info = 'Bad Credentials')
      
    else:
      return render_template('index.html')

if __name__ == '__main__':
    app.run()
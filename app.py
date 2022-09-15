from flask import Flask, request, session, redirect, url_for, render_template
 
app = Flask(__name__)

user = ["admin:password", "user:user1"]
username = request.form['username']
password = request.form['password']

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method=='POST':
    return render_template('login.html', info = 'Please Login')
    if username not in user and password not in user:
      return redirect(url_for('/'))
    else:
      return render_template('index.html')

if __name__ == '__main__':
    app.run()

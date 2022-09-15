from flask import Flask, request, session, redirect, url_for, render_template
 
app = Flask(__name__)
  
@app.route('/', methods=['GET', 'POST'])
def login():
  return render_template('login.html', info = 'Please Login')
  if request.method=='POST':
    usr = request.form["username"]
    pwd = request.form["password"]
    user = {"admin:password", "user:user1"}
    if usr not in user and pwd not in user:
      return redirect(url_for('/'), info = 'Wromg Credentials')
      
    else:
      return render_template('index.html')

if __name__ == '__main__':
    app.run()
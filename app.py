from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
    
database={'atharva','aryan', 'vijay', 'smita'}
psd={'avd@2004','aryan@2008', 'vijay@1973', 'smita@1980'}

@app.route('/login',methods=['POST','GET'])
def login():
    user=request.form['username']
    pwd=request.form['password']
    if user not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if pwd not in psd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('index.html')

if __name__ == '__main__':
    app.run()
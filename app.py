from flask import *
from werkzeug.utils import secure_filename
import os
 
app = Flask(__name__)

user = {"admin"}
password = {"avd@2004"}
  
@app.route('/')
def home():
  return render_template('login.html', info = 'Please Login')
  
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method=='POST':
    usr = request.form["username"]
    pwd = request.form["password"]
    if usr not in user or pwd not in password:
      return render_template('login.html', info = "Bad Credentials")
    else:
      return render_template('index.html', wlcm = "Welcome Admin")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
  if request.method=='POST':
    return render_template('login.html', info = 'Logged Out')

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exists_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(uploads_dir, secure_filename(file.filename)))

        for file in request.files.getlist('charts'):
            file.save(os.path.join(uploads_dir, secure_filename(file.name)))

        return redirect(url_for('upload'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
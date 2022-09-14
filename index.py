from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
  return render_template('login.html')
  if request.method=="POST":
    if request.form['username']!=user1 and request.form['password']!=pass1:
      return render_template('login.html', info="Bad Credentials!")
    else:
      return render_template('index.html')

if __name__ == '__main__':
    app.run()
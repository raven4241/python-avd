from flask import Flask, request, session, redirect, url_for, render_template
 
app = Flask(__name__)

user = ["admin:password", "user:user1"]

@app.route('/')
def login():
  return 

if __name__ == '__main__':
    app.run()

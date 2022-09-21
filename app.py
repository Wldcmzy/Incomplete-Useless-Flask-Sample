import os
from flask import Flask, request, session, redirect
from flask_cors import CORS
import modules.master
import modules.caricature
import modules.SDW

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(modules.master.blue)
app.register_blueprint(modules.caricature.blue)
app.register_blueprint(modules.SDW.blue)
CORS(app, supports_credentials=True)

def judge_url_pass(url : str) -> bool:
    pass_url: list[str] = ['/login', '/regist']
    pass_prefix: list[str] = ['/static/nologin']
    if url in pass_url: return True
    for each in pass_prefix: 
        if url.startswith(each): return True 
    return False

@app.before_request
def before():
    url = request.path
    if judge_url_pass(url):
        pass
    else:
        username = session.get('username', None)
        cookie = session.get('cookie', None)
        if not cookie or not modules.master.check_cookie(username, cookie):
            return redirect('login')
        else:
            pass


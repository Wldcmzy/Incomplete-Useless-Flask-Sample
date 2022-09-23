from flask import(
    render_template, 
    Blueprint, 
    request, 
    session, 
    redirect, 
    send_from_directory,
)
from .identifier import *
from .config import *

blue = Blueprint('master', __name__)

@blue.route('/')
def home():
    return render_template('home.html')

@blue.route('/favicon.ico')
def ikun():
    return send_from_directory('static', 'favicon.ico')

@blue.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        if check_login_datas(username, password):
            cookie = Cookie()
            cookie_dict[username] = cookie
            session['username'] = username
            session['cookie'] = cookie.value
            return redirect('/')
        else:
            return redirect('/login')
    else:
        return render_template("login.html")

@blue.route('/regist', methods = ['POST', 'GET'])
def regist():
    pass
from flask import(
    render_template, 
    Blueprint, 
    request, 
    session, 
    redirect, 
    send_from_directory,
)

blue = Blueprint(
    'SDW', 
    __name__, 
    url_prefix = '/SDW',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = '/SDWsource',
)

@blue.route('/', methods = ['GET'])
def root():
    return render_template('index山东天气图.html')

@blue.route('/temperature', methods = ['GET'])
def temperature():
    return render_template('山东温度图.html')

@blue.route('/humidity', methods = ['GET'])
def humidity():
    return render_template('山东湿度图.html')

@blue.route('/pressure', methods = ['GET'])
def pressure():
    return render_template('山东气压图.html')

@blue.route('/precipitation', methods = ['GET'])
def precipitation():
    return render_template('山东降水图.html')
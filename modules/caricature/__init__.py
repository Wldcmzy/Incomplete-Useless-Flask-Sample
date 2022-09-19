from flask import render_template, Blueprint
from .utils.Affix import Affix_OnlyZeroExample
__affixer = Affix_OnlyZeroExample()

blue = Blueprint(
    'caricature', 
    __name__, 
    url_prefix = '/caricature',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = '/caricaturesource',
)

@blue.route('/', methods = ['GET'])
def root():
    return render_template('caricatures_index.html')

@blue.route('/drstone<string:page>', methods = ['GET'])
def DrStone(page: str):
    try:
        if page == 'idx':
            res = render_template(f'Dr.STONE/index.html')
        elif page[ : 6] == 'Reboot':
            res = render_template(f'Dr.STONE/Dr.STONEhtmls/Dr.STONE石纪元外传-Reboot百夜 第 {page[6 : ]} 话.html')
        else:
            res = render_template(f'Dr.STONE/Dr.STONEhtmls/Dr.STONE石纪元 第 {__affixer.add_prefix(page, 3)} 话.html')
        return res
    except Exception as e:
        return f'错误, 可能没有此页面 {type(e)}'

@blue.route('/OPM<string:uuid>')
def OPM(uuid: str):
    try:
        if uuid == 'idx':
            res = render_template(f'OPM/index.html')
        else:
            res = render_template(f'OPM/一拳超人ONE原作版HTMLS/一拳超人ONE[ {uuid} ].html')
        return res
    except Exception as e:
        return f'错误, 可能没有此页面 {type(e)}'
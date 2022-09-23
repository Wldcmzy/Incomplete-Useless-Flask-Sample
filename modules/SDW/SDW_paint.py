import random
from pyecharts import options as opts
from pyecharts.charts import Map
from pathlib import Path

class ColorMaker:
    ColorMap = { 
         'Gray'        : 'Gray'
        ,'Red'         : 'Red'
        ,'Redpurple'   : 'RedPurple'
        ,'Purplered'   : 'RedPurple'
        ,'Purple'      : 'Purple'
        ,'Purpleblue'  : 'PurpleBlue'
        ,'Bluepurple'  : 'PurpleBlue'
        ,'Blue'        : 'Blue'
        ,'Bluecyan'    : 'BlueCyan'
        ,'Cyanblue'    : 'BlueCyan'
        ,'Cyan'        : 'Cyan'
        ,'Cyangreen'   : 'CyanGreen'
        ,'Greencyan'   : 'CyanGreen'
        ,'Green'       : 'Green'
        ,'Greenyellow' : 'GreenYellow'
        ,'Yellowgreen' : 'GreenYellow'
        ,'Yellow'      : 'Yellow'
        ,'Yelloworange': 'YellowOrange'
        ,'Orangeyellow': 'YellowOrange'
        ,'Orange'      : 'Orange'
        ,'Orangered'   : 'OrangeRed'
        ,'Redorange'   : 'OrangeRed'
        #,'Dullred'     : 'DullRed'
        #,'Dullyellow'  : 'DullYellow'
        #,'Dullcyan'    : 'DullCyan'
        #,'Dullblue'    : 'DullBlue'
        #,'Dullpurple'  : 'DullPurple'
    }
    BaseColorOrder = { 
         'Gray'        :   ['#ffffff','#272727','#3C3C3C','#4F4F4F','#5B5B5B','#6C6C6C','#7B7B7B','#8E8E8E','#9D9D9D','#ADADAD','#BEBEBE','#d0d0d0','#E0E0E0','#F0F0F0','#FCFCFC','#FFFFFF']
        ,'Red'         :   ['#2F0000','#4D0000','#600000','#750000','#930000','#AE0000','#CE0000','#EA0000','#FF0000','#FF2D2D','#FF5151','#ff7575','#FF9797','#FFB5B5','#FFD2D2','#FFECEC']
        ,'RedPurple'   :   ['#600030','#820041','#9F0050','#BF0060','#D9006C','#F00078','#FF0080','#FF359A','#FF60AF','#FF79BC','#FF95CA','#ffaad5','#FFC1E0','#FFD9EC','#FFECF5','#FFF7FB']
        ,'Purple'      :   ['#460046','#5E005E','#750075','#930093','#AE00AE','#D200D2','#E800E8','#FF00FF','#FF44FF','#FF77FF','#FF8EFF','#ffa6ff','#FFBFFF','#FFD0FF','#FFE6FF','#FFF7FF']
        ,'PurpleBlue'  :   ['#28004D','#3A006F','#4B0091','#5B00AE','#6F00D2','#8600FF','#921AFF','#9F35FF','#B15BFF','#BE77FF','#CA8EFF','#d3a4ff','#DCB5FF','#E6CAFF','#F1E1FF','#FAF4FF']
        ,'Blue'        :   ['#000079','#000093','#0000C6','#0000C6','#0000E3','#2828FF','#4A4AFF','#6A6AFF','#7D7DFF','#9393FF','#AAAAFF','#B9B9FF','#CECEFF','#DDDDFF','#ECECFF','#FBFBFF']
        ,'BlueCyan'    :   ['#000079','#003D79','#004B97','#005AB5','#0066CC','#0072E3','#0080FF','#2894FF','#46A3FF','#66B3FF','#84C1FF','#97CBFF','#ACD6FF','#C4E1FF','#D2E9FF','#ECF5FF']
        ,'Cyan'        :   ['#003E3E','#005757','#007979','#009393','#00AEAE','#00CACA','#00E3E3','#00FFFF','#4DFFFF','#80FFFF','#A6FFFF','#BBFFFF','#CAFFFF','#D9FFFF','#ECFFFF','#FDFFFF']
        ,'CyanGreen'   :   ['#006030','#01814A','#019858','#01B468','#02C874','#02DF82','#02F78E','#1AFD9C','#4EFEB3','#7AFEC6','#96FED1','#ADFEDC','#C1FFE4','#D7FFEE','#E8FFF5','#FBFFFD']
        ,'Green'       :   ['#006000','#007500','#009100','#00A600','#00BB00','#00DB00','#00EC00','#28FF28','#53FF53','#79FF79','#93FF93','#A6FFA6','#BBFFBB','#CEFFCE','#DFFFDF','#F0FFF0']
        ,'GreenYellow' :   ['#467500','#548C00','#64A600','#73BF00','#82D900','#8CEA00','#9AFF02','#A8FF24','#B7FF4A','#C2FF68','#CCFF80','#D3FF93','#DEFFAC','#E8FFC4','#EFFFD7','#F5FFE8']
        ,'Yellow'      :   ['#424200','#5B5B00','#737300','#8C8C00','#A6A600','#C4C400','#E1E100','#F9F900','#FFFF37','#FFFF6F','#FFFF93','#FFFFAA','#FFFFB9','#FFFFCE','#FFFFDF','#FFFFF4']
        ,'YellowOrange':   ['#5B4B00','#796400','#977C00','#AE8F00','#C6A300','#D9B300','#EAC100','#FFD306','#FFDC35','#FFE153','#FFE66F','#FFED97','#FFF0AC','#FFF4C1','#FFF8D7','#FFFCEC']
        ,'Orange'      :   ['#844200','#9F5000','#BB5E00','#D26900','#EA7500','#FF8000','#FF9224','#FFA042','#FFAF60','#FFBB77','#FFC78E','#FFD1A4','#FFDCB9','#FFE4CA','#FFEEDD','#FFFAF4']
        ,'OrangeRed'   :   ['#642100','#842B00','#A23400','#BB3D00','#D94600','#F75000','#FF5809','#FF8040','#FF8F59','#FF9D6F','#FFAD86','#FFBD9D','#FFCBB3','#FFDAC8','#FFE6D9','#FFF3EE']
        #,'DullRed'     :   ['#613030','#743A3A','#804040','#984B4B','#AD5A5A','#B87070','#C48888','#CF9E9E','#D9B3B3','#E1C4C4','#EBD6D6','#F2E6E6']
        #,'DullYellow'  :   ['#616130','#707038','#808040','#949449','#A5A552','#AFAF61','#B9B973','#C2C287','#CDCD9A','#D6D6AD','#DEDEBE','#E8E8D0']
        #,'DullCyan'    :   ['#336666','#3D7878','#408080','#4F9D9D','#5CADAD','#6FB7B7','#81C0C0','#95CACA','#A3D1D1','#B3D9D9','#C4E1E1','#D1E9E9']
        #,'DullBlue'    :   ['#484891','#5151A2','#5A5AAD','#7373B9','#8080C0','#9999CC','#A6A6D2','#B8B8DC','#C7C7E2','#D8D8EB','#E6E6F2','#F3F3FA']
        #,'DullPurple'  :   ['#6C3365','#7E3D76','#8F4586','#9F4D95','#AE57A4','#B766AD','#C07AB8','#CA8EC2','#D2A2CC','#DAB1D5','#E2C2DE','#EBD3E8']
      }

    @classmethod
    def generate(cls, colorname: str = None, length: int = None,  startpos: int = None, reverse: bool = False):
        if not colorname:
            colorname = random.choice(list(ColorMaker.BaseColorOrder.keys()))
        else:
            colorname = ColorMaker.ColorMap[colorname.capitalize()]
        if not length or length > len(ColorMaker.BaseColorOrder[colorname]):
            length = len(ColorMaker.BaseColorOrder[colorname])
        if not startpos:
            startpos = random.randint(0, len(ColorMaker.BaseColorOrder[colorname]) - length)
        lst =  ColorMaker.BaseColorOrder[colorname][startpos : startpos + length]
        if reverse: lst = lst[ : : -1]
        return lst


def draw(name: str, datas: list[list], ranges: list, colors: list = None, measure = ''):
    PATH: Path = Path(__file__).parent / "templates"
    if not colors: colors = ColorMaker.generate(length = len(ranges))
    pieces = []
    for i in range(1, len(ranges)):
        pieces.append({
            "min": ranges[i - 1], 
            "max": ranges[i], 
            "label": f'{ranges[i - 1]}{measure} - {ranges[i]}{measure}', 
            "color": colors[i - 1]}
        )
    return (
        Map()
        .add(name, datas, "山东")
        .set_global_opts(
            title_opts = opts.TitleOpts(title = name), 
            visualmap_opts = opts.VisualMapOpts(
                is_piecewise = True,
                pieces = pieces
            ),
        )
        .render(PATH / f"{name}.html")
    )
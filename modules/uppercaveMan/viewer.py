'''
蓝图文件
'''

from re import template
from flask import Blueprint,render_template,url_for,request
import  uuid
from flask import  Flask,render_template,request

from .dataBase.dataHandle import *

#引入重定向的包（一个请求到另外一个请求）
from werkzeug.utils import  redirect
#蓝图变量
blue = Blueprint(
    'uppercaveMan',
    __name__,
    url_prefix = '/uppercaveMan',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path='')

@blue.route( "/")
def hello_index():
    return render_template(("index.html"))

@blue.route("/tag_list")
def tag_list():
    taglist_data = getTag_list()
    # 将数据分析前10 的标签占比饼图渲染到网页上
    return render_template("tag_list.html",taglist_data = taglist_data)

@blue.route("/play_collection_relation")
def play_collection_relation():
    play_coll_data = getPlay_Coll()
    return render_template("play_collection_relation.html",play_coll_data = play_coll_data)

@blue.route("/user_list")
def user_list():
    userlist_data = getUser_list()
    return render_template("user_list.html",userlist_data = userlist_data)

@blue.route("/play_user")
def play_user():
    playuser_data = getPlay_list()
    return render_template("play_user.html",playuser_data = playuser_data)

@blue.route("/singersun")
def share_rev():
    return render_template("singersun.html")

@blue.route("/map_singer")
def map_singer():
    mapsinger_data = getMap_siger()
    print(mapsinger_data)
    return render_template("map_singer.html",mapsinger_data = mapsinger_data)

# 播放前十的歌单名称
@blue.route("/max_play_title")
def max_play_title():
    max_play_title_data = get_max_play_title_data()
    # 将数据渲染到网页上
    return render_template("max_play_title.html",max_play_title_data=max_play_title_data)

# 歌单播放前十的用户
@blue.route("/max_play_user")
def max_play_user():
    max_play_user_data = get_max_play_user_data()
    # 将数据渲染到网页上
    return render_template("max_play_user.html",max_play_user_data=max_play_user_data)

# 发布歌单最多的用户
@blue.route("/max_title_user")
def max_title_user():
    max_title_user_data = get_max_title_user_data()
    # 将数据渲染到网页上
    return render_template("max_title_user.html",max_title_user_data=max_title_user_data)

# 播放次数区间歌单的数量
@blue.route("/title_in_play")
def title_in_play():
    title_in_play_data = get_title_in_play_data()
    # 将数据渲染到网页上
    return render_template("title_in_play.html",title_in_play_data=title_in_play_data)

# 40万播放量下，不同标签收藏数和播放量的关系
@blue.route("/collection_play")
def collection_play():
    collection_play_data = get_collection_play_data()
    # 将数据渲染到网页上
    #print(collection_play_data)
    return render_template("collection_play.html",collection_play_data=collection_play_data)

# 标签评论和播放的关系
@blue.route("/stack")
def review_play():
    review_play_data = get_review_play_data()
    print(review_play_data)
    # 将数据渲染到网页上
    return render_template("stack.html")

@blue.route("/one")
def hello_pic1():
    bar_3d_data = bar_3d_play()
    hour = list(range(0,500))
    days = list(range(0,500))
    print(bar_3d_data)
    return render_template("picture1.html",bar_3d_data=bar_3d_data,hour=hour,days=days)

@blue.route("/two")
def hello_pic2():
    pie_time_name_data = pie_time_name()
    print(pie_time_name_data)
    return render_template("picture2.html",pie_time_name_data=pie_time_name_data)

@blue.route("/three")
def hello_pic3():
    scatter_collection_review_play_data = scatter_collection_review_play()
    print(scatter_collection_review_play_data)
    return render_template("picture3.html",scatter_collection_review_play_data=scatter_collection_review_play_data)

@blue.route("/four")
def hello_pic4():
    play_low_data,play_high_data = bar_scatter()
    print(play_low_data)
    print("--------------------")
    print(play_high_data)
    return render_template("picture4.html",play_low_data=play_low_data,play_high_data=play_high_data)

@blue.route("/five")
def hello_pic5():
    pie_time_player_data = pie_time_player()
    print(pie_time_player_data)
    return render_template("picture5.html",pie_time_player_data=pie_time_player_data)


@blue.route("/six")
def hello_pic6():
    return render_template("3d歌手地图.html")
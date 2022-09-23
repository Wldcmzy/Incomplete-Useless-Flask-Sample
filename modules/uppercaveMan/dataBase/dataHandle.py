from ast import main
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import  math
from flask import  Flask,render_template,request,jsonify
from .myDB import *
from pandas._libs import json
from typing import List, Any


def getPlayData():
    db = MyDB()
    fc = db.select_playlist()
    df = DataFrame(list(fc))
    return df

def getMessageData():
    db = MyDB()
    fc = db.select_music_message()
    df = DataFrame(list(fc))
    return df

def getAreaData():
    db = MyDB()
    fc = db.select_arealist()
    df = DataFrame(list(fc))
    return df

# 标签前十的百分比
def getTag_list():
    df = getMessageData()
    result = df['tag'].str.split(" ",expand=True).stack().reset_index(drop=True)
    result = result.value_counts(normalize=True).head(10)
    result = pd.DataFrame({'tag':result.index,'precent':result.values})
    taglist_data = [{
        "value": round(value['precent']*100),
        "name":value['tag']
    }for _,value in result.iterrows()]
    return taglist_data

# 播放量和收藏量的关系（散点图）
def getPlay_Coll():
    df = getMessageData()
    play = df['play']
    coll = df['collection']
    result = pd.DataFrame({"play":play,"coll":coll})
    play_coll_data = [[
        int(value['coll']),
        int(value['play'])/10000
    ]for _,value in result.iterrows()]
    json.dumps(play_coll_data)
    return play_coll_data

#贡献歌单数量用户榜（动态排序柱状图）
def getUser_list():
    df = getPlayData()
    df = df['user'].value_counts()[2:11]
    result = pd.DataFrame({"name":df.index,"value":df.values})
    userlist_data = [{
        'value':value['value'],
        'name':value['name']
    }for _,value in result.iterrows()]
    return userlist_data

def getPlay_list():
    df = getPlayData()
    df1 = df['play']
    result1 = []
    for item in df1:
        if "万" in item:
            item1 = item[:-1]+"0000"
            df1.replace(to_replace={item:item1},inplace = True)
        else :
            continue
    result2 = pd.DataFrame({"title":df['title'],"name":df['user'],"value":df1})
    result3 = result2[result2['name']=='云音乐官方歌单']
    playuser_data = {
        "title":result3['title'].to_list(),
        "value":result3['value'].to_list()
    }
    return playuser_data

def getShare_rev():
    df = getMessageData()
    #print(df)
    #df[df['tag']=='tag']['share'].values
    df = df.sort_values(by=['share','review'],ascending=[False,False])[1:21]
    sharerev_data = {
        'tag':df['tag'].to_list(),
        'share':df['share'].to_list(),
        'review':df['review'].to_list()
    }
    print(sharerev_data)
    return sharerev_data

def getMap_siger():
    df = getAreaData()
    df1 = df['area'].str.split(" - ",expand = True)
    df1 = df1[0].str.split(" ",expand = True)
    df2 = df['name']
    result = pd.DataFrame({'name':df2,'area':df1[0]})
    result.loc[result['area']=='北京'] = '北京市'
    result.loc[result['area'] == '上海'] = '上海市'
    result.loc[result['area'] == '浙江'] = '浙江省'
    result.loc[result['area'] == '重庆'] = '重庆市'
    result.loc[result['area'] == '新疆'] = '新疆维吾尔自治区'
    result.loc[result['area'] == '内蒙古'] = '内蒙古自治区'
    result.loc[result['area'] == '香港'] = '香港特别行政区'
    result = result['area'].value_counts()
    result2 = pd.DataFrame({'area': result.index, 'value': result.values})
    mapsinger_data = [{
        "name":value['area'],
        "value":value['value']
    }for _,value in result2.iterrows()]
    print(" ...................................................")
    print(mapsinger_data)
    return mapsinger_data

#lllllllllllllllllll

# 从数据库playlist 表中取数
def getPlayDataLlz():
    db = MyDB()
    fc = db.select_playlist()
    df = DataFrame(list(fc))
    # 只分析破放量上万的数据
    newdf = df[df['play'].str.contains(pat='万', regex=False)].reset_index(drop=True,level=-1)
    # 将播放量数据转为 int类型
    newdf["play"] = newdf["play"].map(lambda x:str(x)[:-1]).astype('int')
    return newdf

# 从数据库music_message 表中取数
def getMessageDataLlz():
    db = MyDB()
    fc = db.select_music_message()
    df = DataFrame(list(fc))

    df["play"] = df["play"].map(lambda x: str(x)[:-1]).astype('int')
    # newdf["review"] = newdf["review"].map(lambda x: str(x)[:-1]).astype('int')
    df["collection"] = df["collection"].map(lambda x: str(x)[:-1]).astype('int')
    # df["share"] = df["share"].map(lambda x: str(x)[:-1]).astype('int')
    return df

# 播放前十的歌单名称
def get_max_play_title_data():
    df = getPlayDataLlz()
    # 播放前十的歌单名称
    result = df[["title","play"]].sort_values(by="play")[::-1].reset_index(drop=True,level=-1)[:10]
    result = result[::-1]
    # print(result)
    # print(type(newdf["play"][1]))
    max_play_title_data = {
        "title":result.title.tolist(),
        "play":result.play.tolist()
    }
    print(max_play_title_data)
    return max_play_title_data

# 歌单播放前十的用户
def get_max_play_user_data():
    df = getPlayDataLlz()
    # 歌单播放前十的用户
    newdf = df.groupby(["user"])['play'].sum().reset_index()
    # print(newdf)
    result = newdf[["user","play"]].sort_values(by="play")[::-1].reset_index(drop=True,level=-1)[:10]
    result = result[::-1]
    # print(result)
    # print(type(newdf["play"][1]))
    max_play_user_data = {
        "user":result.user.tolist(),
        "play":result.play.tolist()
    }
    print(max_play_user_data)
    return max_play_user_data

# 发布歌单最多的用户
def get_max_title_user_data():
    df = getPlayDataLlz()
    newdf = df.groupby(["user"])['title'].count().reset_index()
    # print(newdf)
    result = newdf[["user","title"]].sort_values(by="title")[::-1].reset_index(drop=True,level=-1)[:10]
    result = result[::-1]
    # print(result)
    # print(type(newdf["play"][1]))
    max_title_user_data = {
        "user":result.user.tolist(),
        "title":result.title.tolist()
    }
    print(max_title_user_data)
    return max_title_user_data

# 播放次数区间歌单的数量
def get_title_in_play_data():
    df = getPlayDataLlz()
    # 设置切分区域
    listBins = [0, 100, 300, 700, 1500, 3000, 7000, 50000]
    # 设置切分后对应标签
    listLabels = ['0-100万播放量', '100-300万播放量', '300-700万播放量', '700-1500万播放量',
                  '1500-3000万播放量', '3000-7000万播放量', '7000万播放量以上']
    df['fenzu'] = pd.cut(df['play'], bins=listBins, labels=listLabels, include_lowest=True)
    # print(df)
    result = df.groupby(["fenzu"])['title'].count().reset_index()
    # print(newdf)
    # result = newdf[["user","title"]].sort_values(by="title")[::-1].reset_index(drop=True,level=-1)[:10]
    # result = result[::-1]
    # print(result)
    # print(type(newdf["play"][1]))
    title_in_play_data = [{
        "value": round(value['title']),
        "name": value['fenzu']
    }for _,value in result.iterrows()]
    print(title_in_play_data)
    return title_in_play_data

# 40万播放量下，不同标签收藏数和播放量的关系
def get_collection_play_data():
    df = getMessageDataLlz()
    # print(df["review"][1])
    # result = df[["collection","share","review","play"]]
    # 只统计400万播放量下的不同标签
    result = df.sort_values(by="play")[::-1].reset_index(drop=True,level=-1)[20:]
    # print(result)
    collection_play_data = [[
        value['collection'],
        value['play']
    ]for _,value in result.iterrows()]
    print(collection_play_data)
    return collection_play_data

# 标签评论数,收藏数和转发数的关系
def get_review_play_data():
    df = getMessageDataLlz()
    result = df[["review","play"]]
    review_play_data = [[
        value['review']+1,
        value['play']+1
    ]for _,value in result.iterrows()]
    print(review_play_data)
    return review_play_data

#if __name__ == '__main__':
    #cal_education_percent()
    #fc = getData()
    #get_industry_data()
    #print(fc)

#rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
#获得热歌榜的全部信息
def getHotsonglist():
    db = MyDB()
    fc = db.select_music_hotsonglist()
    df = DataFrame(list(fc))
    return df

#绘制（分享量，评论数，播放量）的三维柱状图
def bar_3d_play():
    df = getMessageData()
    newdf = df.groupby(['share','review']).play.mean().reset_index()
    newdf = newdf.loc[newdf['share']<500]
    newdf = newdf.loc[newdf['review'] < 500]
    print(newdf)
    arr = np.array(newdf)
    bar_3d_data = arr.tolist()
    print(bar_3d_data)
    return bar_3d_data

#绘制10首歌时长的饼图
def pie_time_name():
    df = getHotsonglist()
    newdf = df.iloc[:,0:2].copy()
    newdf = newdf.head(10)
    newdf['time']=newdf['time'].map(process_Data)
    #print(newdf)
    pie_time_name_data = [{
        "value":value['time'],
        "name":value['name']
    }for  _,value in newdf.iterrows()]
    print(pie_time_name_data)
    return pie_time_name_data

#处理时间的函数
def process_Data(x):
    if not isinstance(x,str):
        return x
    #得到分钟和秒
    m,s = x.split(":")
    second = float(s)/60
    return (float(m)+second)

#绘制（收藏量，评论数，播放量）的三维散点图
def scatter_collection_review_play():
    df = getMessageData()
    newdf = df.groupby(['collection','review']).play.mean().reset_index()
    newdf = newdf.loc[newdf['collection'] < 500]
    newdf = newdf.loc[newdf['review'] < 500]
    scatter_collection_review_play_data = newdf.values.tolist()
    scatter_collection_review_play_data.insert(0,list(newdf.columns))
    print(scatter_collection_review_play_data)
    return scatter_collection_review_play_data

#绘制播放量15万以下与以上的播放量与收藏量与评论量的关系
#柱状图与散点图的转化
def bar_scatter():
    df = getMessageData()
    newdf = df.groupby(['collection', 'review']).play.mean().reset_index()
    newdf1 = newdf.loc[newdf['play'] < 150000]
    newdf2 = newdf.loc[newdf['play'] >= 150000]
    newdf2 = newdf2.loc[newdf2['play']<500000]
    play_low_data = newdf1.iloc[:,0:2].copy()
    play_high_data = newdf2.iloc[:,0:2].copy()
    play_low_data = play_low_data.values.tolist()
    play_high_data = play_high_data.values.tolist()
    print(play_low_data)
    print("---------------------")
    print(play_high_data)
    return play_low_data,play_high_data

#绘制热榜出现次数前10的歌手
def pie_time_player():
    df = getHotsonglist()
    newdf1 = df.iloc[:, 1:3].copy()
    newdf2 = newdf1['singer'].value_counts().sort_values(ascending=False).head(10)
    data = {'player':newdf2.index,'count':newdf2.values}
    data2 = pd.DataFrame(data)
    pie_time_player_data = [{
        "value":value['count'],
        "name":value['player']
    }for _, value in data2.iterrows()]
    print(pie_time_player_data)
    return pie_time_player_data

if __name__ == '__main__':
    getMap_siger()

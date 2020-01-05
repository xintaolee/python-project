#coding=utf-
#引入模块和模块中的函数
from flask import Flask,render_template,request
import pandas as pd
import numpy as np
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Page, Pie
from prettytable import PrettyTable
from pyecharts.faker import Faker
from pyecharts import options as opts
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import csv

#利用pandas模块读取CSV数据文件
af = pd.read_csv("data/total-cancer-deaths-by-type.csv",encoding='ANSI')
bf = pd.read_csv("data/share-population-with-cancer.csv",encoding='ANSI')
cf = pd.read_csv("data/cancer-death-rates.csv",encoding='ANSI')
df = pd.read_csv("data/share-of-cancer-deaths-attributed-to-tobacco.csv",encoding='ANSI')
hf = pd.read_csv("data/survise-from-lung-cancer.csv",encoding='ANSI')
app = Flask(__name__)

#生成吸烟致癌症死亡率和癌症类型的两个图的后端代码
@app.route('/')
def hello_world():
 bar = (
        Bar()
.add_xaxis(['1990年', '1995年', '2000年', '2005年', '2006年', '2010年', '2016年'])
.add_yaxis("世界吸烟致癌症死亡率", ['23.6', '24', '23.7', '23.9', '23.6', '23.2', '22.1'])
.add_yaxis("中国吸烟致癌症死亡率", ['18.3', '18.6', '20.8', '23.4', '23.2', '23.9', '22'])
.add_yaxis('俄国吸烟致癌症死亡率', ['57.6', '57.7', '57.7', '57', '56.8', '57', '57.1'])
.add_yaxis("'美国吸烟致癌症死亡率", ['39.7', '40.5', '40', '39.1', '38.6', '36.6', '36'])
.set_global_opts(title_opts=opts.TitleOpts(title="世界吸烟致癌症死亡率", subtitle="副标题"))
        )
 line = (
       Line()
.add_xaxis(['2017年', '2016年', '2015年', '2014年', '2013年'])
.add_yaxis("肝癌", ['3032141', '2973889', '2879212', '2763830', '2665300'])
.add_yaxis("乳腺癌", ['2087821', '2052430', '2008660', '1945659', '1884618'])
.add_yaxis("胃癌", ['3158640', '3152218', '3098867', '3019719', '2967585'])
.add_yaxis("结直肠癌", ['3141681', '3085910', '3002722', '2899632', '2822919'])
.add_yaxis("肺癌", ['6723249', '6625799', '6441441', '6185396', '5976504'])
.set_global_opts(
   title_opts=opts.TitleOpts(title="癌症类型", subtitle="副标题"),
   tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
   toolbox_opts=opts.ToolboxOpts(is_show=True, orient="vertical", pos_left="right", pos_top="middle")
       )
   )
 map=timeline_map()
 return render_template("index.html",#后端代码渲染图到index.html前端页面
              bar_data=bar.dump_options(),#.dump_options()函数渲染图到前端页面，由bar_data变量在前端页面进行接收
              line_data=line.dump_options()#.dump_options()函数渲染图到前端页面，由line_data变量在前端页面进行接收

                            )


#生成世界肺癌生存率的图
def timeline_map():
    tl = Timeline()
    for i in range(2015, 2018):
        map0 = (
            Map()
                .add(
                "世界世界肺癌生存率",list(zip(list(cf.地区),list(cf["{}年".format(i)]))),"world",is_map_symbol_show= False
                )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界肺癌生存率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=5, max_=40),

            )
        )
        tl.add(map0, "{}年".format(i))
    return tl


timeline_map_scl=timeline_map()#调用函数并且把值传给timeline_map_scl变量
timeline_map_scl.render('世界肺癌生存率.html')#利用.render()函数生成该图的HTML页面

#生成世界癌症死亡人数的图
def timeline_map_death() -> 'Timeline':
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
                .add(
                "世界癌症死亡人数",list(zip(list(cf.地区), list(cf["{}年".format(i)]))), "world", is_map_symbol_show=False
                )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界癌症死亡人数".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=40, max_=280),

            )
        )
        tl.add(map0, "{}年".format(i))
    return tl
timeline_map_dea=timeline_map_death()#调用函数并且把值传给timeline_map_dea变量
timeline_map_dea.render('2008-2017十年世界癌症死亡人数.html')#利用.render()函数生成该图的HTML页面

#生成世界癌症患病率的图
def timeline_map_hbl() ->'Timeline':
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
                .add(
                "世界癌症患病率", list(zip(list(bf.地区), list(bf["{}年".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界癌症患病率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=0, max_=6),

            )
        )
        tl.add(map0, "{}年".format(i))
    return tl
timeline_map_hb=timeline_map_hbl()#调用函数并且把值传给timeline_map_hb变量
timeline_map_hb.render('2008-2017十年世界癌症患病率.html')#利用.render()函数生成该图的HTML页面


#渲染患病率的图到前端页面
@app.route('/world_hbl',methods=['POST'])
def world_hbl() -> 'html':
    with open("data/share-population-with-cancer.csv",encoding='ANSI') as log:#打开CSV文件，log作为文件流
        rows = csv.reader(log)  #利用csv.reader()函数读取log文件流数据并赋值给rows
        list_data=list(rows)    #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
    with open("2008-2017十年世界癌症患病率.html", encoding="utf8", mode="r") as f1:  #打开CSV文件，f1作为文件流
        plot_all_1 = "".join(f1.readlines()) #f1.readlines()读取f1的数据，并且转化为字符串
        title = '2008-2017十年世界癌症患病率'    #网页标题
        interactive_controls = ['癌症患病率地图']#绑定前端页面的按钮以实现Python页面与前端页面交互
        return render_template('results2.html', #向/world_hbl返回result.html页面
                            the_plot_all_1 = plot_all_1,#赋值给变量以渲染图表到前端页面
                            the_title = title,#赋值给变量以渲染标题到前端页面
                            the_list = list_data,#渲染列表到前端
                            )
#渲染世界癌症死亡人数的图到前端页面
@app.route('/world_death_person',methods=['POST'])
def world_death_person() -> 'html':
    with open("data/cancer-death-rates.csv",encoding='ANSI') as log:#打开CSV文件，log作为文件流
        rows = csv.reader(log)  #利用csv.reader()函数读取log文件流数据并赋值给rows
        list_data=list(rows)    #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
    with open("2008-2017十年世界癌症死亡人数.html", encoding="utf8", mode="r") as f1: #打开CSV文件，f1作为文件流
        plot_all_1 = "".join(f1.readlines())    #f1.readlines()读取f1的数据，并且转化为字符串
        interactive_controls =  ['世界癌症死亡人数']    #绑定前端页面的按钮以实现Python页面与前端页面交互
        title = '2008-2017十年世界癌症死亡人数'   #网页标题
        return render_template('results2.html',     #向/world_death_person返回result2.html页面
                            the_plot_all_1 = plot_all_1,#赋值给变量以渲染图表到前端页面
                            the_title = title,  #赋值给变量以渲染标题到前端页面
                           the_list = list_data #渲染列表到前端
                           )
#渲染世界肺癌生存率的图到前端页面
@app.route('/world_lung',methods=['POST'])
def world_lung() -> 'html':
    with open("data/survise-from-lung-cancer.csv",encoding='ANSI') as log:  #打开CSV文件，log作为文件流
        rows = csv.reader(log)      #利用csv.reader()函数读取log文件流数据并赋值给rows
        list_data=list(rows)        #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
    with open("世界肺癌生存率.html", encoding="utf8", mode="r") as f1: #打开CSV文件，f1作为文件流
        plot_all_1 = "".join(f1.readlines())    #f1.readlines()读取f1的数据，并且转化为字符串
        interactive_controls =  ['世界肺癌生存率'] #绑定前端页面的按钮以实现Python页面与前端页面交互
        title = '2008-2017十年世界肺癌生存率'    #网页标题
        return render_template('results2.html', #向/world_lung返回result2.html页面
                            the_plot_all_1 = plot_all_1,#赋值给变量以渲染图表到前端页面
                            the_title = title,  #赋值给变量以渲染标题到前端页面
                           the_list = list_data,    #渲染列表到前端
                            )
#下拉框跳转功能
@app.route('/world',methods=['POST'])
def world() ->'html':
    result=request.form['select'] #获取前端页面下拉框数据
    if '癌症患病率地图'== result:  #if循环，若前端数据与这个字符串一致
        with open("data/share-population-with-cancer.csv", encoding='ANSI') as log: #打开CSV文件，log作为文件流
            rows = csv.reader(log)   #利用csv.reader()函数读取log文件流数据并赋值给rows
            list_data = list(rows)  #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
        with open("2008-2017十年世界癌症患病率.html", encoding="utf8", mode="r") as f2:  #打开CSV文件，f2作为文件流
            plot_all = "".join(f2.readlines())  #f2.readlines()读取f2的数据，并且转化为字符串
            title="2008-2017十年世界癌症患病率"   #网页标题
    elif '世界癌症死亡人数' ==result:    #elif类似于if，表示若前端数据与这个字符串一致
        with open("data/cancer-death-rates.csv", encoding='ANSI') as log:   #打开CSV文件，log作为文件流
            rows = csv.reader(log)  #利用csv.reader()函数读取log文件流数据并赋值给rows
            list_data = list(rows)  #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
        with open("2008-2017十年世界癌症死亡人数.html", encoding="utf8", mode="r") as f2: #打开CSV文件，f2作为文件流
            plot_all = "".join(f2.readlines())  #f2.readlines()读取f2的数据，并且转化为字符串
            title = "2008-2017十年世界癌症死亡人数"   #网页标题
    elif '世界肺癌生存率' ==result:    #elif类似于if，可以有多个elif，表示若前端数据与这个字符串一致
        with open("data/survise-from-lung-cancer.csv", encoding='ANSI') as log: #打开CSV文件，log作为文件流
            rows = csv.reader(log)  #利用csv.reader()函数读取log文件流数据并赋值给rows
            list_data = list(rows)  #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
        with open("世界肺癌生存率.html", encoding="utf8", mode="r") as f2: #打开CSV文件，f2作为文件流
            plot_all = "".join(f2.readlines()) #f2.readlines()读取f2的数据，并且转化为字符串
            title = "世界肺癌生存率" #网页标题
    return render_template('results2.html', #根据前端传值返回相应的图表和文字到results2.html，并且传入/world页面
                           the_plot_all_1= plot_all, #赋值给变量以渲染图表到前端页面
                           the_list=list_data, #渲染列表到前端
                           the_title=title)
#吸烟致癌症死亡率-表格图
@app.route("/tobacco",methods=['POST'])#前端页面按钮提交跳转到/tobacco页面
def tobacco():
    with open("data/share-of-cancer-deaths-attributed-to-tobacco.csv",encoding='ANSI') as log:  #打开CSV文件，log作为文件流
        rows = csv.reader(log)  #利用csv.reader()函数读取log文件流数据并赋值给rows
        list_data=list(rows)    #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
        title='吸烟导致癌症死亡比例'  #网页标题
    return render_template('tobacco.html', #向/tobacco返回result2.html页面
                            the_title= title,
                            the_list=list_data #渲染列表到前端
                           )

@app.route("/field",methods=['POST'])
def field():
    with open("data/total-cancer-deaths-by-type.csv",encoding='ANSI') as log:   #打开CSV文件，log作为文件流
        rows = csv.reader(log)  #利用csv.reader()函数读取log文件流数据并赋值给rows
        list_data=list(rows)    #利用list()函数使变量rows转化为嵌套列表，并且赋给list_data
        title='世界各癌症类型死亡率'  #网页标题
    return render_template('field.html',    #向/tobacco返回result2.html页面
                            the_title= title,   #网页标题
                            the_list=list_data  #the_list=list_data #渲染列表到前端
                           )




if __name__ == '__main__':
    app.run(debug=True)
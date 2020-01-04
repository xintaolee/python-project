from flask import Flask,render_template,request
import pandas as pd
import numpy as np
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Page, Pie
from prettytable import PrettyTable
from pyecharts.faker import Faker
from pyecharts import options as opts
import plotly as py

import demo7

af=pd.read_csv("data/total-cancer-deaths-by-type.csv",encoding='ANSI')
bf=pd.read_csv("data/share-population-with-cancer.csv",encoding='ANSI')
cf = pd.read_csv("data/cancer-death-rates.csv",encoding='ANSI')
df = pd.read_csv("data/share-of-cancer-deaths-attributed-to-tobacco.csv",encoding='ANSI')
ef=pd.read_csv("data/survise-from-lung-cancer.csv",encoding='ANSI')



# print(list(cf.地区))
app = Flask(__name__)

df1 = pd.read_csv("癌症人口.csv",encoding = 'UTF-8')
regions_available = list(df1.地区.dropna().unique())

@app.route('/癌症人口',methods=['POST'])
def hu_run_select() -> 'domeload.html':
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df1.query("地区=='{}'".format(the_region))

# 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="地区", asFigure=True)
    py.offline.plot(fig, filename="download.html",auto_open=False)
    with open("download.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('download.html',
                            the_plot_all = plot_all,
                     # the_plot_all = [],
                            the_res = data_str,
                            the_select_region=regions_available,
                           )

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
 return render_template("index.html",
              bar_data=bar.dump_options(),
              line_data=line.dump_options()

                            )



def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2015, 2018):
        map0 = (
            Map()
                .add(
                "世界肺癌生存率", list(zip(list(ef.地区), list(ef["{}年".format(i)]))), "world", is_map_symbol_show=False
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


timeline_map_scl=timeline_map()
timeline_map_scl.render('世界肺癌生存率.html')


def timeline_map_death() -> Timeline:
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
                .add(
                "世界癌症死亡人数", list(zip(list(cf.地区), list(cf["{}年".format(i)]))), "world", is_map_symbol_show=False
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
timeline_map_dea=timeline_map_death()
timeline_map_dea.render('2008-2017十年世界癌症死亡人数.html')


def timeline_map_hbl() -> Timeline:
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
timeline_map_hb=timeline_map_hbl()
timeline_map_hb.render('2008-2017十年世界癌症患病率.html')


#患病率
@app.route('/world_hbl',methods=['POST'])
def yi_yu_select_1() -> 'html':
    with open("2008-2017十年世界癌症患病率.html", encoding="utf8", mode="r") as f1:
        plot_all_1 = "".join(f1.readlines())
#     the_region = request.form["the_region_selected"]
#     print(the_region)
    interactive_controls =  ['癌症患病率地图']
    title = '2008-2017十年世界癌症患病率'
    return render_template('results2.html',
                            the_plot_all_1 = plot_all_1,
                            the_title = title,
#                             the_res = data_str,
                            the_select_region=interactive_controls)
#世界癌症死亡人数
@app.route('/world_death_person',methods=['POST'])
def world_death_person() -> 'html':
    with open("2008-2017十年世界癌症死亡人数.html", encoding="utf8", mode="r") as f1:
        plot_all_1 = "".join(f1.readlines())
#     the_region = request.form["the_region_selected"]
#     print(the_region)
    interactive_controls =  ['世界癌症死亡人数']
    title = '2008-2017十年世界癌症死亡人数'
    return render_template('results2.html',
                            the_plot_all_1 = plot_all_1,
                            the_title = title,
#                             the_res = data_str,
                            the_select_region=interactive_controls)
#世界肺癌生存率
@app.route('/world_lung',methods=['POST'])
def world_lung() -> 'html':
    with open("世界肺癌生存率.html", encoding="utf8", mode="r") as f1:
        plot_all_1 = "".join(f1.readlines())
#     the_region = request.form["the_region_selected"]
#     print(the_region)
    interactive_controls =  ['世界肺癌生存率']
    title = '2008-2017十年世界肺癌生存率'
    return render_template('results2.html',
                            the_plot_all_1 = plot_all_1,
                            the_title = title,
#                             the_res = data_str,
                            the_select_region=interactive_controls)
#吸烟致癌症死亡率-折线图
@app.route("/tobacco" )
def tobacco():
    # lines = (
    #     Line()
    #         .add_xaxis(list(df.set_index('指标').columns))
    #         .add_yaxis("世界吸烟致癌症死亡率", list(df.iloc[0])[1:])
    #         .add_yaxis("中国吸烟致癌症死亡率", list(df.iloc[1])[1:])
    #         .add_yaxis("俄国吸烟致癌症死亡率	", list(df.iloc[2])[1:])
    #         .add_yaxis("美国吸烟致癌症死亡率", list(df.iloc[3])[1:])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(title="吸烟致癌症死亡率", subtitle="副标题"),
    #         tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    #         toolbox_opts=opts.ToolboxOpts(is_show=True, orient="vertical", pos_left="right", pos_top="middle")
    #     )
    # )

    title='吸烟导致癌症死亡比例'
    return render_template('tobacco.html',
                           # lines_data=lines.dump_options(),
                            the_title= title,
                           list=df
                           )
data=list(df)
print(data)
if __name__ == '__main__':
    app.run(debug=True)

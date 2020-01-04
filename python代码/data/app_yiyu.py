from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Scatter
from pyecharts.globals import ChartType, SymbolType
from pyecharts.components import Table
from flask import Flask, render_template, request
import pandas as pd

# 总表
df_z = pd.read_csv('number-with-depression-by-country.csv',encoding = 'gbk')

# 总人数
df_zrs = pd.read_csv('number-with-depression-by-country-zrs.csv',\
                keep_default_na=False, na_values='na_rep', dtype=str)
# 患病率
df_hbl = pd.read_csv('number-with-depression-by-country-hbl.csv',\
                keep_default_na=False, na_values='na_rep')
# 男性患病人数
df_man = pd.read_csv('number-with-depression-by-country-man.csv',\
                keep_default_na=False, na_values='na_rep')
# 女性患病人数
df_woman = pd.read_csv('number-with-depression-by-country-woman.csv',\
                keep_default_na=False, na_values='na_rep')


# 总人数
def timeline_map_zrs() -> Timeline:
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
            .add(
                "世界抑郁症总人数", list(zip(list(df_zrs.地区.unique()),list(df_zrs["{}".format(i)]))), "world",is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界抑郁症总人数".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_= 0,
                                                  max_= df_zrs["2017"].max(),
                                                  series_index=0),
            )
        )
        
        tl.add(map0,"{}年".format(i))
    return tl

Timeline_map_zrs = timeline_map_zrs()
Timeline_map_zrs.render('世界抑郁症总人数.html')

# 患病率
def timeline_mapdf_hbl() -> Timeline:
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
            .add(
                "世界抑郁症患病率", list(zip(list(df_hbl.地区.unique()),list(df_hbl["{}".format(i)]))), "world",is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界抑郁症患病率".format(i)),
                visualmap_opts=opts.VisualMapOpts(
                    min_= df_hbl["2016"].min(),
                    max_=df_hbl["2008"].max(),
                    series_index=0,
                    is_piecewise=True),
            )
        )
        
        tl.add(map0,"{}年".format(i))
    return tl

Timeline_mapdf_hbl = timeline_mapdf_hbl()
Timeline_mapdf_hbl.render('世界抑郁症患病率.html')

def timeline_bar() -> Timeline:
    x = list(df_man.地区)
    tl = Timeline()
    for i in range(2008, 2018):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("女性患病人数", list(df_woman["{}".format(i)]))
            .add_yaxis("男性患病人数", list(df_man["{}".format(i)]))
            .reversal_axis()
            .set_global_opts(title_opts=opts.TitleOpts("{}年世界男性和女性抑郁症人数对比".format(i)),
                            datazoom_opts=opts.DataZoomOpts(orient="vertical",range_start="50",range_end="60"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
        )
        )
        tl.add(bar, "{}年".format(i))
    return tl

Timeline_bar = timeline_bar()
Timeline_bar.render('男性和女性抑郁症人数对比.html')

# tab = Tab()
# tab.add(timeline_map_zrs(), "世界抑郁症总人数")
# tab.add(timeline_mapdf_hbl(), "世界抑郁症患病率")
# # tab.add(timeline_scatter(), "世界男性、女性患病人数对比")
# tab.add(timeline_bar(), "世界男性、女性患病人数对比")
# # tab.add(bar_reversal_axis(), "世界男性、女性患病人数对比")
# tab.render('组合图.html')
# # tab.render_notebook()

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hu_run_2019():
    data_str = df_z.to_html()
#     the_region = request.form["the_region_selected"]
    interactive_controls = ['首页']
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('results2.html',
                           the_title = title,
                           the_res = data_str,
                           the_select_region=interactive_controls)   

@app.route('/world_number',methods=['POST'])
def yi_yu_select() -> 'html':
    with open("世界抑郁症总人数.html", encoding="utf8", mode="r") as f: 
        plot_all = "".join(f.readlines())
    the_region = request.form["the_region_selected"]
    print(the_region)
    the_plot_all = plot_all
#     if the_region == '1':
#         the_plot_all = plot_all
    interactive_controls =  ['总人数地图']
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('results2.html',
                            the_plot_all = plot_all,
                            the_title = title,
#                             the_res = data_str,
                            the_select_region=interactive_controls)

@app.route('/world_hbl',methods=['POST'])
def yi_yu_select_1() -> 'html':
    with open("世界抑郁症患病率.html", encoding="utf8", mode="r") as f1: 
        plot_all_1 = "".join(f1.readlines())
#     the_region = request.form["the_region_selected"]
#     print(the_region)
    interactive_controls =  ['患病率地图']
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('results2.html',
                            the_plot_all_1 = plot_all_1,
                            the_title = title,
#                             the_res = data_str,
                            the_select_region=interactive_controls)

@app.route('/world_man_woman',methods=['POST'])
def yi_yu_select_2() -> 'html':
    with open("男性和女性抑郁症人数对比.html", encoding="utf8", mode="r") as f2: 
        plot_all_2 = "".join(f2.readlines())
#     the_region = request.form["the_region_selected"]
#     print(the_region)
    interactive_controls =  ['男女对比图']
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('results2.html',
                            the_plot_all_2 = plot_all_2,
                            the_title = title,
#                             the_res = data_str,
                            the_select_region=interactive_controls)

if __name__ == '__main__':
    app.run(port = 8004, debug=True)   # debug=True, 在py使用, 在ipynb不使用

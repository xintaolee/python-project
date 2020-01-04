# @Time    : 2020/1/4 16:26
# @Author  : xintao
from flask import Flask,render_template,request
import pandas as pd
import plotly as py

app = Flask(__name__)


df1 = pd.read_csv("癌症人口.csv",encoding = 'UTF-8')
regions_available = list(df1.地区.dropna().unique())

@app.route('/癌症人口',methods=['POST'])
def hu_run_select() -> 'demo7.html':
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df1.query("地区=='{}'".format(the_region))

# 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="地区", asFigure=True)
    py.offline.plot(fig, filename="demo7.html",auto_open=False)
    with open("demo7.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('dome7.html',
                            the_plot_all = plot_all,
                     # the_plot_all = [],
                            the_res = data_str,
                            the_select_region=regions_available,
                           )

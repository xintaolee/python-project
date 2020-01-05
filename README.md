#  python-project
## 欢迎老师查看我的期末项目
### 本人李鑫桃 学号181013050 18网络与新媒体3班
- 本学期我和我的小伙伴合作完成了一个python的期末项目
- [Github URL](https://github.com/xintaolee/python-project)
- 这是我们期末项目的链接（已上传到pythonanywhere）：
-[Pythonanywhere主页](http://lixintao.pythonanywhere.com/)
我们的网站有**7个URL以下URL除主页外均不能直接打开，只有在前端执行命令后后台才会工作，才能打开**：
1. [主页](http://lixintao.pythonanywhere.com/)
2. [2008-2017十年世界癌症患病率](http://lixintao.pythonanywhere.com/world_hbl)
3. [2008-2017十年世界癌症死亡人数](http://lixintao.pythonanywhere.com/world_death_person)
4. [2008-2017十年世界肺癌生存率](http://lixintao.pythonanywhere.com/world_lung)
5. [吸烟导致癌症死亡比例](http://lixintao.pythonanywhere.com/tobacco)
6. [世界各癌症类型死亡率](http://lixintao.pythonanywhere.com/field)
7. [下拉框动图显示](http://lixintao.pythonanywhere.com/world)
#### **这几个URL以下URL除主页外均不能直接打开，只有在前端执行命令后后台才会工作，才能打开**展示的功能分别是：
1. python语法和html语法的合理嵌套，数据的动态现实、数据的传递交互
- [主页](http://lixintao.pythonanywhere.com/)
- [2008-2017十年世界癌症患病率](http://lixintao.pythonanywhere.com/world_hbl)、
- [2008-2017十年世界癌症死亡人数](http://lixintao.pythonanywhere.com/world_death_person)
- [2008-2017十年世界肺癌生存率](http://lixintao.pythonanywhere.com/world_lung)
2. for循环、列表的嵌套、复杂数据结构的循环、条件判断（**以下URL除主页外均不能直接打开，只有在前端执行命令后后台才会工作，才能打开）**- [吸烟导致癌症死亡比例](http://lixintao.pythonanywhere.com/tobacco)
- [世界各癌症类型死亡率](http://lixintao.pythonanywhere.com/field)
- [下拉框动图显示](http://lixintao.pythonanywhere.com/world)

- 我参与负责的页面（以下URL除主页外均不能直接打开，只有在前端执行命令后后台才会工作，才能打开）：
1. [主页](http://lixintao.pythonanywhere.com/)
2. [2008-2017十年世界癌症患病率](http://lixintao.pythonanywhere.com/world_hbl)
3. [2008-2017十年世界癌症死亡人数](http://lixintao.pythonanywhere.com/world_death_person)
4. [世界各癌症类型死亡率](http://lixintao.pythonanywhere.com/field)
5. [下拉框动图显示](http://lixintao.pythonanywhere.com/world)

设计了flask的嵌套、动态表格下拉框、以及前端部分页面的设计、for循环、设计基本交互功能的HTML5控件、基本的for循环。
[具体截图放在github上](https://github.com/xintaolee/python-project/tree/master/images)

####	HTML档描述(更详细的注释已写在每个html档里)
- index.html是“基文档”html页面的都是基于此拓展的
- field.html是显示表格文件的文档
- base.html是显示首页的文档
- result2.html是显示跳转结果页的文档
- tabacco.html是显示癌症表格的文档
- 使用了flask框架和jinji2模板，通过extend指令实现模板继承。
- 使用了bookstrap前端按钮、下拉导航栏和轮播图。
- 使用了pyecharts设计动态图标
- 使用了css3响应式网页

####	Python档描述(更详细的注释已写在webapp.py档里)
webapp.py是整个flask框架的核心，集合了所有python代码包括所有嵌套在html的代码、动作代码和函数。
####	Web App动作描述(更详细的注释已写在webapp.py档里)
例如点击某图表的下拉框名字会跳转到对应的页面
在动态图表中，点击某个点会显示相应的数据



# @Time    : 2020/1/4 17:47
# @Author  : xintao

# 创建主窗口
import tkinter as tk

window = tk.Tk()
window.title('菜单栏')
window.geometry('300x200')

# 创建标签，用于显示内容
l = tk.Label(window, bg='green', width=25, height=2, text='empty')
l.pack()

# 下方command参数的do_job函数
counter = 0


def do_job():
    global counter
    l.config(text='do' + str(counter))
    counter += 1


# 　创建一个菜单栏，这里我们可以把它理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
# 　定义一个空的菜单单元
filemenu = tk.Menu(menubar, tearoff=0)  # tearoff意为下拉
# 　将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='文件', menu=filemenu)
# 　在`文件`中加入`新建`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
# 　如果点击这些单元, 就会触发`do_job`的功能
filemenu.add_command(label='新建', command=do_job)
filemenu.add_command(label='打开', command=do_job)
filemenu.add_command(label='保存', command=do_job)
# 分隔线
filemenu.add_separator()
filemenu.add_command(label='退出', command=window.quit)

# 创建编辑菜单
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='剪切', command=do_job)
editmenu.add_command(label='复制', command=do_job)
editmenu.add_command(label='粘贴', command=do_job)

# 在‘文件’下拉菜单中创建二级菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='导入', menu=submenu, underline=0)
submenu.add_command(label='导入图片', command=do_job)

window.config(menu=menubar)  # 加上这代码，才能将菜单栏显示
window.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from Weather_Spider import Weather_Get
from threading import Thread
import datetime
import time

'''
5-1
1.打开首页定位当前位置获取天气    (ip定位+jieba分词+城市号+城市天气) **5.11实现**
2.用户手动选择，查看当前所选城市天气 （Toplevel+Combobox） **已实现**

5-14
1.加入notepad，显示多个城市天气    （notebook Frame）    **已实现**
2.频繁刷新检测（线程计时10秒）   **已实现**
3.用户选择主题    (Menu.add_radiobutton())    **已实现**
4.一个窗口多个Combobox，怎样处理选择事件  **已实现**

5-15
1.右击notebook frame标题出现“关闭”菜单  **已砍掉**
2.用户添加了城市后，label出现在了最后的Frame中  **未实现**

'''
imgs = ['./img/loading.png']


class App:
    def __init__(self):
        self.w = Tk()
        self.w.title('天气预报小工具-v1.0')
        width = 600
        height = 282
        left = (self.w.winfo_screenwidth() - width) / 2
        top = (self.w.winfo_screenheight() - height) / 2
        self.w.geometry('%dx%d+%d+%d' % (width, height, left, top))
        self.w.iconbitmap('biticon.ico')
        self.w.resizable(False, False)
        self.cerate_widgets()
        self.first_launch()
        self.set_widgets()
        self.place_widgets()
        self.thread_it(self.show_local_weather)
        self.w.mainloop()

    def cerate_widgets(self):
        self.note = ttk.Notebook()
        self.f1 = Frame()
        self.tree = ttk.Treeview(self.f1)
        self.l1_var = StringVar()
        self.l1 = ttk.Label(self.f1, textvariable=self.l1_var)
        self.m = Menu(self.w)
        self.w['menu'] = self.m
        self.s1 = Menu(self.m, tearoff=False)
        self.s2 = Menu(self.m, tearoff=False)
        self.s3 = Menu(self.m, tearoff=False)

    def set_widgets(self):
        self.location = []
        style = ttk.Style(self.w)
        style.theme_use("default")
        columns = ('rq', 'tq', 'flfx', 'zdqw', 'zgqw')
        self.tree.config(show='headings', columns=columns)
        self.tree.column(columns[0], anchor=CENTER, minwidth=95, width=110)
        self.tree.column(columns[1], anchor=CENTER, minwidth=60, width=70)
        self.tree.column(columns[2], anchor=CENTER, minwidth=90, width=100)
        self.tree.column(columns[3], anchor=CENTER, minwidth=90, width=100)
        self.tree.column(columns[4], anchor=CENTER, minwidth=90, width=100)
        self.tree.heading('rq', text='日期')
        self.tree.heading('tq', text='天气')
        self.tree.heading('flfx', text='风向风力')
        self.tree.heading('zdqw', text='最低气温')
        self.tree.heading('zgqw', text='最高气温')
        self.m.add_cascade(label='开始', menu=self.s1)
        self.s1.add_command(label='aaa', command='')
        self.s1.add_separator()
        self.s1.add_command(label='退出', command=self.quit_window)
        self.m.add_cascade(label='操作', menu=self.s2)
        self.s2.add_command(label='刷新', command=lambda: self.thread_it(self.refresh_weather))
        self.s2.add_command(label='添加城市', command=lambda: self.thread_it(self.select_city), state='disable')
        s2_sub = Menu(self.s2, tearoff=0)
        self.s2.add_separator()
        self.s2.add_cascade(label='更换主题', menu=s2_sub)
        self.m.add_cascade(label='关于', menu=self.s3)
        self.s3.add_command(label='关于作者',
                            command=lambda: messagebox.showinfo('关于作者', '作者很神秘，什么都没留下'))
        self.tree.tag_configure('evenColor', background='lightblue')
        self.w.protocol('WM_DELETE_WINDOW', self.quit_window)
        themes = ['default', 'clam', 'alt', 'classic']
        self.themevar = StringVar()
        for i, t in enumerate(themes):
            s2_sub.add_radiobutton(label=t, variable=self.themevar, command=lambda: self.thread_it(self.change_theme),
                                   value=t)
        self.themevar.set('default')

    def place_widgets(self):
        self.note.place(x=0, y=0, width=600, height=282)
        self.tree.place(x=0, y=0, width=600, height=150)
        self.l1.place(x=0, y=150, height=85, width=600)

    def first_launch(self):
        '''
        第一次启动，展示加载图片提示信息
        :return:
        '''
        self.start_time = time.time()
        paned = PanedWindow(self.w)
        self.img = imgs
        img = Image.open(self.img[0])
        paned.image = ImageTk.PhotoImage(img)
        self.load_img = Label(self.w, image=paned.image)
        self.load_lab = Label(self.w, text='Loading...')
        self.load_img.pack()
        self.load_lab.pack()

    def show_local_weather(self):
        '''
        展示定位天气信息
        :return:
        '''
        self.l1_var.set('正在刷新天气......')
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        try:
            city, item = Weather_Get().get_local_weather()
            self.load_img.destroy()
            self.load_lab.destroy()
            self.s2.entryconfig('添加城市', state='normal')
            self.note.add(self.f1, text=city)
            i = 0
            for data in item['recent']:
                self.tree.insert('', i, values=(
                    data.get('日期'), data.get('天气'), data.get('风力风向'), data.get('最低气温'),
                    data.get('最高气温')))
                i += 1
            self.l1_var.set(
                f'今天：{self.show_date()}\n当前所在地区：{city}\n当前气温：{item["now"]}\n感冒指数：{item["ganmao"]}')
        except TypeError:
            messagebox.showerror('错误', '天气信息加载失败！')
            self.l1_var.set('天气信息加载失败！')
            self.s2.entryconfig('添加城市', state='normal')

    def refresh_weather(self):
        """
        刷新天气后，10秒内不能点击刷新
        :return:
        """
        self.s2.entryconfig('刷新', state='disable')
        self.show_local_weather()
        self.thread_it(self.wait_time)

    def wait_time(self):
        '''
        线程计时10s，十秒后刷新按钮可点击
        :return:
        '''
        time.sleep(10)
        self.s2.entryconfig('刷新', state='normal')

    def show_date(self):
        """
        展示日期信息，便于天气展示
        :return:
        """
        date = str(datetime.date.today())
        year, month, day = date.split('-')
        week_day_dict = {
            0: '星期一',
            1: '星期二',
            2: '星期三',
            3: '星期四',
            4: '星期五',
            5: '星期六',
            6: '星期日 ',
        }
        now = datetime.datetime.now()
        date_index = now.weekday()
        return f'{year}年{month}月{day}日 {week_day_dict[date_index]}'

    def select_city(self):
        '''
        Toplevel让用户选择城市，后台获取城市号
        :return:
        '''
        self.t = Toplevel()
        self.t.resizable(0, 0)
        width = 300
        height = 140
        left = (self.t.winfo_screenwidth() - width) / 2
        top = (self.t.winfo_screenheight() - height) / 2
        self.t.geometry('%dx%d+%d+%d' % (width, height, left, top))
        self.t.title('选择城市')
        self.tl1 = ttk.Label(self.t, text='请选择城市：')
        self.tl1.pack()
        provinces = Weather_Get().get_provinces()
        self.tc1 = ttk.Combobox(self.t, justify='center', state='readonly', value=provinces)
        self.tc2 = ttk.Combobox(self.t, justify='center', state='readonly')
        self.tc1.pack()
        self.tc1.bind('<<ComboboxSelected>>', self.show_tc2_value)
        self.tc2.bind('<<ComboboxSelected>>', self.show_tc3_value)
        self.tc2.pack()
        self.tc3 = ttk.Combobox(self.t, justify='center', state='readonly')
        self.tc3.pack()
        self.tb1 = ttk.Button(self.t, text='选择', command=lambda: self.thread_it(self.ack_city))
        self.tb1.pack(pady=10)

    # ----待完善
    def ack_city(self):
        '''
        Toplevel中选择了城市，选择使用notebook中建立Frame展示所选城市信息
        :return:
        '''
        cityno = self.get_city_no()
        weather_item = Weather_Get().get_weather(cityno)
        location = self.province_name + self.city_name + self.region
        if location in self.location:
            messagebox.showwarning('警告', '此城市已添加，请勿重复添加！')
        else:
            self.location.append(location)
            self.f2 = Frame(takefocus=True)
            self.note.add(self.f2, text=location)
            self.tree2 = ttk.Treeview(self.f2)
            columns = ('rq', 'tq', 'flfx', 'zdqw', 'zgqw')
            self.tree2.config(show='headings', columns=columns)
            self.tree2.column(columns[0], anchor=CENTER, minwidth=95, width=110)
            self.tree2.column(columns[1], anchor=CENTER, minwidth=60, width=70)
            self.tree2.column(columns[2], anchor=CENTER, minwidth=90, width=100)
            self.tree2.column(columns[3], anchor=CENTER, minwidth=90, width=100)
            self.tree2.column(columns[4], anchor=CENTER, minwidth=90, width=100)
            self.tree2.heading('rq', text='日期')
            self.tree2.heading('tq', text='天气')
            self.tree2.heading('flfx', text='风向风力')
            self.tree2.heading('zdqw', text='最低气温')
            self.tree2.heading('zgqw', text='最高气温')
            self.tree2.place(x=0, y=0, width=600, height=150)
            # label_='label'+str(self.click_no)
            # label_var='label'+str(self.click_no)+'_var'
            self.fl1_var = StringVar()
            self.fl1 = ttk.Label(self.f2, textvariable=self.fl1_var)
            self.fl1.place(x=0, y=150, height=85, width=600)
            items = self.tree2.get_children()
            for item in items:
                self.tree2.delete(item)
            try:
                item = weather_item
                city = location
                i = 0
                for data in item['recent']:
                    self.tree2.insert('', i, values=(
                        data.get('日期'), data.get('天气'), data.get('风力风向'), data.get('最低气温'),
                        data.get('最高气温')))
                    i += 1
                self.fl1_var.set(
                    f'今天：{self.show_date()}\n当前所在地区：{city}\n当前气温：{item["now"]}\n感冒指数：{item["ganmao"]}')
            except TypeError:
                messagebox.showerror('错误', '天气信息加载失败！')
                self.fl1_var.set(f'{city}天气信息加载失败！')
        self.t.destroy()

    def change_tab(self, *args):
        pass

    def show_tc2_value(self, event):
        '''
        展示"市"级信息
        :param event:
        :return:
        '''
        self.tc2.config(value=[])
        self.tc3.config(value=[])
        self.province_name = self.tc1.get()
        cities = Weather_Get().get_cities(self.province_name)
        self.tc2.config(value=cities)

    def show_tc3_value(self, event):
        '''
        展示"区/县"级信息
        :param event:
        :return:
        '''
        self.city_name = self.tc2.get()
        regions = Weather_Get().get_regions(self.province_name, self.city_name)
        self.tc3.config(value=regions)

    def get_city_no(self):
        """
        根据省、市、区、县 获取城市号
        :return: 城市号
        """
        self.region = self.tc3.get()
        city_no = Weather_Get().get_city_id_by_add(self.province_name, self.city_name, self.region)
        return city_no

    def change_theme(self, ):
        '''
        更换主题
        :return:
        '''
        theme = self.themevar.get()
        style = ttk.Style(self.w)
        style.theme_use(theme)

    def quit_window(self):
        ret = messagebox.askyesno('退出', '是否要退出？')
        if ret:
            self.w.destroy()

    def thread_it(self, func, *args):
        '''
        防止线程冲突
        :param func:
        :param args:
        :return:
        '''
        t = Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    a = App()

import random
import time
from tkinter import *
import tkinter.messagebox


class My_Test_GUI(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('选择困难专用')
        self.root.geometry('600x512')
        self.list_left_items = []

        # add label
        self.time_label = tkinter.Label(self.root, text='', fg='black', font=('微软雅黑', 20))
        self.time_label.pack(side='top')
        self.get_time()

        # add list
        self.list_left = tkinter.Listbox(self.root, font=('微软雅黑', 16))
        self.list_left.pack(side='left')
        self.list_right = tkinter.Listbox(self.root, font=('微软雅黑', 16))
        self.list_right.pack(side='right')

        #  add button
        self.button_add = tkinter.Button(self.root, text="增加", command=self.list_insert_left).pack()
        self.buttun_del = tkinter.Button(self.root, text="删除", command=self.list_delete).pack()
        self.buttun_clr = tkinter.Button(self.root, text="清空", command=self.list_clr).pack()
        self.buttun_init = tkinter.Button(self.root, text="初始化", command=self.list_init).pack()
        self.buttun_pick = tkinter.Button(self.root, text="选择", command=self.pick_left_random_to_right).pack()

        # add entry
        self.ent = tkinter.Entry(self.root, font=('微软雅黑', 16))
        self.ent.pack()

        #  windows main-loop
        self.root.mainloop()

    # get time now
    def get_time(self):
        self.timestr = time.strftime("%H:%M:%S")
        self.time_label.configure(text=self.timestr)
        self.root.after(1000, self.get_time)

    # initialize lists
    def list_init(self):
        self.list_left.delete(0, END)
        self.list_right.delete(0, END)
        for item in self.list_left_items:
            self.list_left.insert(END, item)

    # insert items into list
    def list_insert_left(self):
        if self.ent.get() != '':
            if self.list_left.curselection() == ():
                self.list_left.insert(self.list_left.size(), self.ent.get())
                self.list_left_items.append(self.ent.get())
            else:
                self.list_left.insert(self.list_left.curselection(), self.ent.get())
                self.list_left_items.append(self.ent.get())
            self.ent.delete(0, END)

    # clear list
    def list_clr(self):
        self.list_left.delete(0, END)
        self.list_right.delete(0, END)

    # delete item in list
    def list_delete(self):
        if self.list_left.curselection() != ():
            self.list_left.delete(self.list_left.curselection())

    # pick randomly
    def pick_left_random_to_right(self):
        for i in self.list_left.curselection():
            self.list_left_items.insert(self.list_left.get(i))
        len_list_left = len(self.list_left_items)
        tdd_pick = random.randint(0, len_list_left-1)
        self.list_right.insert(self.list_right.size(), str(self.list_left_items[tdd_pick]))
        tkinter.messagebox.showinfo('Successfull', str(self.list_left_items[tdd_pick]))


if __name__ == '__main__':
    My_Test_GUI()


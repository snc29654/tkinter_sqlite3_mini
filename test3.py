#!/usr/bin/python3
from tkinter.scrolledtext import ScrolledText
import tkinter
import tkinter as tk
import tkinter.simpledialog as sd
import sqlite3
from contextlib import closing
import sys
from tkinter import filedialog
from tkinter import filedialog as tkFileDialog
import os
from PIL import Image, ImageTk

class main_window(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(master,text="sqlite3 mini test")
        self.label.pack()
        
        button1 = tk.Button(root, text = 'DB読み出し', command=self.read_db)
        button1.pack() 
        button1.place(x=300, y=30)
        
        button2 = tk.Button(root, text = 'DB書き込み', command=self.write_db)
        button2.pack() 
        button2.place(x=380, y=30)

        button3 = tk.Button(root, text = '表示クリア', command=self.text_clear)
        button3.pack() 
        button3.place(x=460, y=30)

        button4 = tk.Button(root, text = 'DB消去', command=self.clear_db)
        button4.pack() 
        button4.place(x=540, y=30)


        self.textExample=ScrolledText(root, height=13,width=60, wrap=tkinter.CHAR)
        self.textExample.pack()
        self.textExample.place(x=150, y=100)
        
        self.txt1= tkinter.Entry(width=10)
        self.txt1.place(x=10, y=30)
        self.txt1.insert(tkinter.END,"data1")

        self.txt2= tkinter.Entry(width=10)
        self.txt2.place(x=10, y=50)
        self.txt2.insert(tkinter.END,"data2")

        self.txt3= tkinter.Entry(width=10)
        self.txt3.place(x=10, y=70)
        self.txt3.insert(tkinter.END,"data3")


        button5= tk.Button(root, text=u'jpgファイル選択', command=self.button5_clicked)  
        button5.pack() 
        button5.place(x=300, y=55) 

        button6= tk.Button(root, text=u'jpg読み出し', command=self.read_jpg)  
        button6.pack() 
        button6.place(x=400, y=55) 
        self.dir = 0


    def dbwrite(self):
     dbname = '../personbase3.db'
     #DBコネクト​
     with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),data4 img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #データインサート​
        sql = 'insert into users (data1, data2, data3,data4) values (?,?,?,?)'
        user = (self.data1, self.data2, self.data3,self.data4)
        c.execute(sql, user)
        conn.commit()


        self.textExample.insert(tkinter.END,"\n")
        self.textExample.insert(tkinter.END,"DB書き込みしました")


    def dbclear(self):
     dbname = '../personbase3.db'
     #DBコネクト​
     with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),data4 img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #データインサート​
        sql = 'delete from users'
        #user = (1, self.data1, self.data2, self.data3)
        c.execute(sql)
        conn.commit()

        self.textExample.insert(tkinter.END,"\n")
        self.textExample.insert(tkinter.END,"DB消去しました")

    def dbread(self):
     wf = 'C:\\github\\tkinter_sqlite3_mini\\write.jpg' #書き込み画像ファイルパス
  
  
     dbname = '../personbase3.db'
     #DBコネクト​
     with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),data4 img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        select = 'select * from users'
        self.textExample.delete("1.0",tkinter.END)

        for row in c.execute(select):
            print(row)


        for row in c.execute('select id ,data1 ,data2, data3 from users'):
            blob = row[0]
            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,row)

        for row in c.execute('select data4 from users'):
            blob = row[0]
        #バイナリ出力
        with open(wf, 'wb') as f:
            f.write(blob)
            
    def dbread(self):
     wf = 'C:\\github\\tkinter_sqlite3_mini\\write.jpg' #書き込み画像ファイルパス
  
  
     dbname = '../personbase3.db'
     #DBコネクト​
     with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),data4 img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        self.textExample.delete("1.0",tkinter.END)



        for row in c.execute('select id ,data1 ,data2, data3 from users'):
            blob = row[0]
            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,row)


    def jpgread(self):
     wf = 'C:\\github\\tkinter_sqlite3_mini\\write.jpg' #書き込み画像ファイルパス
  
  
     dbname = '../personbase3.db'
     #DBコネクト​
     with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),data4 img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        select = 'select * from users'
        self.textExample.delete("1.0",tkinter.END)

        for row in c.execute('select data4 from users'):
            blob = row[0]
        #バイナリ出力
        with open(wf, 'wb') as f:
            f.write(blob)

        self.select_one_image(wf)


    def write_db(self):
        global filenames

        if(self.dir==0):
            self.textExample.insert(tkinter.END,"jpgが未指定\n")
            return

        for file in self.filenames:
            file_c = file.replace('\\', '\\\\');
            print(file_c)


        
        self.data1 =self.txt1.get()
        self.data2 =self.txt2.get()
        self.data3 =self.txt3.get()
        with open(file_c, 'rb') as f:
            self.data4 = f.read()

        self.dbwrite()
 
            
    def read_db(self):
        self.dbread()

    def read_jpg(self):
        self.jpgread()



    def clear_db(self):
        self.dbclear()


    def text_clear(self):
        self.textExample.delete("1.0",tkinter.END)


    def select_one_image(self,n):

        img2 = Image.open(n)
        x = 300
        y = 300
        img2.thumbnail((x, y), Image.ANTIALIAS)

        img2 = ImageTk.PhotoImage(img2)

        canvas = tkinter.Canvas(width=600, height=500)
        canvas.place(x=0, y=0)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        canvas.itemconfig(item,image=img2)
        root.mainloop()




    def button5_clicked(self):  
        global filenames


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        print(filenames)
        self.filenames=filenames
        self.dir = 1

#=================================================
# main function
#=================================================
if __name__  == '__main__':
    root = tk.Tk()
    mw = main_window(root)
    root.geometry("640x380")  
    root.mainloop();

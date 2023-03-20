#!/usr/bin/python3
from tkinter.scrolledtext import ScrolledText
import tkinter
import tkinter as tk
import tkinter.simpledialog as sd
import sqlite3
from contextlib import closing
import sys
class main_window(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(master,text="sqlite3 mini test")
        self.label.pack()
        
        button1 = tk.Button(root, text = 'DB書き込み', command=self.suspend)
        button1.pack(side="left") 
        
        self.textExample=ScrolledText(root, height=10,width=60, wrap=tkinter.CHAR)
        self.textExample.pack()
        self.textExample.place(x=150, y=70)
        
        self.txt1= tkinter.Entry(width=10)
        self.txt1.place(x=10, y=30)
        self.txt1.insert(tkinter.END,"data1")

        self.txt2= tkinter.Entry(width=10)
        self.txt2.place(x=110, y=30)
        self.txt2.insert(tkinter.END,"data2")

        self.txt3= tkinter.Entry(width=10)
        self.txt3.place(x=210, y=30)
        self.txt3.insert(tkinter.END,"data3")

    def dbwrite(self):
     dbname = '../personbase2.db'
     #DBコネクト​
     with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id int, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64))'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #データインサート​
        sql = 'insert into users (id, data1, data2, data3) values (?,?,?,?)'
        user = (1, self.data1, self.data2, self.data3)
        c.execute(sql, user)
        conn.commit()
        #表示​
        select = 'select * from users'
        self.textExample.delete("1.0",tkinter.END)

        for row in c.execute(select):
            print(row)

            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,row)
            
    def suspend(self):
        self.data1 =self.txt1.get()
        self.data2 =self.txt2.get()
        self.data3 =self.txt3.get()
        self.dbwrite()
            
#=================================================
# main function
#=================================================
if __name__  == '__main__':
    root = tk.Tk()
    mw = main_window(root)
    root.geometry("640x280")  
    root.mainloop();

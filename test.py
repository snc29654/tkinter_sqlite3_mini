#!/usr/bin/python3
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
        self.button = tk.Button(master, text="Input String", fg="red",
                                command=self.askstr)
        self.button.pack(side="left")
    def set(self, str):
        self.label.config(text=str)
    def askstr(self):
        data=sd.askstring("test askstring", "input", initialvalue="initial data")
        self.set(data)
        self.dbwrite(data)
    def dbwrite(self,str):
     dbname = 'personbase.db'
     #DBコネクト​
     with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id int, name varchar(64),
                      age int, gender varchar(32))'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #データインサート​
        sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
        user = (1, str, 20, 'male')
        c.execute(sql, user)
        conn.commit()
        #表示​
        select = 'select * from users'
        for row in c.execute(select):
            print(row)
#=================================================
# main function
#=================================================
if __name__  == '__main__':
    root = tk.Tk()
    mw = main_window(root)
    root.mainloop();

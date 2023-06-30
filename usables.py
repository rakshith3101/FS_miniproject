from tkinter import *
from tkinter import ttk

def ok():
    pass

def example():
    file=open('example.txt','r')
    file_content=file.read()
    print(file_content)
    file.close()
def click():
    file_path="for_women/education.txt"
    r=open(file_path,'r')
    r_content=r.read()
    window2=Tk()
    window2.title("window two")
    window2.geometry("500x500")
    text_widget=Text(window2,height=500,width=500,bg="#aaff00")
    text_widget.pack()
    text_widget.insert(END,r_content)
    window2.mainloop()
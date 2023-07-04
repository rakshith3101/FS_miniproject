from tkinter import *
from tkinter import ttk
import os
bckgnd_clr="#f7ffe6"
def education_def(option):
    directory="education"
    ext="txt"
    file_path=os.path.join(directory,f"{option}.{ext}")
    r=open(file_path,'r')
    r_content=r.read()
    window2=Tk()
    window2.title(option)
    window2.geometry("500x500")
    text_widget=Text(window2,height=500,width=500,bg=bckgnd_clr)
    text_widget.pack()
    text_widget.insert(END,r_content)
    window2.mainloop()
    
def agriculture(option):
    directory="agriculture"
    ext="txt"
    file_path=os.path.join(directory,f"{option}.{ext}")
    r=open(file_path,'r')
    r_content=r.read()
    window2=Tk()
    window2.title(option)
    window2.geometry("500x500")
    text_widget=Text(window2,height=500,width=500,bg=bckgnd_clr)
    text_widget.pack()
    text_widget.insert(END,r_content)
    window2.mainloop()
def small_scale(option):
    directory="small_scale_industry"
    ext="txt"
    file_path=os.path.join(directory,f"{option}.{ext}")
    r=open(file_path,'r')
    r_content=r.read()
    window2=Tk()
    window2.title(option)
    window2.geometry("500x500")
    text_widget=Text(window2,height=500,width=500,bg=bckgnd_clr)
    text_widget.pack()
    text_widget.insert(END,r_content)
    window2.mainloop()
def for_women(option):
    directory="for_women"
    ext="txt"
    file_path=os.path.join(directory,f"{option}.{ext}")
    r=open(file_path,'r')
    r_content=r.read()
    window2=Tk()
    window2.title(option)
    window2.geometry("500x500")
    text_widget=Text(window2,height=500,width=500,bg=bckgnd_clr)
    text_widget.pack()
    text_widget.insert(END,r_content)
    window2.mainloop()
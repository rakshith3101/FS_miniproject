from tkinter import *
from tkinter import ttk
c1='#f7ffe6'
c2='#aaff00'
# main window
window=Tk()
window.title("Krishi")
window.geometry('500x500')
window.config(background=c1)
window.resizable(width=True,height=True)
#frame_up=Frame(window,width=500,height=50,bg=c2)
#frame_up.grid(row=2,column=2,pady=1,padx=0)

#frame_down=Frame(window,width=500,height=500,bg='#000000')
#frame_down.grid(row=2,column=2,padx=0,pady=1)


#inner frame title
frame_label=Label(window,text="KRISHI",height=1,font=('Verdan 20 bold'),fg='#000000',bg=c2)
frame_label.place(x=200,y=5)


# type scheme selection
scheme=Label(window,text='SELECT SCHEME',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=18,y=10)
scheme.place(y=40)
OPTIONS = [
"LOANS",
"RURAL_WOMEN_WELFARE",
"CROPS AND FERTILIZERS",
"BASIC NEEDS"
] 
variable = StringVar()
variable.set(OPTIONS[0]) # default value
w = OptionMenu(window, variable, *OPTIONS)
w.pack()
w.place(x=20,y=10)
w.place(y=63)

def ok():
    print ("value is:" + variable.get())
button = Button(window, text="SELECT", command=ok)
button.pack()
button.place(x=20,y=10)
button.place(y=87)


#regional scheme
scheme=Label(window,text='SELECT REGION',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=375,y=10)
scheme.place(y=40)

regions=["STATE","CENTRAL"]
variable1=StringVar()
variable1.set(regions[0])
r=OptionMenu(window,variable1,*regions)#option menu for region selection
r.pack()
r.place(x=380,y=10)
r.place(y=63)

button2=Button(window,text='SELECT',command=ok)#button for scheme
button2.pack()
button2.place(x=380,y=10)
button2.place(y=87)
window.mainloop()

# from tkinter import *
from tkinter import ttk
from usables import *
c1='#f7ffe6'
c2='#aaff00'
# main window
window=Tk()
window.title("Scheme Hub")
window.geometry('450x450')
window.config(background="#213300")
window.resizable(width=True,height=True)

#main window
frame=Frame(window,width=500,height=300,bg=c1)
frame.pack()
#inner frame title
frame_label=Label(window,text="SCHEAM HUB",height=1,font=('Verdan 20 bold'),fg='#000000',bg=c1)
frame_label.place(x=130,y=5)

#AGRICULTURE SCHEME
scheme=Label(window,text='AGRICULTURE',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=290,y=10)
scheme.place(y=60)
AGRICULTURE = [
"LOANS",
"RURAL_WOMEN_WELFARE",
"CROPS AND FERTILIZERS",
"BASIC NEEDS"
] 
variable = StringVar()
variable.set(AGRICULTURE[0]) # default value
w = OptionMenu(window, variable, *AGRICULTURE)
w.pack()
w.place(x=310,y=10)
w.place(y=87)
button = Button(window, text="SELECT", command=lambda:agriculture(variable.get()))
button.pack()
button.place(x=320,y=10)
button.place(y=120)


#EDUCATION SCHEME
scheme2=Label(window,text='EDUCATION',height=1,font=('Verdan 12 '),fg='#000000')
scheme2.place(x=310,y=10)
scheme2.place(y=160)

education=[
"SCHOLARSHIP",
"FACILITIES",
"OTHERS"
]
variable1 = StringVar()
variable1.set(education[0])
r=OptionMenu(window,variable1,*education)#option menu for region selection
r.pack()
r.place(x=295,y=10)
r.place(y=190)

button2=Button(window,text='SELECT',command=lambda:education_def(variable1.get()),width=5,height=1)#button for scheme
button2.pack()
button2.place(x=330,y=10)
button2.place(y=220)

#SMALL-SCALE INDUSTRY
scheme=Label(window,text='INDUSTRY',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=40,y=10)
scheme.place(y=160)
SMALL_SCALE_INDUSTRY = [
"ESTABLISHMENT",
"MACHINERY",
"MENTORSHIP",
"INDUSTIAL LOAN",
"MARKING AND SUPPLY CHAIN"
] 
variable3 = StringVar()
variable3.set(SMALL_SCALE_INDUSTRY[0]) # default value
s = OptionMenu(window, variable3, *SMALL_SCALE_INDUSTRY)
s.pack()
s.place(x=20,y=10)
s.place(y=190)
button3 = Button(window, text="SELECT", command=lambda:small_scale(variable3.get()))
button3.pack()
button3.place(x=50,y=10)
button3.place(y=220)


#WOMEN RELATED SCHEMES
scheme=Label(window,text='WOMEN',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=40,y=10)
scheme.place(y=60)
FOR_WOMEN = [
"EDUCATION",
"BASIC FACILITY",
"LOAN AND HOUSEHOLD",
"OTHERS"
] 
variable5 = StringVar()
variable5.set(FOR_WOMEN[0]) # default value
f = OptionMenu(window, variable5, *FOR_WOMEN)
f.pack()
f.place(x=20,y=10)
f.place(y=87)
button5 = Button(window, text="SELECT", command=lambda:for_women(variable5.get()))
button5.pack()
button5.place(x=50,y=10)
button5.place(y=120)
##search scheme
def search_schemes():
    keyword = entry.get()  # Get the keyword entered in the Entry widget
    keyword = keyword.lower()  # Convert the keyword to lowercase for case-insensitive search
    results = []

    with open('government_schemes.txt', 'r') as file:
        for line in file:
            scheme, description, url = line.strip().split('|')
            if keyword in scheme.lower() or keyword in description.lower() or keyword in url:
                results.append((scheme, description,url))

    display_results(results)

def display_results(results):
    result_text.delete('1.0',END)  # Clear previous results

    if results:
        for scheme, description,url in results:
            result_text.insert(END, f'Scheme: {scheme}\n')
            result_text.insert(END, f'Description: {description}\n\n')
            result_text.insert(END,f'Website Link:{url}\n\n\n')
    else:
        result_text.insert(END, 'No matching schemes found.')
def exam():
    print("hello")

label = ttk.Label(window, text='Enter the Scheme Name:')
label.pack()

entry = ttk.Entry(window)
entry.pack()

search_button = ttk.Button(window, text='Search', command=search_schemes)
search_button.pack()

result_text =Text(window, height=10, width=50)
result_text.pack()

window.mainloop()
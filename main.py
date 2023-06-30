from tkinter import *
from tkinter import ttk
from usables import *
c1='#f7ffe6'
c2='#aaff00'
# main window
window=Tk()
window.title("Krishi")
window.geometry('500x500')
window.config(background=c1)
window.resizable(width=True,height=True)

#main window
frame=Frame(window,width=500,height=300,bg=c1)
frame.pack()
#inner frame title
frame_label=Label(window,text="KRISHI",height=1,font=('Verdan 20 bold'),fg='#000000',bg=c2)
frame_label.place(x=200,y=5)

#AGRICULTURE SCHEME
scheme=Label(frame,text='SELECT SCHEME',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=18,y=10)
scheme.place(y=40)
AGRICULTURE = [
"LOANS",
"RURAL_WOMEN_WELFARE",
"CROPS AND FERTILIZERS",
"BASIC NEEDS"
] 
variable = StringVar()
variable.set(AGRICULTURE[0]) # default value
w = OptionMenu(frame, variable, *AGRICULTURE)
w.pack()
w.place(x=20,y=10)
w.place(y=63)
button = Button(frame, text="SELECT", command=ok)
button.pack()
button.place(x=20,y=10)
button.place(y=87)

#EDUCATION SCHEME
scheme2=Label(frame,text='SELECT REGION',height=1,font=('Verdan 12 '),fg='#000000')
scheme2.place(x=375,y=10)
scheme2.place(y=40)

education=[
"SCHOLARSHIP",
"FACILITIES",
"OTHERS"
]
variable1 = StringVar()
variable1.set(education[0])
r=OptionMenu(frame,variable1,*education)#option menu for region selection
r.pack()
r.place(x=380,y=10)
r.place(y=63)

button2=Button(frame,text='SELECT',command=click,width=5,height=1)#button for scheme
button2.pack()
button2.place(x=380,y=10)
button2.place(y=87)

#SMALL-SCALE INDUSTRY
scheme=Label(frame,text='SELECT SCHEME',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=18,y=10)
scheme.place(y=40)
SMALL_SCALE_INDUSTRY = [
"ESTABLISHMENT",
"MACHINERY",
"MENTORSHIP",
"INDUSTIAL LOAN",
"MARKING AND SUPPLY CHAIN"
] 
variable3 = StringVar()
variable3.set(SMALL_SCALE_INDUSTRY[0]) # default value
s = OptionMenu(frame, variable3, *SMALL_SCALE_INDUSTRY)
s.pack()
s.place(x=20,y=10)
s.place(y=100)
button3 = Button(frame, text="SELECT", command=ok)
button3.pack()
button3.place(x=20,y=10)
button3.place(y=110)

#BANKING SCHEME
scheme=Label(frame,text='SELECT SCHEME',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=18,y=10)
scheme.place(y=40)
BANKING = [
"BANKING LOANS",
"STUDENT FACILITY",
"FACILITIES FOR WOMEN",
"BASIC FACILITIES"
] 
variable4 = StringVar()
variable4.set(BANKING[0]) # default value
b = OptionMenu(frame, variable4, *BANKING)
b.pack()
b.place(x=20,y=10)
b.place(y=150)
button4 = Button(frame, text="SELECT", command=ok)
button4.pack()
button4.place(x=20,y=10)
button4.place(y=150)

#WOMEN RELATED SCHEMES
scheme=Label(frame,text='SELECT SCHEME',height=1,font=('Verdan 12 '),fg='#000000')
scheme.place(x=18,y=10)
scheme.place(y=40)
FOR_WOMEN = [
"EDUCATION",
"BASIC FACILITY",
"LOAN AND HOUSEHOLD",
"OTHERS"
] 
variable5 = StringVar()
variable5.set(FOR_WOMEN[0]) # default value
f = OptionMenu(frame, variable5, *FOR_WOMEN)
f.pack()
f.place(x=20,y=10)
f.place(y=63)
button5 = Button(frame, text="SELECT", command=ok)
button5.pack()
button5.place(x=20,y=10)
button5.place(y=87)
##search scheme

def search_schemes():
    keyword = entry.get()  # Get the keyword entered in the Entry widget
    keyword = keyword.lower()  # Convert the keyword to lowercase for case-insensitive search
    results = []

    with open('government_schemes.txt', 'r') as file:
        for line in file:
            scheme, description = line.strip().split('|')
            if keyword in scheme.lower() or keyword in description.lower():
                results.append((scheme, description))

    display_results(results)

def display_results(results):
    result_text.delete('1.0',END)  # Clear previous results

    if results:
        for scheme, description in results:
            result_text.insert(END, f'Scheme: {scheme}\n')
            result_text.insert(END, f'Description: {description}\n\n')
    else:
        result_text.insert(END, 'No matching schemes found.')
def exam():
    print("hello")

label = ttk.Label(window, text='Enter a keyword to search:')
label.pack()

entry = ttk.Entry(window)
entry.pack()

search_button = ttk.Button(window, text='Search', command=search_schemes)
search_button.pack()

result_text =Text(window, height=10, width=50)
result_text.pack()


window.mainloop()
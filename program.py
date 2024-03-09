from tkinter import *
from tkinter import ttk
import tkinter as tk



from googletrans import LANGUAGES,Translator

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data_get():
    s=comb_sor.get()
    d=comb_dest.get()
    msg=Sor_txt.get(1.0,END)
    text_get=change(msg,s,d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,text_get)


















root= tk.Tk()
root.title("Language Translator")
root.geometry("500x700")
root.config(bg='#BABAD3')

lab_txt=Label(root,text="Translator",font=("Time New Roman",40),bg="#BABAD3")
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root,bd=5,relief=tk.SOLID).pack(side=BOTTOM)


lab_txt=Label(root,text="Source",font=("Time New Roman",20),fg="black",bg="#BABAD3")
lab_txt.place(x=-90,y=120,height=40,width=300)

Sor_txt=Text(frame,font=("Time New Roman",10),wrap=WORD)
Sor_txt.place(x=10,y=160,height=100,width=480)



list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=370,y=130,height=20,width=120)
comb_sor.set("english")

def on_enter(event):
    button_change.config(bg="pink") 

def on_leave(event):
    button_change.config(bg="SystemButtonFace")

button_change=Button(frame,text="translate",relief=tk.SOLID,command=data_get,)
button_change.place(x=180,y=280,height=40,width=140)
button_change.bind("<Enter>",on_enter)
button_change.bind("<Leave>",on_leave)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=370,y=410,height=20,width=120)
comb_dest.set("hindi")

dest_txt=Label(root,text="Translation",font=("Time New Roman",20),fg="black",bg="#BABAD3")
dest_txt.place(x=-70,y=400,height=40,width=290)

dest_txt=Text(frame,font=("Time New Roman",10),wrap=WORD)
dest_txt.place(x=10,y=440,height=100,width=480)

def on_enter(event):
    button_speech.config(bg="pink") 

def on_leave(event):
    button_speech.config(bg="SystemButtonFace")

button_speech=Button(frame,text="Speak to Enter",relief=tk.SOLID)
button_speech.place(x=180,y=580,height=40,width=140)
button_speech.bind("<Enter>",on_enter)
button_speech.bind("<Leave>",on_leave)



root.mainloop()

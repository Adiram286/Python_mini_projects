from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD,ITALIC
import PIL.ImageTk as imtk
import PIL.Image as i
import random

win=Tk()
win.title("Guess the Number")
win.configure(background="black")
win.geometry("950x650+0+0")

bgimg=imtk.PhotoImage(file="2.png")
label1=Label(win,image=bgimg)
label1.place(x=0,y=0)

welcome_msg=Label(win,text=" Welcome to Rock, Paper, Scissor Game !!!",font=("Calibri",35,ITALIC,BOLD),bg="#7f1734")
welcome_msg.place(x=40,y=0)

global urs
urs=''

def r():
    global urs
    urs="Rock"
    l=["Rock","Paper","Scissor"]
    cs=random.choice(l)
    
    frame=Frame(win,width=950,height=650)
    frame.configure(background="black")
    frame.place(x=0,y=0)

    bgimg2=imtk.PhotoImage(file="2.png")
    label2=Label(frame,image=bgimg)
    label2.place(x=0,y=0)

    ys=Label(frame,text="Your Selection",font=("Times New Roman",30,ITALIC,BOLD),bg="#F1C40F")
    ys.place(x=60,y=10)
    csl=Label(frame,text="Computer Selection",font=("Times New Roman",30,ITALIC,BOLD),bg="#F1C40F")
    csl.place(x=470,y=10)

    ursi=urs+".png"
    csi=cs+".png"
    global ursi2
    ursi2=PhotoImage(file=ursi)
    ursi2l=Label(frame,image=ursi2)
    ursi2l.place(x=60,y=80)
    global csi2
    csi2=PhotoImage(file=csi)
    csi2l=Label(frame,image=csi2)
    csi2l.place(x=525,y=80)
    
    if urs==cs:
        msg=Label(frame,text=" It's an Draw !!",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=300,y=400)
    elif cs=="Paper":
        msg=Label(frame,text=" Oops! You lose !! \n you selected Rock and system selected Paper.",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=75,y=400)
    elif cs=="Scissor":
        msg=Label(frame,text=" Congrats, You win !! \n You selected Rock and system selected Scissor.",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=75,y=400)

    def des():
        frame.destroy()

    ag=Button(frame,text="Play Again !!!",font=("Times New Roman",30,ITALIC,BOLD),bg="#34495E",command=des)
    ag.place(x=300,y=525)

global aa
aa=PhotoImage(file="Rock.png")
al=Label(win,image=aa)
zero=Button(win,image=aa,command=r)
zero.place(x=40,y=150)

def p():
    global urs
    urs="Paper"
    l=["Rock","Paper","Scissor"]
    cs=random.choice(l)
    
    frame=Frame(win,width=950,height=650)
    frame.configure(background="black")
    frame.place(x=0,y=0)

    bgimg2=imtk.PhotoImage(file="2.png")
    label2=Label(frame,image=bgimg)
    label2.place(x=0,y=0)

    ys=Label(frame,text="Your Selection",font=("Times New Roman",30,ITALIC,BOLD),bg="#F1C40F")
    ys.place(x=60,y=10)
    csl=Label(frame,text="Computer Selection",font=("Times New Roman",30,ITALIC,BOLD),bg="#F1C40F")
    csl.place(x=470,y=10)

    ursi=urs+".png"
    csi=cs+".png"
    global ursi2
    ursi2=PhotoImage(file=ursi)
    ursi2l=Label(frame,image=ursi2)
    ursi2l.place(x=60,y=80)
    global csi2
    csi2=PhotoImage(file=csi)
    csi2l=Label(frame,image=csi2)
    csi2l.place(x=525,y=80)
    
    if urs==cs:
        msg=Label(frame,text=" It's an Draw !!",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=300,y=400)
    elif cs=="Scissor":
        msg=Label(frame,text=" Oops! You lose !! \n you selected Paper and system selected Scissor.",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=75,y=400)
    elif cs=="Rock":
        msg=Label(frame,text=" Congrats, You win !! \n You selected Paper and system selected Rock.",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=75,y=400)

    def des():
        frame.destroy()

    ag=Button(frame,text="Play Again !!!",font=("Times New Roman",30,ITALIC,BOLD),bg="#34495E",command=des)
    ag.place(x=300,y=525)
    
global bb
bb=PhotoImage(file="Paper.png")
al=Label(win,image=bb)
one=Button(win,image=bb,command=p)
one.place(x=340,y=150)

def s():
    global urs
    urs="Scissor"
    l=["Rock","Paper","Scissor"]
    cs=random.choice(l)
    
    frame=Frame(win,width=950,height=650)
    frame.configure(background="black")
    frame.place(x=0,y=0)

    bgimg2=imtk.PhotoImage(file="2.png")
    label2=Label(frame,image=bgimg)
    label2.place(x=0,y=0)

    ys=Label(frame,text="Your Selection",font=("Times New Roman",30,ITALIC,BOLD),bg="#F1C40F")
    ys.place(x=60,y=10)
    csl=Label(frame,text="Computer Selection",font=("Times New Roman",30,ITALIC,BOLD),bg="#F1C40F")
    csl.place(x=470,y=10)

    ursi=urs+".png"
    csi=cs+".png"
    global ursi2
    ursi2=PhotoImage(file=ursi)
    ursi2l=Label(frame,image=ursi2)
    ursi2l.place(x=60,y=80)
    global csi2
    csi2=PhotoImage(file=csi)
    csi2l=Label(frame,image=csi2)
    csi2l.place(x=525,y=80)
    
    if urs==cs:
        msg=Label(frame,text=" It's an Draw !!",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=300,y=400)
    elif cs=="Rock":
        msg=Label(frame,text=" Oops! You lose !! \n you selected Scissor and system selected Rock.",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=75,y=400)
    elif cs=="Paper":
        msg=Label(frame,text=" Congrats, You win !! \n You selected Scissor and system selected Paper.",font=("Times New Roman",30,ITALIC,BOLD),bg="#D35400")
        msg.place(x=75,y=400)

    def des():
        frame.destroy()

    ag=Button(frame,text="Play Again !!!",font=("Times New Roman",30,ITALIC,BOLD),bg="#34495E",command=des)
    ag.place(x=300,y=525)
    
global cc
cc=PhotoImage(file="Scissor.png")
al=Label(win,image=cc)
two=Button(win,image=cc,command=s)
two.place(x=640,y=150)

win.mainloop()




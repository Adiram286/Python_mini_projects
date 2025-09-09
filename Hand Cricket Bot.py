from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD,ITALIC
import PIL.ImageTk as imtk
import PIL.Image as i
import random


win=Tk()
win.title("SunBucks Cafe")
win.attributes("-fullscreen",True)
win.configure(background="black")


bgimg=imtk.PhotoImage(file="1.png")
label1=Label(win,image=bgimg)
label1.place(x=0,y=0)


welcome_msg=Label(win,text=" Welcome to Hand Cricket Simulator!!!",font=("Calibri",35,ITALIC,BOLD),bg="#7f1734")
welcome_msg.place(x=375,y=0)


over=Label(win,text="Enter No.of Overs :",font=("Times New Roman",30,ITALIC,BOLD),bg="#ffcc33")
over.place(x=350,y=105)
over_entry=Entry(win,width=25,font=("Calibri",30,BOLD))
over_entry.place(x=700,y=105)

toss_msg=Label(win,text="Select Head OR Tiles :",font=("Times New Roman",30,ITALIC,BOLD),bg="#ffcc33")
toss_msg.place(x=300,y=255)
toss_entry=ttk.Combobox(win,width=10,font=("Times New Roman",30,BOLD,ITALIC),values=("Heads","Tiles"))
toss_entry.place(x=700,y=255)

def toss():
    a=(toss_entry.get())
    
    t=["Heads","Tiles"]
    tr=random.choice(t)
    if a==tr:
        toss_button.place_forget()
        
        toss_result=Label(win,text="You Won the toss, Select to Bat or Bowl !!!",font=("Times New Roman",30,ITALIC,BOLD),bg="#2DE508")
        toss_result.place(x=250,y=350)

        toss_selection=ttk.Combobox(win,width=10,font=("Times New Roman",30,BOLD,ITALIC),values=("Bat","Bowl"))
        toss_selection.place(x=600,y=450)
                             
        def get_over():
            a=int((over_entry.get()))
            global ba
            ba=a*6
            tsr=(toss_selection.get())

            toss_msg.place_forget()
            toss_entry.place_forget()
            toss_result.place_forget()
            toss_selection.place_forget()
            welcome_msg.place_forget()
            over.place_forget()
            over_entry.place_forget()
            start_button.place_forget()
            
            frame = Frame(win, width=400, height=200)
            frame.place(x=20,y=10)
            frame.configure(background="black")
            
            run_count=Label(frame,text="Your Score :",font=("Times New Roman",30,ITALIC,BOLD),bg="#FAD100")
            run_count.place(x=5,y=5)
            global rc
            rc=0
            
            com_score=Label(frame,text="System Score :",font=("Times New Roman",30,ITALIC,BOLD),bg="#FAD100")
            com_score.place(x=5,y=60)
            cs=0

            if tsr=="Bat":
                urs=Label(win,text="Your Selection:",font=("Times New Roman",25,ITALIC,BOLD),bg="#FAD100")
                urs.place(x=500,y=40)

                cs=Label(win,text="Computer Selection:",font=("Times New Roman",25,ITALIC,BOLD),bg="#FAD100")
                cs.place(x=900,y=40)

                frame2 = Frame(win, width=400, height=200)
                frame2.place(x=600,y=400)
                frame2.configure(background="black")

                
                def zo():
                    cn=random.randrange(0,7)
                    un=0
                    global rc
                    rc+=0
                    rcl=Label(frame,text=rc,font=("Times New Roman",40,ITALIC,BOLD),bg="#FC7701")
                    rcl.place(x=300,y=5)
                    unl=Label(win,text="0",font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    unl.place(x=520,y=100)
                    cnl=Label(win,text=cn,font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    cnl.place(x=920,y=100)
                    if cn==un:
                        frame3= Frame(win,width=1920,height=1080)
                        frame3.place(x=0,y=0)
                        global bgimg2
                        bgimg2=imtk.PhotoImage(file="1.png")
                        label1=Label(frame3,image=bgimg2)
                        label1.place(x=0,y=0)
                        
                global aa
                aa=PhotoImage(file="img0.png")
                al=Label(frame2,image=aa)
                zero=Button(frame2,image=aa,command=zo)
                zero.place(x=0,y=0)


                def oo():
                    cn=random.randrange(0,7)
                    un=0
                    global rc
                    rc+=1
                    rcl=Label(frame,text=rc,font=("Times New Roman",40,ITALIC,BOLD),bg="#FC7701")
                    rcl.place(x=300,y=5)
                    unl=Label(win,text="1",font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    unl.place(x=520,y=100)
                    cnl=Label(win,text=cn,font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    cnl.place(x=920,y=100)
                    if cn==un:
                        frame3= Frame(win,width=1920,height=1080)
                        frame3.place(x=0,y=0)
                        global bgimg2
                        bgimg2=imtk.PhotoImage(file="1.png")
                        label1=Label(frame3,image=bgimg2)
                        label1.place(x=0,y=0)
                global bb
                bb=PhotoImage(file="img1.png")
                bl=Label(frame2,image=bb)
                one=Button(frame2,image=bb,command=oo)
                one.place(x=70,y=0)


                def to():
                    cn=random.randrange(0,7)
                    un=0
                    global rc
                    rc+=2
                    rcl=Label(frame,text=rc,font=("Times New Roman",40,ITALIC,BOLD),bg="#FC7701")
                    rcl.place(x=300,y=5)
                    unl=Label(win,text="2",font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    unl.place(x=520,y=100)
                    cnl=Label(win,text=cn,font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    cnl.place(x=920,y=100)
                    if cn==un:
                        frame3= Frame(win,width=1920,height=1080)
                        frame3.place(x=0,y=0)
                        global bgimg2
                        bgimg2=imtk.PhotoImage(file="1.png")
                        label1=Label(frame3,image=bgimg2)
                        label1.place(x=0,y=0)
                global cc
                cc=PhotoImage(file="img2.png")
                cl=Label(frame2,image=cc)
                two=Button(frame2,image=cc,command=to)
                two.place(x=140,y=0)


                def tto():
                    cn=random.randrange(0,7)
                    un=0
                    global rc
                    rc+=3
                    rcl=Label(frame,text=rc,font=("Times New Roman",40,ITALIC,BOLD),bg="#FC7701")
                    rcl.place(x=300,y=5)
                    unl=Label(win,text="3",font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    unl.place(x=520,y=100)
                    cnl=Label(win,text=cn,font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    cnl.place(x=920,y=100)
                    if cn==un:
                        frame3= Frame(win,width=1920,height=1080)
                        frame3.place(x=0,y=0)
                        global bgimg2
                        bgimg2=imtk.PhotoImage(file="1.png")
                        label1=Label(frame3,image=bgimg2)
                        label1.place(x=0,y=0)
                global dd
                dd=PhotoImage(file="img3.png")
                dl=Label(frame2,image=dd)
                three=Button(frame2,image=dd,command=tto)
                three.place(x=0,y=70)


                def fo():
                    cn=random.randrange(0,7)
                    un=0
                    global rc
                    rc+=4
                    rcl=Label(frame,text=rc,font=("Times New Roman",40,ITALIC,BOLD),bg="#FC7701")
                    rcl.place(x=300,y=5)
                    unl=Label(win,text="4",font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    unl.place(x=520,y=100)
                    cnl=Label(win,text=cn,font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    cnl.place(x=920,y=100)
                    if cn==un:
                        frame3= Frame(win,width=1920,height=1080)
                        frame3.place(x=0,y=0)
                        global bgimg2
                        bgimg2=imtk.PhotoImage(file="1.png")
                        label1=Label(frame3,image=bgimg2)
                        label1.place(x=0,y=0)
                global ee
                ee=PhotoImage(file="img4.png")
                el=Label(frame2,image=ee)
                four=Button(frame2,image=ee,command=ee)
                four.place(x=70,y=70)

                def go():
                    cn=random.randrange(0,7)
                    un=0
                    global rc
                    rc+=6
                    rcl=Label(frame,text=rc,font=("Times New Roman",40,ITALIC,BOLD),bg="#FC7701")
                    rcl.place(x=300,y=5)
                    unl=Label(win,text="6",font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    unl.place(x=520,y=100)
                    cnl=Label(win,text=cn,font=("Times New Roman",50,ITALIC,BOLD),bg="#FC7701")
                    cnl.place(x=920,y=100)
                    if cn==un:
                        frame3= Frame(win,width=1920,height=1080)
                        frame3.place(x=0,y=0)
                        global bgimg2
                        bgimg2=imtk.PhotoImage(file="1.png")
                        label1=Label(frame3,image=bgimg2)
                        label1.place(x=0,y=0)
                global gg 
                gg=PhotoImage(file="img6.png")
                gl=Label(frame2,image=gg)
                six=Button(frame2,image=gg,command=go)
                six.place(x=210,y=70)

            
        start_button=Button(win,text="Start",font=("Times New Roman",25,BOLD),bg="#F10F0F",command=get_over)
        start_button.place(x=675,y=550)

        
    else:
        toss_button.place_forget()
        
        toss_result=Label(win,text="You lost the toss, Bowl first !!!",font=("Times New Roman",30,ITALIC,BOLD),bg="#2DE508")
        toss_result.place(x=250,y=350)
        
        def get_over():
            a=int((over_entry.get()))

            toss_msg.place_forget()
            toss_entry.place_forget()
            toss_result.place_forget()
            welcome_msg.place_forget()
            over.place_forget()
            over_entry.place_forget()
            start_button.place_forget()
            
            frame = Frame(win, width=400, height=200)
            frame.place(x=20,y=10)
            frame.configure(background="black")
            
            run_count=Label(frame,text="Your Score :",font=("Times New Roman",30,ITALIC,BOLD),bg="#FAD100")
            run_count.place(x=5,y=5)
            rc=0
            
            com_score=Label(frame,text="System Score :",font=("Times New Roman",30,ITALIC,BOLD),bg="#FAD100")
            com_score.place(x=5,y=60)
            cs=0

            urs=Label(win,text="Your Selection:",font=("Times New Roman",25,ITALIC,BOLD),bg="#FAD100")
            urs.place(x=500,y=40)

            cs=Label(win,text="Computer Selection:",font=("Times New Roman",25,ITALIC,BOLD),bg="#FAD100")
            cs.place(x=900,y=40)
            
        start_button=Button(win,text="Start",font=("Times New Roman",25,BOLD),bg="#F10F0F",command=get_over)
        start_button.place(x=675,y=750)


    

toss_button=Button(win,text="Toss",font=("Times New Roman",25,BOLD),bg="#F10F0F",command=toss)
toss_button.place(x=675,y=525)

win.mainloop()
    







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

bgimg=imtk.PhotoImage(file="1.png")
label1=Label(win,image=bgimg)
label1.place(x=3,y=3)


system_name_label=Label(win,text="Guess the Number",font=("Calibri",43,BOLD),bg="#800000")
system_name_label.place(x=250,y=0)


input_range=Label(win,text="Enter range of numbers(from 0 to):",font=("Times New Roman",25,ITALIC,BOLD),bg="#0000ff" )
input_range.place(x=40,y=90)


range_entry=Entry(win,width=15,font=("Times New Roman",25,BOLD,ITALIC))
range_entry.place(x=610,y=90)


label1=Label(win,text="You have 3 chances to guess the number !!",font=("Calibri",30,BOLD,ITALIC),bg="#FFFF00")
label1.place(x=105,y=150)

def guess():
    a=int((range_entry.get()))
    n=random.randrange(0,a)


    c1=Label(win,text="Enter Guess-1:",font=("Times New Roman",25,BOLD,ITALIC),bg="#FF0000")
    c1.place(x=150,y=305)

    c1g=Entry(win,width=15,font=("Times New Roman",25,BOLD,ITALIC))
    c1g.place(x=375,y=305)

    def c1f():
        c1n=int((c1g.get()))
        if c1n==n:
            end_msg1=Label(win,text="Congrats, you guessed it right !!!",font=("Calibri",25,BOLD,ITALIC),bg="#FF8000")
            end_msg1.place(x=20,y=500)
            
        else:
                c2=Label(win,text="Enter Guess-2:",font=("Times New Roman",25,BOLD,ITALIC),bg="#FF0000")
                c2.place(x=150,y=365)

                c2g=Entry(win,width=15,font=("Times New Roman",25,BOLD,ITALIC))
                c2g.place(x=375,y=365)

                def c2f():
                    c2n=int((c2g.get()))
                    if c2n==n:
                        end_msg2=Label(win,text="Congrats, you guessed it right !!!",font=("Calibri",25,BOLD,ITALIC),bg="#FF8000")
                        end_msg2.place(x=20,y=500)


                    else:
                            c3=Label(win,text="Enter Guess-3:",font=("Times New Roman",25,BOLD,ITALIC),bg="#FF0000")
                            c3.place(x=150,y=425)

                            c3g=Entry(win,width=15,font=("Times New Roman",25,BOLD,ITALIC))
                            c3g.place(x=375,y=425)

                            def c3f():
                                c3n=int((c3g.get()))
                                if c3n==n:
                                    end_msg3=Label(win,text="Congrats, you guessed it right !!!",font=("Calibri",25,BOLD,ITALIC),bg="#FF8000")
                                    end_msg3.place(x=20,y=500)
                                else:
                                    end_msg4=Label(win,text="Wrong Guesses, Better luck next time! The number was",font=("Calibri",25,BOLD,ITALIC),bg="#FF8000")
                                    end_msg4.place(x=25,y=500)

                                    end_msg5=Label(win,text=n,font=("Calibri",25,BOLD,ITALIC),bg="#FF8000")
                                    end_msg5.place(x=780,y=500) 


                            c3b=Button(win,text="Check",font=("Times New Roman",16,BOLD,ITALIC),bg="#A0A0A0",command=c3f)
                            c3b.place(x=675,y=425)
                                    

                c2b=Button(win,text="Check",font=("Times New Roman",16,BOLD,ITALIC),bg="#A0A0A0",command=c2f)
                c2b.place(x=675,y=365)
            

    c1b=Button(win,text="Check",font=("Times New Roman",16,BOLD,ITALIC),bg="#A0A0A0",command=c1f)
    c1b.place(x=675,y=305)


start_button=Button(win,text="Start Guessing",font=("Calibri",20,BOLD,ITALIC),bg="#00CC00",command=guess)
start_button.place(x=375,y=225)


win.mainloop()


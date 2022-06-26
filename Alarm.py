from cProfile import label         # it's use to take input box.
from turtle import bgcolor, title  # it's use to give color,title in the GUI Application form  
from playsound import playsound    # it's use to take sound  
from tkinter import *              # it's use of Tkinter library
from win10toast import ToastNotifier  # It's use to Notification
import datetime                       # It's use for taking date 
import time                           # It's use for taking time 

def alarm(set_alarm):     
    toast = ToastNotifier()        # for showing notifications
    while True:
        time.sleep(1)              # it will increase the time within 1 sec.
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("Alarm Clock")
            toast.show_toast("Alarm Clock", duration=2)
            playsound("Alarm-Fast-High-Pitch-A1.mp3")
            break
        
def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()                  # these from and import keywords here so you can't use these in place of root it will give you the error as a invalid 
                             # TK() is a function, we can use easly tkinter library in in pyhton.
root.title("Alarm Clock")    # give it the title of the project
root.geometry("670x410")          # to give it width and height using of the geometry(function)
photo=PhotoImage(file="cat.png")  # it's using for backgroud display
picture=Label(root,image=photo).place(x=0,y=0)     # to specify the width and length the GUI display page
info = Label(root,text = "(24)Hour  Min   Sec").place(x = 10)    # (.place) that mean acjesting of the text
set_time = Label(root,text = "Set Time",relief = "solid",font=("Cambria",10,"bold")).place(x=0,y=30)  # relief,bold=>dark and thick,  .place(x=0=>horizentol,y=0=>vertical)

# Entry Variables
hour = StringVar() # What is StringVar () in tkinter? The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectively
min = StringVar()
sec = StringVar()

# Entry Widget
hour_E = Entry(root,textvariable = hour,bg = "grey",width = 4).place(x=60,y=30)  #entry of hour
min_E = Entry(root,textvariable = min,bg = "grey",width = 4).place(x=90,y=30)    #entry of min.
sec_E = Entry(root,textvariable = sec,bg = "grey",width = 4).place(x=120,y=30)   #entry of sec.

submit = Button(root,text = "Set Alarm",width = 10,command = getvalue).place(x =50,y=70)  # command=getvalue that mean to get the values from getvalue function

root.mainloop()               # this is the mainloop(), it's work to intract our whole code to the tkinter library and bind-up the code in a function.
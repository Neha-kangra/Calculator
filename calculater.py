from tkinter import *
win=Tk()
win.title("calculator")
win.geometry("400x650")
win.config(bg="red")
#win.resizable(False,False)
#-------------------------------------

data=""

def get_data(value):
    global data

    data=data+str(value)
    var.set(data)

def equal_data():
    """Evaluate the expression """  
    global data
    try:
        total = str(eval(data))  
        var.set(total)
        data = total  
    except Exception as e:
        var.set("Error")
        data = ""

def clear_data():
    """Clear the input field"""
    global data

    data=""
    var.set(data)
#-----------------------------------------
#heading
label1=Label(win,text="CALCULATOR",font=("times new roman",30,"bold"))
label1.place(x=50,y=20)
#--------------------------------------
#textbox
var=StringVar()

entry1=Entry(win,font=("times new roman",40),textvariable=var)
entry1.place(x=10,y=90,width=370)
#-------------------------------------
#buttons
button7=Button(win,text="7",font=("times new roman",30,"bold")
               ,command=lambda:get_data(7))
button7.place(x=20,y=180,width=80)

button8=Button(win,text="8",font=("times new roman",30,"bold"),
               command=lambda:get_data(8))
button8.place(x=110,y=180,width=80)

button9=Button(win,text="9",font=("times new roman",30,"bold"),
               command=lambda:get_data(9))
button9.place(x=200,y=180,width=80)

bt_plus=Button(win,text="+",font=("times new roman",30,"bold"),
           command=lambda:get_data("+"))
bt_plus.place(x=290,y=180,width=80)
#--------------------------------
button4=Button(win,text="4",font=("times new roman",30,"bold"),
               command=lambda:get_data(4))
button4.place(x=20,y=270,width=80)

button5=Button(win,text="5",font=("times new roman",30,"bold"),
               command=lambda:get_data(5))
button5.place(x=110,y=270,width=80)

button6=Button(win,text="6",font=("times new roman",30,"bold"),
               command=lambda:get_data(6))
button6.place(x=200,y=270,width=80)

bt_minus=Button(win,text="-",font=("times new roman",30,"bold"),
           command=lambda:get_data("-"))
bt_minus.place(x=290,y=270,width=80)
#--------------------------------
button1=Button(win,text="1",font=("times new roman",30,"bold"),
               command=lambda:get_data(1))
button1.place(x=20,y=360,width=80)

button2=Button(win,text="2",font=("times new roman",30,"bold"),
               command=lambda:get_data(2))
button2.place(x=110,y=360,width=80)

button3=Button(win,text="3",font=("times new roman",30,"bold"),
               command=lambda:get_data(3))
button3.place(x=200,y=360,width=80)

bt_prod=Button(win,text="*",font=("times new roman",30,"bold"),
           command=lambda:get_data("*"))
bt_prod.place(x=290,y=360,width=80)
#---------------------------------
bt_clear=Button(win,text="c",font=("times new roman",30,"bold"),
           command=clear_data)
bt_clear.place(x=20,y=450,width=80)

button0=Button(win,text="0",font=("times new roman",30,"bold"),
               command=lambda:get_data(0))
button0.place(x=110,y=450,width=80)

bt_dot=Button(win,text=".",font=("times new roman",30,"bold"),
           command=lambda:get_data("."))
bt_dot.place(x=200,y=450,width=80)

bt_div=Button(win,text="/",font=("times new roman",30,"bold"),
           command=lambda:get_data("/"))
bt_div.place(x=290,y=450,width=80)
#-----------------------------------
bt_equal=Button(win,text="=",font=("times new roman",30,"bold"),
          command=equal_data)
bt_equal.place(x=110,y=550,width=160)


win.mainloop()

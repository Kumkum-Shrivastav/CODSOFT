from tkinter import *
window=Tk()
window.geometry("356x445")
window.title("Kumkum's Calci")

txt=StringVar()
expression= ""

def click(num):

    global expression
    expression = expression + str(num)
    txt.set(expression)

def equal():

    try:
        global expression
       
        add = str(eval(expression))
        txt.set(add)
        expression = " "

    except:
        expression.set("Error")
        expression=""

def clr():
  
    global expression
    length = len(txt.get())
    e1.delete(length - 1, 'end')


def clearAll():
   
    global expression
    expression = ""
    txt.set("")

frame1=Frame(window,width=390,height=100,bg="white")
frame1.pack(side=TOP)
frame2=Frame(window,width=390,height=368,bg="#171717")
frame2.pack(side=BOTTOM)

l1=Label(frame1,text="Calculator",font=("Arial Bold",20))
l1.pack(side=TOP,expand=YES)

e1=Entry(frame1,textvariable=txt,width=30,bd=10,font=("Arial Bold",12),
         fg="black",bg="#CDC0B0",relief=RIDGE,justify=RIGHT)
e1.pack(side=TOP)
e1.insert(0,"0")

but1=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(7),text="7",font=("Helvetica",16,'bold'))

but1.place(x=5,y=10)

but2=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(4),text="4",font=("Helvetica",16,'bold'))
but2.place(x=5,y=81)

but3=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(1),text="1",font=("Helvetica",16,'bold'))
but3.place(x=5,y=152)

but4=Button(frame2,padx=48,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(0),text="0",font=("Helvetica",16,'bold'))
but4.place(x=5,y=223)

but5=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(8),text="8",font=("",16,'bold'))
but5.place(x=72,y=10)

but6=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(5),text="5",font=("Helvetica",16,'bold'))
but6.place(x=72,y=81)

but7=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(2),text="2",font=("Helvetica",16,'bold'))
but7.place(x=72,y=152)

but8=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click("."),text=".",font=("Helvetica",16,'bold'))
but8.place(x=139,y=223)

but9=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
            command=lambda:click(9),text="9",font=("Helvetica",16,'bold'))
but9.place(x=139,y=10)

but10=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
             command=lambda:click(6), text="6", font=("Helvetica", 16,'bold'))
but10.place(x=139,y=81)

but11=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
             command=lambda:click(3),text="3",font=("Helvetica",16,'bold'))
but11.place(x=139,y=152)

but12=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
             command=lambda:click("+"),text="+",font=("Helvetica",16,'bold'))
but12.place(x=205,y=10)

but13=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
             command=lambda:click("-"),text="-",font=("Helvetica",16,'bold'))
but13.place(x=205,y=81)

but14=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
     command=lambda:click("*"),text="x",font=("Helvetica",16,'bold'))
but14.place(x=205,y=152)

but15=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
             command=lambda:click("/"),text="/",font=("Helvetica",16,'bold'))
but15.place(x=205,y=223)

but16=Button(frame2,padx=14,pady=84,bd=4,fg="white",bg='#171717',
             command=clr,text="CE",font=("Helvetica",16,'bold'))
but16.place(x=270,y=10)

but17=Button(frame2,padx=153,pady=14,bd=4,fg="white",bg='#171717',
             command=equal,text="=",font=("Helvetica",16,'bold'))
but17.place(x=5,y=294)

but18=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#171717',
             command=clearAll,text="CA",font=("Helvetica",16,'bold'))
but18.place(x=270,y=223)

window.mainloop()
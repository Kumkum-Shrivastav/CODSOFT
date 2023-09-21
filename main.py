try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import time
from psgn_fun import RandPass

def pwGenerator(size = 10): #defining function a function for the generation of password
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password);
    lbl_strength.configure(foreground="aliceblue", background=pw_color, text=pw_strength, font=('Comic Sans MS', 10, 'bold'), bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(.02)
    gui.update()
    gui.mainloop()


gui = Tk() #creation of a window of password gui interface
gui.title("Kumkum's Random Password Generator")
width = 590
height = 321
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

PASSWORD = StringVar() #defining variables
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(7) #sets the default value for PW size

Top = Frame(gui, width=width)
Top.pack(side=TOP)
Form = Frame(gui, width=width)
Form.pack(side=TOP)
Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)

lbl_title = Label(Top, width=width, font=('Comic Sans MS', 12, 'bold'), text="choose:-Size & Click:-Generate Passwod Here", bd=2, relief=SOLID)
lbl_title.pack(fill=X)
lbl_password = Label(Form, font=('Comic Sans MS', 16), text="Password: ", bd=8)
lbl_password.grid(row=0, pady=11)
lbl_strength = Label(Form, font=('Comic Sans MS', 10, 'bold'), foreground="white", background="#6d0001", text="Weak", bd=10, height=1, width=10)
lbl_strength.grid(row=0, column=3, pady=10, padx=10)
lbl_pw_size = Label(Form, font=('Comic Sans MS', 16), text="Size: ", bd=8)
lbl_pw_size.grid(row=1, pady=11)
lbl_instructions = Label(Bot, width=width, font=('Comic Sans MS', 11, 'bold'), text="Copy your password from clipboard.", bd=1, relief=SOLID)
lbl_instructions.pack(fill=X)

password = Entry(Form, textvariable=PASSWORD, font=(18), width=24) #accepting values for password generation
password.grid(row=0, column=1, columnspan=2)
pw_size = Scale(Form, from_=8, to=24, length=230,width=24,sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, font=(18))
pw_size.grid(row=1, column=1, columnspan=2)


btn_generate = Button(Form, text="Generate Password Here", width=20, command=lambda: pwGenerator(PW_SIZE)) 
btn_generate.grid(row=2, column=1, columnspan=2)

gui.mainloop()
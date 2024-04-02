from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import hashlib

# Correctly initialize the master password and hash it outside of the function.
masterPass = 'Jason'
hashedMasterPass = hashlib.sha256(masterPass.encode()).hexdigest()

def encryption(passInput):
    # This function now just returns the hashed version of the input.
    return hashlib.sha256(passInput.encode()).hexdigest()

def loginButton():
    # Hash the input and compare it to the hashed master password.
    if encryption(passCode.get()) == hashedMasterPass:
        create_new_window()

        
    else:
        messagebox.showinfo("Error ", "You're on fraud alert 🚨")

def create_new_window():
    new_window = Toplevel(root)
    new_window.configure(bg= "#F1B46D")
    new_window.title("Welcome")
    new_window.geometry("925x500")
    new_window.resizable(False,False)
    Label(new_window, text="Huh.. I guess it's really you..👄", bg= "#F1B46D", fg="Teal",font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=310,y=150)
    option1 = Label(new_window, text="1. Create New", bg="#F1B46D", fg='teal').place(x=385, y=200)
    option2 = Label(new_window, text="2. Search password", bg='#F1B46D', fg='teal').place(x=385,y=220)
    option3 = Label(new_window, text="3. Delete a password",bg='#F1B46D', fg="teal").place(x=385,y=240)
    optionButton1 = Button(new_window, text='1', width=1, height=1,bg='#FBEED3',command=clickOption1).place(x=380,y=300)
    optionButton2 = Button(new_window, text='2', width=1, height=1,bg='#FBEED3',command=clickOption2).place(x=430,y=300)
    optionButton3 = Button(new_window, text='3', width=1, height=1,bg='#FBEED3',command=clickOption3).place(x=480,y=300)
    global quickBallImg
    quickBallImg = PhotoImage(file='/Users/jeg/Desktop/Python/Password-Manager/PassImages/quickball.png')
    Label(new_window, image=quickBallImg, bg='#F1B46D').place(x=5, y=150)  # Corrected the background color reference
    Label(new_window, image=quickBallImg, bg='#F1B46D').place(x=750, y=150)  # Corrected the background color reference



def clickOption1():
    messagebox.showinfo("Create New", "Option to create a new password entry.")

def clickOption2():
    messagebox.showinfo("Search", "Option to search password entry.")

def clickOption3():
    messagebox.showinfo("Delete", "Option to delete existing password entry.")





root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file="/Users/jeg/Desktop/Python/Password-Manager/PassImages/drag.png")
Label(root, image=img, bg="white").place(x=50, y=20)

frame = Frame(root, width=350, height=350, bg="orange")
frame.place(x=480, y=80)
heading = Label(frame, text='Master Password', bg="orange", fg="teal", font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=80, y=80)

passCode = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
passCode.place(x=85, y=150)

blackLine =Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

button = Button(frame, text="Is it really you?", command=loginButton)
button.place(x=110, y=200)

result_label = Label(frame, text="", bg="orange", fg="teal", font=('Microsoft YaHei UI Light', 12))
result_label.place(x=80, y=250)

root.mainloop()
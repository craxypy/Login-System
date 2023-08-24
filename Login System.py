import customtkinter 
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("Login System")
app.geometry("500x250")
app.config(bg="#242320")
font1=('Times New Roman' ,20, )
app.resizable = (False)


username = "craxy"
key = "test"
attempts = 0


def login():
    global username
    global key
    global attempts
    written_username=username_entry.get()
    written_key=key_entry.get()
    if(written_username=='' or written_key==''):
        messagebox.showwarning(title='Error',message="Enter User and Key.")
    elif(written_username==username and written_key==key):
        newwindow=Toplevel(app)
        newwindow.geometry("500x250")
        newwindow.config(bg="#242320")
        welcome_label=customtkinter.CTkLabel(newwindow,text="Welcome To ...", font=font1, text_color="#FFFFFF")
        welcome_label.place(x=100,y=100)
    elif((written_username!=username or written_key!=key) and attempts<3):
        messagebox.showerror(title="Error",message="Incorrect Key or User.")
        attempts=attempts+1
        if(attempts!=3):
            attempts_label=customtkinter.CTkLabel(app,text=f'You have {3-attempts} attempts.', font=font1,text_color="#FFFFFF")
            attempts_label.place(x=100, y=200)
        if(attempts==3):
            login_button.destroy()
            locked_label=customtkinter.CTkLabel(app,text=f'Your key is invalidated.', font=font1,text_color="#FFFFFF")
            locked_label.place(x=100, y=160)





username_label=customtkinter.CTkLabel(app,text="Username:",font=font1,text_color="#FFFFFF")
username_label.place(x=3,y=25)

key_label=customtkinter.CTkLabel(app,text="Key:",font=font1,text_color="#FFFFFF")
key_label.place(x=3,y=100)

username_entry=customtkinter.CTkEntry(app,fg_color="#FFFFFF",font=font1,text_color="#000000",border_color="#FFFFFF", width=250,height=1)
username_entry.place(x=130,y=25)

key_entry=customtkinter.CTkEntry(app,show ='*',fg_color="#FFFFFF",font=font1,text_color="#000000",border_color="#FFFFFF", width=250,height=1)
key_entry.place(x=130,y=100)

login_button=customtkinter.CTkButton(app,command=login,text="Login", font=font1,text_color="#FFFFFF",fg_color="#07b527",hover_color="#07b527",width=76)
login_button.place(x=150,y=150)

credits_label=customtkinter.CTkLabel(app,text="Made by Craxy.",font=font1,text_color="#FFFFFF")
credits_label.place(x=450,y=125)


app.mainloop()

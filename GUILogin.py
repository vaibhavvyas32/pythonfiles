import tkinter

window = tkinter.Tk()
window.title("Login Program")
window.geometry("200x200")
def btn_login():
    print("Login Successful")
    tkinter.Label(window,text="Login Successful",fg="Blue").grid(row=4,column=1)
tkinter.Label(window, text = "Username").grid(row = 0)
tkinter.Entry(window).grid(row = 0, column = 1)
tkinter.Label(window, text = "Password").grid(row = 1)
tkinter.Entry(window).grid(row = 1, column = 1)
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)
btn1=tkinter.Button(window,text="Login",command=btn_login)
btn1.grid()


window.mainloop()
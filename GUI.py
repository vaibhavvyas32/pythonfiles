import tkinter
root=tkinter.Tk()
root.title("Just A Program")
root.geometry("300x300+200+200")
def btnexit():
   exit(1)
button1=tkinter.Button(main=root,text="EXIT",fg="Red",command=btnexit)
button1.pack()
root.mainloop()
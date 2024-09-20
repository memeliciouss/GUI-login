import tkinter as tk
def fun():
    print("presseddd")
win = tk.Tk()  
win.title("TIKLE")
win.maxsize(width=666,height=666)
win.minsize(width=55,height=55)

a=tk.Label(win,text="HELLO",bg="BLUE")
a.pack(padx=33,pady=99)
b=tk.Label(win,text="NO BYE")
b.pack()

ent=tk.Entry(win)
ent.pack()

b=tk.Button()

b1 =tk.Button(win,text = "Red",activeforeground = "red",activebackground ="pink",pady=10)
b1.pack()

win.mainloop()

import tkinter as tk
from idlelib.tooltip import Hovertip
import tkinter.font as tkFont


app = tk.Tk()

myBtn = tk.Button(app,text='Ayuda')

fontExample=tkFont.Font(family="Arial")
myBtn.configure(font=fontExample)

myBtn.pack(pady=30)
myTip = Hovertip(myBtn,'mexico de mis amores')
app.mainloop()
from tkinter import *
import tkinter 

window = Tk()
window.title("Nintendo")
window.configure(width=1300, height=700)
window.configure(bg="white")

T = Text(window, height = 700, width = 1300,font=('Century Schoolbook', 50, 'italic'))
T.tag_configure("tag_name", justify='center')
T.tag_add("tag_name", "1.0", "end")
Fact = ' Welcome To NINTENDO! ' 
T.pack()

T.insert(tkinter.END, Fact)

window.mainloop()

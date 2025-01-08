from tkinter import *
root = Tk()

text= Text(root, width =40, height =10)
text.pack()
text.config(wrap ="word")
text.get("1.0", "end")
text.get("1.0", "1.end")
text.insert("1.0 + 2 lines", "Inserted message")
text.insert("1.0 + 2lines lineend", "and \n More")

text.delete("1.0")
text.replace("1.0","1.0 lineend","This is the first line")
text.delete("1.0","3.0 lineend")
text.replace("1.0","1.0 lineend","This is the first line")


root.mainloop()

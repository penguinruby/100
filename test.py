from tkinter import *
root = Tk()

root.option_add("*tearOff", False)
menuBar = Menu(root)
root.config(menu= menuBar)
file = Menu(menuBar)
edit = Menu(menuBar)
save = Menu(file)
help_ =Menu(menuBar)
menuBar.add_cascade(menu = file, label ="File")
menuBar.add_cascade(menu = edit, label ="Edit")
menuBar.add_cascade(menu = help_, label ="Help")
file.add_command(label = "New", command = lambda:print("New File"))

file.add_separator()
file.add_command(label = "open...", command = lambda: print("Opening File..."))
file.add_command(label ="Save", command= lambda :print("Save File"))
file.entryconfig("New", accelerator =" Ctrl + N")
# file.entryconfig("New", state ="disable")
# file.delete("Save")
file.add_cascade(menu = save, label= "Save")
save.add_command(label = "Save As", command = lambda: print("saving As..."))

choice = IntVar
edit.add_radiobutton(label="1", variable= choice, value = 1)




root.mainloop()

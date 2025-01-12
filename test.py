# from tkinter import *
# root = Tk()

# root.option_add("*tearOff", False)
# menuBar = Menu(root)
# root.config(menu= menuBar)
# file = Menu(menuBar)
# edit = Menu(menuBar)
# save = Menu(file)
# help_ =Menu(menuBar)
# menuBar.add_cascade(menu = file, label ="File")
# menuBar.add_cascade(menu = edit, label ="Edit")
# menuBar.add_cascade(menu = help_, label ="Help")
# file.add_command(label = "New", command = lambda:print("New File"))

# file.add_separator()
# file.add_command(label = "open...", command = lambda: print("Opening File..."))
# file.add_command(label ="Save", command= lambda :print("Save File"))
# file.entryconfig("New", accelerator =" Ctrl + N")
# # file.entryconfig("New", state ="disable")
# # file.delete("Save")
# file.add_cascade(menu = save, label= "Save")
# save.add_command(label = "Save As", command = lambda: print("saving As..."))

# choice = IntVar
# edit.add_radiobutton(label="1", variable= choice, value = 1)




# root.mainloop()


my_list=[]
for i in range(5):
    my_list.append("A")
print(my_list)

my_list=["A" for i in range(5)]
print(my_list)


my_list=[]
for i in range(5):
    my_list.append([])
    for x in range(5):
        my_list[i].append("A")
print(my_list)

my_list=[["A" for i in range(5)]for x in range(5)]
print(my_list)

my_list=[1, 2 , 3,4,5,5,6]
x = [ n for n in my_list if n >= 3]
print(x)


my_list=[1, 2 , 3,4,5,5,6]
x = [ n if n >= 3 else "NO" for n in my_list]
print(x)





my_list=[1,2,3,4,5]
new_list=[]
for i in my_list:
    new_list.append (i+i)
print(new_list)


my_list=[1,2,3,4,5]
new_list = [i+i for i in my_list]
print(new_list)

print((lambda a,b: a+b)(5, 5))

x = 5
y = 3
if x > y:
    print(x)
else:
    print(y)

my_num =[1,2,3,4,5,6,7,8,9,10]

squares = list(map(lambda x: x**2, my_num))
print(squares)
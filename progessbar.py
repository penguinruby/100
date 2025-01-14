from tkinter import *
from tkinter import ttk
import time
import random
def move_no_button(event):
    new_x = random.randint(0, 480)
    new_y = random.randint(0, 200)
    end_button.place(x =new_x, y =new_y)

root = Tk()

txt= ttk.Label(root, text= "This is never end progress bar")
txt.pack()

def no_use():
     txt.config(text ="No, I am joking, still never end")

end_button = ttk. Button(root, text="click me to finish progress",  command=no_use)
end_button.pack()
end_button.bind("<Enter>", move_no_button)

#進度條 max的部分是速度,數字越小越快  用 inde 進度調不會填滿  
progessbar = ttk.Progressbar(root, orient = HORIZONTAL, length=300, mode="determinate",takefocus="True", maximum= 500)
progessbar.place(x=70, y=70)

progessbar.start()
time.sleep(2)



root.title("No progress")
root.geometry("480x200")

root.mainloop()


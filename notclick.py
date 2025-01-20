import tkinter as tk
import random
def move_no_button(event):
    new_x = random.randint(0, 500)
    new_y = random.randint(0, 500)
    no_button.place(x =new_x, y =new_y)


def you_got_me():
    label.config(text ="Happy Birthday!")

def no_use():
     label.config(text ="You need to catch your cake!")


root=tk.Tk()
root.title("Catch me if you can!")
root.geometry("800x600")   #視窗大小

label = tk.Label(root, text="Catch me if you can!", font=("comicsans", 20))
label.pack(pady=5)  #標籤字的位置 

yes_button = tk. Button(root, text="Don't touch me", font=("comicsans", 10), command=no_use)
yes_button.pack(side=tk.LEFT, padx = 50)

no_button = tk. Button(root, text="I am cake", font=("comicsans", 10), command=you_got_me)
no_button.place(x=250, y =100)  #按鈕一開始的位置
no_button.bind("<Enter>", move_no_button) #標籤通常沒有 command 屬性，所以如果你想要excute一些動作，就會用bind,就是當滑鼠碰到那個東西時的動作

root.mainloop()




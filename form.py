from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FeedBack:
    def __init__(self,master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.logo =PhotoImage(file ="C:\\Users\\user\\Desktop\\python\\100\\ToastFly.png")
        ttk.Label(self.frame_header, image =self.logo).grid(row=0, column=0, rowspan =2)
        ttk.Label(self.frame_header, text = "Thanks for Exploring!").grid(row=0, column=2)
        ttk.Label(self.frame_header, text = "We are glad you choose us").grid(row=1, column =1)


        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()


        ttk.Label(self.frame_content, text ="Name").grid(row=0, column=0)
        ttk.Label(self.frame_content, text ="Email").grid(row=0, column=1)
        ttk.Label(self.frame_content, text ="Comments").grid(row=2, column=0)

        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.text_comments=Text(self.frame_content, width =50, height = 10)

        self.entry_name.grid(row=1, column=0)
        self.entry_email.grid(row=1, column=1)
        self.text_comments.grid(row=3, column=0, columnspan=2)

        ttk.Button(self.frame_content,text ="Submit", command = self.submit).grid(row=4, column=0)
        ttk.Button(self.frame_content, text="Clear",command = self.clear).grid(row=4, column=1)

    def submit(self):
        print("Name: {}".format(self.entry_name.get()))
        print("Email: {}".format(self.entry_email.get()))
        print("Comments: {}".format(self.text_comments.get(1.0, "end")))
        self.clear()
        messagebox.showinfo(title ="Feebback result", message="submitted")
 
    def clear(self):
        self.entry_name.delete(0, "end")
        self.entry_email.delete(0,"end")
        self.text_comments.delete(1.0, "end")


def main():
    root=Tk()
    feedback =FeedBack(root)
    root.title("Fill up")
    root.geometry("800x600")   #視窗大小
    root.mainloop()

if __name__ =="__main__": main()




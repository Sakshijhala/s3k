from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root, text="HELP DESK",font=("times new roman", 35, "bold"),bg="white", fg="blue" )
        title_lbl.place(x=0, y=0, width=1300, height=40)

        img_top=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (2).jpeg" )
        img_top= img_top.resize((1280,720), Image.LANCZOS)
        self.photoimg_top =ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1280, height=720) 
        
        dev_label=Label(f_lbl , text="Email: sakshijhala07@gmail.com",font=("times new roman", 30, "bold"), fg="dark blue",bg="white")
        dev_label.place(x=350, y=100)
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
    
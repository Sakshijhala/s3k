from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root, text="DEVELOPER",font=("times new roman", 35, "bold"),bg="white", fg="blue" )
        title_lbl.place(x=0, y=0, width=1300, height=40)

        img_top=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (2).jpeg")
        img_top= img_top.resize((1280,720), Image.LANCZOS)
        self.photoimg_top =ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1280, height=720) 
        
        #Frame
        main_frame=Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=450, y=50, width=350, height= 500) 
        
        
        img_top1=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\WhatsApp Image 2024-09-22 at 00.32.53_ae914b89.jpg")
        img_top1= img_top1.resize((200,200), Image.LANCZOS)
        self.photoimg_top1 =ImageTk.PhotoImage(img_top1)
        
        f_lbl = Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=60, y=0, width=200, height=200) 
        
        # Developer
        
        dev_label=Label(main_frame, text="Hello My Name is Sakshi!!",font=("times new roman", 20, "bold"), fg="white",bg="dark blue")
        dev_label.place(x=20, y=200)
        
        dev_label=Label(main_frame, text="I Am Python Developer",font=("times new roman", 20, "bold"),fg="white",bg="dark blue")
        dev_label.place(x=20, y=250)
        
        dev_label=Label(main_frame, text="This is  an Group Project",font=("times new roman", 20, "bold"),fg="white",bg="dark blue")
        dev_label.place(x=20, y=300)
        
        dev_label=Label(main_frame, text="We Develelop this Project",font=("times new roman", 20, "bold"),fg="white",bg="dark blue")
        dev_label.place(x=20, y=350)
        
        dev_label=Label(main_frame, text="Using Tkinter Library",font=("times new roman", 20, "bold"),fg="white",bg="dark blue")
        dev_label.place(x=20, y=380)
        
        dev_label=Label(main_frame, text="ThankYou!!",font=("times new roman", 20, "bold"),fg="white",bg="dark blue")
        dev_label.place(x=80, y=430)
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
    
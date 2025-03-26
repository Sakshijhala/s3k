from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
from student import student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # first image
        
        img=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images.jpeg")
        img = img.resize((300,130), Image.LANCZOS)
        self.photoimg =ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=300, height=130)
        
        # second image
        
        img1=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\download (2).jpeg")
        img1 = img1.resize((500,130), Image.LANCZOS)
        self.photoimg1 =ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=250, y=0, width=700, height=130)
        
        #third image
        
        img2=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (3).jpeg")
        img2 = img2.resize((300,130), Image.LANCZOS)
        self.photoimg2 =ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=300, height=130)
        
        # bg img
        img3=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (1).jpeg")
        img3 = img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3 =ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman", 35, "bold"),bg="white", fg="red" )
        title_lbl.place(x=0, y=0, width=1300, height=45)
        
        # ===================== time ===========================
        def time():
            string = strftime('%H:%M:%S:%p')
            lbl.config(text= string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font=("times new roman", 15, "bold"),bg="white", fg="blue")
        lbl.place(x=10, y=0, width=120, height=40)
        time()
        
        # student button
        
        img4=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (3).jpeg")
        img4 = img4.resize((220,220), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=100,y=70,width=220, height=220)
        
        b1_1=Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=100,y=250,width=220, height=40)
        
        # detect face button
        
        img5=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (5).jpeg")
        img5 = img5.resize((220,220), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=400,y=70,width=220, height=220)
        
        b1_1=Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=400,y=250,width=220, height=40)
        
        # Attendance face button
        
        img6=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\download (2).jpeg")
        img6 = img6.resize((220,220), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=700,y=70,width=220, height=220)
        
        b1_1=Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=700,y=250,width=220, height=40)
        
        # help face button
        
        img7=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (11).jpeg")
        img7 = img7.resize((220,220), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b1.place(x=1000,y=70,width=220, height=220)
        
        b1_1=Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=1000,y=250,width=220, height=40)
        
        # train face button
        
        img8=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\th (4).jpeg")
        img8 = img8.resize((220,220), Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img, image=self.photoimg8, cursor="hand2", command = self.train_data)
        b1.place(x=100,y=300,width=220, height=220)
        
        b1_1=Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=100,y=460,width=220, height=40)
        
        #photos face button
        
        img9=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (8).jpeg")
        img9 = img9.resize((220,220), Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=400,y=300,width=220, height=220)
        
        b1_1=Button(bg_img, text="PHOTOS", cursor="hand2",command=self.open_img, font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=400,y=460,width=220, height=40)
        
        
        #developer face button
        
        img10=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\images (9).jpeg")
        img10 = img10.resize((220,220), Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b1.place(x=700,y=300,width=220, height=220)
        
        b1_1=Button(bg_img, text="DEVELOPER", cursor="hand2",command=self.developer_data, font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=700,y=460,width=220, height=40)
        
        #Exit face button
        
        img11=Image.open(r"C:\Users\Meena Jhala\Desktop\major prject\college_images\exit.jpg")
        img11 = img11.resize((220,220), Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1000,y=300,width=220, height=220)
        
        b1_1=Button(bg_img, text="EXIT", cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="blue", fg="white")
        b1_1.place(x=1000,y=460,width=220, height=40)
        
    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
        
       #========== Function button ======================
       
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
            
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
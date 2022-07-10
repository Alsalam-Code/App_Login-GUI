from tkinter import *
def App():
 pro = Tk()
 pro.title('LOGIN SYSTEM')
 pro.geometry('500x500')
 # pro.resizable(False,False)
 pro.config(background='#5D6D7E')
 pro.iconbitmap(r"E:\my files\yousef programing\APPS\APP\image\logo2.ico")
 #-------------- title -------------
 title = Label(pro, text='LOGIN SYSTEM', font=('Courier',15), bg='black',fg='white')
 title.pack(fill=X)
 #-------------- frame -----------
 fr1 = Frame(pro, width='400', height='390', bg='#2E4053')
 fr1.pack(pady=40)
 #-------------- image -----------
 photo = PhotoImage(file="E:\my files\yousef programing\APPS\APP\image\logo.png")
 panal = Label(pro, image=photo)
 panal.place(x=200, y=50)
 #-------------- label -------------
 lb1 = Label(fr1, text='USERNAME :', font=('Courier',14), bg='whitesmoke',fg='black')
 lb1.place(x=10, y=140)
 lb2 = Label(fr1, text='PASSWORD :', font=('Courier',14), bg='whitesmoke',fg='black')
 lb2.place(x=10, y=180)
 #-------------- Entry -------------
 en1 = Entry(fr1)
 en1.place(x=137, y=144)
 en2 = Entry(fr1)
 en2.place(x=137, y=184)
 #-------------- Button ------------
 bt1 = Button(fr1, text='LOGIN', font=('Courier', 15),bg='black', fg='green')
 bt1.place(x=15, y=260)
 bt2 = Button(fr1, text='SIGNIN', font=('Courier', 15),bg='black', fg='yellow')
 bt2.place(x=115, y=260)
 bt3 = Button(fr1, text='Help', font=('Courier', 15),bg='black', fg='red')
 bt3.place(x=235, y=260)
 #-------------- checkbox -----------
 c1 = Checkbutton(fr1, text='Forget Password!', font=('Courier', 9), bg='whitesmoke')
 c1.place(x=36, y=210)
 #------------ By --------------------
 by = Label(fr1, text='Developed By YOUSEF @2022',font=('Courier',8) )
 by.place(x=105, y=360)

 pro.mainloop()

App()

from tkinter import Tk,Label,Button,Entry,Checkbutton,Frame

root=Tk()
root.geometry("500x500")
user=Label(text="username :")
password=Label(text="password :")
# user.pack()
# password.pack()
user.place(x=125,y=150)
password.place(x=125,y=200)
root.title("PANDORA")
heading =Label(text='PANDORA',fg='black',font=('TIMES IN ROMAN',50)).place(x=100,y=50)
user=Entry().place(x=200,y=150)
password=Entry().place(x=200,y=200)
sub=Button(text='Login').place(x=200,y=250)
ar=Button(text='create account').place(width=120,height=40,x=150,y=400)
dr=Checkbutton(text='male').place(width=100,height=50,x=110,y=300)
sp=Checkbutton(text='female').place(width=100,height=50,x=200,y=300)

root.mainloop()





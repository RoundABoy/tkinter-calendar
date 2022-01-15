from tkinter import *
import calendar
root=Tk()
root.geometry("400x350")

def show():
  m=int(month.get())
  y=int(year.get())
  output=calendar.month(y,m)
  cal.insery("end",output)

def clear():
  cal.delete(1.0,"end")

def exit():
  root.destroy()

m_label=Label(root,text='Month',font=("universal condensed",10))
m_label.place(x=70,y=80)

month=Spinbox(root,from_=1,to=12,width="5")
month.place(x=140,y=80)

y_label=Label(root,text='Year',font=("universal condensed",10))
y_label.place(x=210,y=80)

year=Spinbox(root,from_=2000,to=3000,width="5")
year.place(x=260,y=80)

cal=Text(root,width=33,height=8,borderwidth=2)
cal.place(x=70,y=110)

clear=Button(root,text="Clear",font=("verdana",10,"bold"),borderwidth=2,command=clear)
clear.place(x=200,y=250)

exit=Button(root,text="Exit",font=("verdana",10,"bold"),borderwidth=2,command=exit)
exit.place(x=260,y=250)

root.mainloop()



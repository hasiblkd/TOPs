from tkinter import *

# Starting Point

root=Tk()

# size of interface
root.geometry("500x500")

# for Title
root.title("My App")

# Pack Layout:- it is used when you want display element of application corner(left,right,bottom,top).

# b=Button(root,text="Submit")
# b.pack(side=LEFT)

# b1=Button(root,text="Submit")
# b1.pack(side=RIGHT)

# b2=Button(root,text="Submit")
# b2.pack(side=TOP)

# b3=Button(root,text="Submit")
# b3.pack(side=BOTTOM)

# grid Layout:- it used row and column to display a data.

# l1=Label(root,text="Username")
# l1.grid(row=1,column=1)

# l2=Label(root,text="Email")
# l2.grid(row=2,column=1)

# l3=Label(root,text="Phone no.")
# l3.grid(row=3,column=1)

# Entry():- it is used for textbox.

# t1=Entry(root)
# t1.grid(row=1,column=2)

# t2=Entry(root)
# t2.grid(row=2,column=2)

# t3=Entry(root)
# t3.grid(row=3,column=2)

# b=Button(root,text="Submit")
# b.grid(row=4,column=2)

# place:- it used x,y axis to display data.

l1=Label(root,text="Username")
l1.place(x=100,y=150)

l2=Label(root,text="Email")
l2.place(x=100,y=200)

l3=Label(root,text="Phone no.")
l3.place(x=100,y=250)

t1=Entry(root)
t1.place(x=170,y=150)

t2=Entry(root)
t2.place(x=170,y=200)

t3=Entry(root)
t3.place(x=170,y=250)

b=Button(root,text="Submit")
b.place(x=170,y=300)


# for Ending point

root.mainloop()
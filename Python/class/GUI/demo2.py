from tkinter import *
import mysql.connector as sql

con=sql.connect(
    host="",
    port="",
    user="",
    password="",
    database=""
)
cursor=con.cursor()
print(con.is_connected())
# Starting Point

root=Tk()

# size of interface
root.geometry("500x500")

# for Title
root.title("My App")


def get_data():
    name=t1.get()
    email=t2.get()
    phone_no=t3.get()

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
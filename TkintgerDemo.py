from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
def create_conn():
    return mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="python_11_30"
        )
def insert_data():
    if e_fname.get()=="" or e_lname=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fileds Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")

root=Tk()
root.geometry("340x470")
root.title("Student Registration")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Arial",10))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("Arial",10))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME",font=("Arial",10))
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("Arial",10))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE",font=("Arial",10))
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",12),command=insert_data)
insert.place(x=80,y=320)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",12))
search.place(x=180,y=320)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",12))
update.place(x=80,y=390)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",12))
delete.place(x=180,y=390)

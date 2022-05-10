from numpy import identity


colors=['#2A7FDB']
def slider():
	global count,text
	if(len(text)<count):
		cont=0
		text=''
	text=text+text[count]
	title.configure(text=text)
	color=random.choice(colors)
	title.config(bg=color)
	count+=1
	root.after(250,slider)

def fetch_data(event=None):
	db=sqlite3.connect('students.db')
	con=db.cursor()
	con.execute("select * from student")
	rows = con.fetchall()
	if len(rows) != 0:
		student_table.delete(*student_table.get_children())
		for row in rows:
			student_table.insert('', END, values=row)
		db.commit()
	db.close()

def show_all():
	db=sqlite3.connect('students.db')
	con=db.cursor()
	rows=con.execute('select * from student')
	for row in rows:
		student_table.insert('',END,values=row)
	db.commit()
	db.close()
	fetch_data()

def search_data():
	db=sqlite3.connect('students.db')
	con=db.cursor()
	con.execute(
		"select * from student where  " + str(search.get()) + " Like '%" + str(search_entry.get()) + "%'")
	rows = con.fetchall()
	if len(rows) != 0:
		student_table.delete(*student_table.get_children())
		for row in rows:
			student_table.insert('', END, values=row)
		db.commit()
	db.close()




def delete():
	db = sqlite3.connect('students.db')
	con = db.cursor()
	con.execute("delete from student where fname='"+fname.get()+"'")
	db.commit()
	db.close()
	fetch_data()
	messagebox.showinfo('Success', 'Student has been deleted')
	clear()


def update():
	db=sqlite3.connect('students.db')
	con=db.cursor()
	con.execute("update student set fname='"+fname.get()+"',lname='"+lname.get()+"',email='"+email.get()+"',gender='"+gender.get()+"',contact='"+contact.get()+"',date='"+date.get()+"',adress='"+address_text.get(1.0,END)+"' where id='"+id.get()+"'")
	messagebox.showinfo('Success','Students\' information updated')
	db.commit()
	fetch_data()
	clear()
	db.close()

def get_cursor(event=None):
	cursor_row=student_table.focus()
	content=student_table.item(cursor_row)
	row=content['values']
	ide.set(row[0])
	fname.set(row[1])
	lname.set(row[2])
	email.set(row[3])
	gender.set(row[4])
	contact.set(row[5])
	date.set(row[6])
	address_text.delete(1.0,END)
	address_text.insert(END,row[7])

def clear():
	fname.set('')
	lname.set('')
	email.set('')
	gender.set('')
	contact.set('')
	date.set('')
	address_text.delete(1.0,END)

def add():
	db = sqlite3.connect('students.db')
	con = db.cursor()
	con.execute("insert into student values(null ,'"+fname.get()+"','"+lname.get()+"','"+email.get()+"','"+gender.get()+"','"+contact.get()+"','"+date.get()+"','"+address_text.get(1.0,'end')+"');")
	db.commit()
	db.close()
	fetch_data()
	messagebox.showinfo('Success','Student has been added')
	clear()



from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import random
count=0
text=' Student management system '

root=Tk()
root.title('Student Management System')
root.geometry('1350x800+0+0')
title=Label(root,text='',font='timesnewroman 30 bold',fg='black',bg='powder blue',bd=4,relief=RAISED,width=10)
title.pack(side='top',fill='x')
##################variables
ide=int()
fname=StringVar()
lname=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()
date=StringVar()
search=StringVar()
#####################mange_frame
manage_frame=Frame(root,bd=4,relief=RIDGE,bg='powder blue')
manage_frame.place(x=20,y=80,width=550,height=545)
#Manage Title
m_title=Label(manage_frame,text='Information',font='timesnewroman 30 bold',bd=2,bg='#1DA0C8',fg='white',relief=RAISED)
m_title.grid(row=0,columnspan=2,padx=20,pady=20)

#labes
lbl_fname=Label(manage_frame,text='First name',font='timesnewroman 19 bold',bd=0,bg='#1DA0C8',fg='white',relief=RAISED)
lbl_fname.grid(row=1,column=0,padx=20,pady=10,sticky='w')

fname_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=fname)
fname_entry.grid(row=1,column=1,padx=20,pady=10,sticky='w')

lbl_lname=Label(manage_frame,text='Last name',font='timesnewroman 19 bold',bd=0,bg='#1DA0C8',fg='white',relief=RAISED)
lbl_lname.grid(row=2,column=0,padx=20,pady=10,sticky='w')

lname_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=lname)
lname_entry.grid(row=2,column=1,padx=20,pady=10,sticky='w')

lbl_email=Label(manage_frame,text='Email',font='timesnewroman 19 bold',bd=0,bg='#1DA0C8',fg='white',relief=RAISED)
lbl_email.grid(row=3,column=0,padx=20,pady=10,sticky='w')

email_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=email)
email_entry.grid(row=3,column=1,padx=20,pady=10,sticky='w')

lbl_gender=Label(manage_frame,text='Gender',font='timesnewroman 19 bold',bd=0,bg='#1DA0C8',fg='white',relief=RAISED)
lbl_gender.grid(row=4,column=0,padx=20,pady=10,sticky='w')

combo_gender=ttk.Combobox(manage_frame,width=18,font='timesnewroman 20 bold',state='r',textvariable=gender)
combo_gender['values']=('Male','Female','Other ')
combo_gender.grid(row=4,column=1,padx=20,pady=10,sticky='w')
combo_gender.set('Select Gender')


lbl_contact=Label(manage_frame,text='Contact',font='timesnewroman 19 bold',bd=0,bg='#1DA0C8',fg='white',relief=RAISED)
lbl_contact.grid(row=5,column=0,padx=20,pady=10,sticky='w')

contact_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=contact)
contact_entry.grid(row=5,column=1,padx=20,pady=10,sticky='w')

lbl_date=Label(manage_frame,text='Date',font='timesnewroman 19 bold',bd=0,bg='#1DA0C8',fg='white',relief=RAISED)
lbl_date.grid(row=6,column=0,padx=20,pady=10,sticky='w')

date_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=date)
date_entry.grid(row=6,column=1,padx=20,pady=10,sticky='w')


lbl_address=Label(manage_frame,text='Address',font='timesnewroman 19 bold',bd=0,bg='#1DA0C8',fg='white',relief=RAISED)
lbl_address.grid(row=7,column=0,padx=20,pady=10,sticky='w')

address_text=Text(manage_frame,width=20,height=3,font='timesnewroman 19 bold')
address_text.grid(row=7,column=1,padx=20,pady=10,sticky='w')
######### button frames
btn_frame=Frame(root,bd=4,relief=RIDGE,bg='#2A7FDB')
btn_frame.place(x=23,y=625,width=545)

add_btn=Button(btn_frame,text='ADD',width=13,height=2,fg='black',bg='#1DC8BB',command=add)
add_btn.grid(row=0,column=0,padx=10,pady=10)

update_btn=Button(btn_frame,text='UPDATE',width=13,height=2,fg='black',bg='#1DC8BB',command=update)
update_btn.grid(row=0,column=1,padx=10,pady=10)

delete_btn=Button(btn_frame,text="DELETE",width=13,height=2,fg='black',bg='#1DC8BB',command=delete)
delete_btn.grid(row=0,column=2, padx=10,pady=10)

clear_btn=Button(btn_frame,text='CLEAR',width=13,height=2,fg='black',bg='#1DC8BB',command=clear)
clear_btn.grid(row=0,column=3,padx=10,pady=10)

####################details frame

details_frame=Frame(root,bd=4,relief=RIDGE,bg='#2A7FDB')

details_frame.place(x=600,y=80,width=750,height=600)

search_label=Label(details_frame,text='Search By',font='timesnewroman 19 bold',bg='#2A7FDB',fg='white',relief=RAISED,bd=0)
search_label.grid(row=0,column=0,padx=20,pady=10)

search_combo=ttk.Combobox(details_frame,textvariable=search,width=17,font='timesnewroman 13 bold',state='r')
search_combo['values']=('Select Option','Id','First name','Last Name','Email','Gender','Contact','Date','Adress')
search_combo.grid(row=0,column=1,padx=0,pady=10,sticky='w')

search_entry=ttk.Entry(details_frame,font='timesnewroman 12 bold')
search_entry.grid(row=0,column=2,padx=10,pady=10,sticky='w')

search_btn=Button(details_frame,text='Search',width=12,height=2,bg='white',command=search_data)
search_btn.grid(row=0,column=3,padx=0,pady=10)

showall_btn=Button(details_frame,text='Show All',width=12,height=2,bg='white',command=show_all)
showall_btn.grid(row=0,column=4,padx=2,pady=10)
##########333 table frame
table_frame=Frame(details_frame,bd=4,relief=RIDGE,bg='powder blue')

table_frame.place(x=10,y=70,width=725,height=515)
scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
student_table=ttk.Treeview(table_frame,column=('ide','fname','lname','email','gender','contact','date','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side='bottom',fill='x')
scroll_y.pack(side='right',fill='y')
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.heading('ide',text='Id')
student_table.heading('fname',text='First name')
student_table.heading('lname',text='Last name')
student_table.heading('email',text='Email')
student_table.heading('gender',text='Gender')
student_table.heading('contact',text='Contact')
student_table.heading('date',text='Date')
student_table.heading('address',text='Address')
student_table['show']='headings'

student_table.column('ide',width=90)
student_table.column('fname',width=130)
student_table.column('lname',width=130)
student_table.column('email',width=120)
student_table.column('gender',width=100)
student_table.column('contact',width=120)
student_table.column('date',width=120)
student_table.column('address',width=150)
student_table.pack(fill='both',expand=1)
# when table is created use fetch_data
fetch_data()
slider()
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7), height=5, show="headings")
con = sqlite3.connect("students.db")
con.execute("create table if not exists student ( ide integer auto_increment primary key, fname text, lname text , email text , gender text, contact text, date text, adress text)")
cuser = con.cursor()
select = cuser.execute("select *  from student")
for row in select:
    table.insert('', END, value=row)

student_table.bind('<ButtonRelease-1>',get_cursor)
root.mainloop()
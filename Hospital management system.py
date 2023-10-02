'''from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Mysql.connector
win=Tk()
win.state('zoomed')
win.config(bg='black')
#---------------------BUTTON FUNCTION--------------------------#
def pd():
    if e1.get()==""or e2.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con = Mysql.connector.connect(host="localhost",username="root",password="Jersynumber5@",database="hospital_data")
        my_cursor = con.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            nameofpatient.get(),
            dob.get(),
            patientaddress.get(),
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")
def fetch_data():
    con = Mysql.connector.connect(host="localhost",username="root",password="Jersynumber5@",database="hospital_data")
    my_cursor = con.cursor()
    my_cursor.execute('select * from hospital')
    rows = my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        con.close()
def get_data(event=''):
    cursor_row= table.focus()
    data = table.item(cursor_row)
    row = data['values']
    nameoftablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablets.set(row[3])
    issuedate.set(row[4])
    expdate.set(row[5])
    dailydose.set(row[6])
    sideeffect.set(row[7])
    nameofpatient.set(row[8])
    dob.set(row[9])
    patientaddress.set(row[10])
#----------------Prescription data---------------------#
def pre():
    txt_frme.insert(END,'Name of Tablets:\t\t\t' + nameoftablets.get() + '\n') 
    txt_frme.insert(END,'Reference No.:\t\t\t' + ref.get() + '\n')   
    txt_frme.insert(END,'Reference No.:\t\t\t' + dose.get() + '\n')
    txt_frme.insert(END,'No. of Tablets:\t\t\t' + nooftablets.get() + '\n')      
    txt_frme.insert(END,'Issue Date:\t\t\t' + issuedate.get() + '\n')   
    txt_frme.insert(END,'Exp.Date:\t\t\t' + expdate.get() + '\n') 
    txt_frme.insert(END,'Daily Dose:\t\t\t' + dailydose.get() + '\n')  
    txt_frme.insert(END,'Side Effect:\t\t\t' + sideeffect.get() + '\n')   
    txt_frme.insert(END,'Blood Pressure:\t\t\t' + bloodpressure.get() + '\n')
    txt_frme.insert(END,'Storage Device:\t\t\t' + storage.get() + '\n')   
    txt_frme.insert(END,'medication:\t\t\t' + medication.get() + '\n')
    txt_frme.insert(END,'patient Id:\t\t\t' + patientid.get() + '\n') 
    txt_frme.insert(END,'DOB:\t\t\t' + dob.get() + '\n')    
    txt_frme.insert(END,'Patient Address:\t\t\t' + patientaddress.get() + '\n') 
    
#----------------delete-----------------------#
def delete():
    con = Mysql.connector.connect(host="localhost",username="root",password="Jersynumber5@",database="hospital_data")
    my_cursor = con.cursor()
    querry = ('delete from hospital where Reference = %s')
    value = (ref.get(),)
    my_cursor.execute(querry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Deleted','patient data has been deleted')

#-----------------clear button---------------------------#
def clear():
    nameoftablets.set('')
    ref.set('')
    dose.set('')
    nooftablets.set('')
    issuedate.set('')
    expdate.set('')
    dailydose.set('')
    sideeffect.set('')
    bloodpressure.set('')
    storage.set('')
    medication.set('')
    patientid.set('')
    nameofpatient.set('')
    dob.set('')
    patientaddress.set('')
    txt_frme.delete(1.0,END)
#--------------------------exit button-----------------------#
def exit():
    confirm= messagebox.askyesno('confirmation','Are you sure you want to exit')
    if confirm>0:
        win.destroy()
        return
#heading
Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)
#frame1
frame1 = Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1580,height=310)
#label Frame For Patient info.
lf1=LabelFrame(frame1,text='Patient Information',font='ariel 10 bold',bd=10,bg='pink')
lf1.place(x=10,y=0,width=750,height=280)
#labels for patient information
Label(lf1,text='Name of Tablets',bg='pink').place(x=5,y=10)
Label(lf1,text='Reference No',bg='pink').place(x=5,y=40)
Label(lf1,text='Dose',bg='pink').place(x=5,y=70)
Label(lf1,text='No.of Tablets',bg='pink').place(x=5,y=100)
Label(lf1,text='Issue Date',bg='pink').place(x=5,y=130)
Label(lf1,text='Exp.Date',bg='pink').place(x=5,y=160)
Label(lf1,text='Daily Dose',bg='pink').place(x=5,y=190)
Label(lf1,text='Side Effect',bg='pink').place(x=5,y=220)
Label(lf1,text='Blood Pressure',bg='pink').place(x=370,y=10)
Label(lf1,text='Storage Device',bg='pink').place(x=370,y=40)
Label(lf1,text='Medication',bg='pink').place(x=370,y=70)
Label(lf1,text='Patient Id',bg='pink').place(x=370,y=100)
Label(lf1,text='Name of Patient',bg='pink').place(x=370,y=130)
Label(lf1,text='DOB',bg='pink').place(x=370,y=160)
Label(lf1,text='Patient Address',bg='pink').place(x=370,y=190)
#Text Variable for every Entry Fields
nameoftablets=StringVar()
ref=StringVar()
dose=StringVar()
nooftablets=StringVar()
issuedate=StringVar()
expdate=StringVar()
dailydose=StringVar()
sideeffect=StringVar()
bloodpressure=StringVar()
storage=StringVar()
medication=StringVar()
patientid=StringVar()
nameofpatient=StringVar()
dob=StringVar()
patientaddress=StringVar()
#Entry field for all labels
e1=Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)
e2=Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=40,width=200)
e3=Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=70,width=200)
e4=Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=130,y=100,width=200)
e5=Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=130,y=130,width=200)
e6=Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=130,y=160,width=200)
e7=Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=130,y=190,width=200)
e8=Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=130,y=220,width=200)
e9=Entry(lf1,bd=4,textvariable=bloodpressure)
e9.place(x=500,y=10,width=200)
e10=Entry(lf1,bd=4,textvariable=storage)
e10.place(x=500,y=40,width=200)
e11=Entry(lf1,bd=4,textvariable=medication)
e11.place(x=500,y=70,width=200)
e12=Entry(lf1,bd=4,textvariable=patientid)
e12.place(x=500,y=100,width=200)
e13=Entry(lf1,bd=4,textvariable=nameofpatient )
e13.place(x=500,y=130,width=200)
e14=Entry(lf1,bd=4,textvariable=dob)
e14.place(x=500,y=160,width=200)
e15=Entry(lf1,bd=4,textvariable=patientaddress )
e15.place(x=500,y=190,width=200)
#label Frame For Prescription.
lf2=LabelFrame(frame1,text='Prescription',font='ariel 10 bold',bd=10)
lf2.place(x=770,y=0,width=750,height=280)
#Textbox for Prescription
txt_frme=Text(lf2,font='impack 10 bold',width=40,height=30,bg='yellow')
txt_frme.pack(fill=BOTH)
#frame2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1580,height=250)
#button
#delete button
d_btn = Button(win,text='Delete',font='arial 15 bold',bg='brown',fg='white',bd=6,cursor='hand2',command='delete')
d_btn.place(x=0,y=600,width=270)
#prescription button
p_btn= Button(win,text='Prescription',font='arial 15 bold',bg='purple',fg='white',bd=6,cursor='hand2',command='pre')
p_btn.place(x=270,y=600,width=330)
#save prescription data
p_btn=Button(win,text='Save Prescription Data',font='arial 15 bold',bg='green',fg='white',bd=6,cursor='hand2',command=pd)
p_btn.place(x=600,y=600,width=340)
#clear button
p_btn=Button(win,text='clear',font='arial 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command='clear')
p_btn.place(x=940,y=600,width=170)
#exit button
e_btn=Button(win,text='Exit',font='arial 15 bold',bg='Red',fg='white',bd=6,cursor='hand2',command='exit')
e_btn.place(x=1110,y=600,width=170)
#Scroll Bar for Prescription data
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

table=ttk.Treeview(frame2,colums= ('not','ref','dose','nots','issd','expd','dd','sd','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)
#heading for prescription data
table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference No.')
table.heading('dose',text='Dose')
table.heading('nots',text='No of Tablets')
table.heading('issd',text='Issue Date')
table.heading('expd',text='Exp.Date')
table.heading('dd',text='Daily Dose')
table.heading('sd',text='Side Effect')
table.heading('pn',text='Patient Name')
table.heading('dob',text='DOB')
table.heading('Pa',text='Patient Address')
table['show'] = 'headings'
table.pack(fill=BOTH,expand=1)
############################
table.column('not',width=100)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()'''

import tkinter as tk
import sqlite3

# Create a SQLite database
conn = sqlite3.connect('hospital.db')
c = conn.cursor()

# Create a Patients table
c.execute('''CREATE TABLE IF NOT EXISTS Patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                diagnosis TEXT
             )''')
conn.commit()

class HospitalManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Hospital Management System")

        self.label = tk.Label(root, text="Patient Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        self.gender_label = tk.Label(root, text="Gender:")
        self.gender_label.pack()
        self.gender_entry = tk.Entry(root)
        self.gender_entry.pack()

        self.diagnosis_label = tk.Label(root, text="Diagnosis:")
        self.diagnosis_label.pack()
        self.diagnosis_entry = tk.Entry(root)
        self.diagnosis_entry.pack()

        self.add_button = tk.Button(root, text="Add Patient", command=self.add_patient)
        self.add_button.pack(pady=10)

        self.patient_listbox = tk.Listbox(root)
        self.patient_listbox.pack()

        self.view_patients()

    def add_patient(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        diagnosis = self.diagnosis_entry.get()

        if name and age and gender and diagnosis:
            c.execute("INSERT INTO Patients (name, age, gender, diagnosis) VALUES (?, ?, ?, ?)",
                      (name, age, gender, diagnosis))
            conn.commit()
            self.clear_entries()
            self.view_patients()
        else:
            tk.messagebox.showerror("Error", "Please fill in all fields.")

    def view_patients(self):
        self.patient_listbox.delete(0, tk.END)
        c.execute("SELECT * FROM Patients")
        patients = c.fetchall()
        for patient in patients:
            self.patient_listbox.insert(tk.END, f"Name: {patient[1]}, Age: {patient[2]}, Gender: {patient[3]}, Diagnosis: {patient[4]}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.diagnosis_entry.delete(0, tk.END)

if _name_ == "_main_":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()

# Close the database connection
conn.close()
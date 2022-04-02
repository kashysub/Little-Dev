from tkinter import*
from PIL import Image,ImageTk
import tkinter.font as font
import tkinter.messagebox
import datetime
import mysql.connector as sqltor
import math
mycon=sqltor.connect(host = "localhost", user="root",passwd="devesh2003",database="mysql")
if mycon.is_connected()==False:
    print("Error connecting to database")
cursor=mycon.cursor()
root=Tk()
myFont=font.Font(size=15)
def window():
    global root
    root.destroy()
    root=Tk()
    root.geometry('1800x650')
    root.title('John Deere')
    root.configure(bg="white")

def home():
    global root
    window()
    field=Button(root,text="Fields",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=fields).pack(side="top",pady=10,anchor=CENTER)
    field_operation=Button(root,text="Field Operations",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=field_operations).pack(side="top",pady=10,anchor=CENTER)
    spectator=Button(root,text="Spectate Operatios",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=spectate).pack(side="top",pady=10,anchor=CENTER)
def fields():
    global root
    window()
    create_field = Button(root,text="Create Field",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=create_fields).pack(side="top",pady=10,anchor=CENTER)
    update_field = Button(root,text="Update Field",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=update_fields).pack(side="top",pady=10,anchor=CENTER)
    delete_field = Button(root,text="Delete Field",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=delete_fields).pack(side="top",pady=10,anchor=CENTER)
def field_operations():
    global root
    window()
    create_ops = Button(root,text="Create operations and assign",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=create_op).pack(side="top",pady=10,anchor=CENTER)
    update_ops = Button(root,text="Update operations",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=update_op).pack(side='top',pady=10,anchor=CENTER)
    delete_ops = Button(root,text="Delete operations",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=delete_op).pack(side="top",pady=10,anchor=CENTER)
def spectate():
    global root
    window()
    spectated_all = Button(root,text="Spectate all ",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=spectate_all).pack(side="top",pady=10,anchor=CENTER)
    spectated_op = Button(root,text="Spectate operations",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=spectate_op).pack(side="top",pady=10,anchor=CENTER)
def create_fields():
    global root
    global e1
    global e2
    window()
    Label(root,text="Enter the field name",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e1=Entry(root)
    e1.pack(side="top",anchor=CENTER,pady=20,padx=40)
    Label(root,text="Enter Field Dimensions",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e2=Entry(root)
    e2.pack(side="top",anchor=CENTER,pady=20,padx=40)
    submit=Button(root,text="Submit",fg="black",bg="white",borderwidth=0,font=myFont,command=field_form).pack(side="top",anchor=CENTER,pady=15)
def field_form():
    name = e1.get()
    dimension=e2.get()
    sql = "Insert into Fields(name,dimensions)Values(%s,%s)"
    values=[name,dimension]
    cursor.execute(sql,values)
    mycon.commit()
    home()
def update_fields():
    global root
    window()
    Label(root,text = "Which field do you want to update?",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e1=Entry(root)
    e1.pack(side="top",anchor=CENTER,pady=20,padx=40)
    old_name = e1.get()
    Label(root,text = "Enter new name for the field",fg = "black",bg="white",pady=20,font = myFont).pack(side="top",anchor=CENTER)
    e2=Entry(root)
    e2.pack(side="top",anchor=CENTER,pady=20,padx=40)
    new_name=e2.get()
    Label(root,text = "Enter new dimensions for the field",fg = "black",bg="white",pady=20,font = myFont).pack(side="top",anchor=CENTER)
    e3=Entry(root)
    e3.pack(side="top",anchor=CENTER,pady=20,padx=40)
    new_dimensions=e3.get()
    sql="UPDATE Fields SET Name = %s WHERE name = %s"
    values=[new_name,old_name]
    cursor.execute(sql,values)
    sql="UPDATE Fields SET Dimensions = %s WHERE name = %s"
    values=[new_dimensions,new_name]
    cursor.execute(sql,values)
    mycon.commit()
    submit=Button(root,text="Submit",fg="black",bg="white",borderwidth=0,font=myFont,command=home).pack(side="top",anchor=CENTER,pady=15)
def delete_fields():
    global root
    window()
    Label(root,text = "Enter the name of the field you want to Delete",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e1= Entry(root)
    e1.pack(side="top",anchor=CENTER,pady=20,padx=40)
    name = e1.get()
    #cursor.execute("DELETE FROM Fields WHERE Name = %s"%(e1.get(),))
    mycon.commit()
    submit=Button(root,text="Submit",fg="black",bg="white",borderwidth=0,font=myFont,command=home).pack(side="top",anchor=CENTER,pady=15)
def create_op():
    global root
    window()
    Label(root,text = "Select the Field Operations",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    seed = Button(root,text="Seeding",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=seeding).pack(side="top",pady=10,anchor=CENTER)
    spray= Button(root,text="Spraying",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=spraying).pack(side='top',pady=10,anchor=CENTER)
    tillage= Button(root,text="Tillage",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=tillages).pack(side="top",pady=10,anchor=CENTER)
    harvest= Button(root,text="Harvest",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=harvests).pack(side="top",pady=10,anchor=CENTER)
def seeding():
    global root
    global Corn
    global Soybean
    global Potato
    global Cotton
    global Rice
    window()
    Label(root,text = "Select which Field to assign",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e= Entry(root)
    e.pack(side="top",anchor=CENTER,pady=20,padx=40)
    def corn():
        cursor.execute("UPDATE Fields SET Seeding = Corn WHERE Name = %s"%(e.get(),))
    def soybean():
        global e
        cursor.execute("UPDATE Fields SET Seeding = SoyBean WHERE Name = %s"%(e.get(),))
    def potato():
        global e
        cursor.execute("UPDATE Fields SET Seeding = Potato WHERE Name = %s"%(e.get(),))
    def cotton():
        global e
        cursor.execute("UPDATE Fields SET Seeding = Cotton WHERE Name = %s"%(e.get(),))
    def rice():
        global e
        cursor.execute("UPDATE Fields SET Seeding = Rice WHERE Name = %s"%(e.get(),))
        
    Label(root,text = "Select the Crop type",fg="black",bg="white",pady=10,font=myFont).pack(side="top",anchor=CENTER)
    Corn = Button(root,text="Corn",bg="white",fg="black",padx=10,pady=10,borderwidth=0,font=myFont,command=corn).pack(side="top",pady=10,anchor=CENTER)
    Soybean= Button(root,text="Soybean",bg="white",fg="black",padx=10,pady=10,borderwidth=0,font=myFont,command=soybean).pack(side='top',pady=10,anchor=CENTER)
    Potato= Button(root,text="Potato",bg="white",fg="black",padx=10,pady=10,borderwidth=0,font=myFont,command=potato).pack(side="top",pady=10,anchor=CENTER)
    Cotton= Button(root,text="Cotton",bg="white",fg="black",padx=10,pady=10,borderwidth=0,font=myFont,command=cotton).pack(side="top",pady=10,anchor=CENTER)
    Rice= Button(root,text="Rice",bg="white",fg="black",padx=10,pady=10,borderwidth=0,font=myFont,command=rice).pack(side="top",pady=10,anchor=CENTER)
    submit=Button(root,text="Submit",fg="black",bg="white",borderwidth=0,font=myFont,command=home).pack(side="top",anchor=CENTER,pady=15)
def spraying():
    global root
    window()
    Label(root,text = "Select which Field to spray",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e= Entry(root)
    e.pack(side="top",anchor=CENTER,pady=20,padx=40)
    name = e.get()
    Label(root,text = "Select spraying",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    def water():
        cursor.execute("UPDATE Fields SET Spray = water WHERE Name = %s"%(name,))
        mycon.commit()
    def pesticide():
        cursor.execute("UPDATE Fields SET Spray = Pesticide WHERE Name = %s"%(name,))
        mycon.commit()
    water = Button(root,text="Water",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=water).pack(side="top",pady=10,anchor=CENTER)
    pesticide= Button(root,text="Pesticide",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=pesticide).pack(side='top',pady=10,anchor=CENTER)
    submit=Button(root,text="Submit",fg="black",bg="white",borderwidth=0,font=myFont,command=home).pack(side="top",anchor=CENTER,pady=15)
def tillages():
    global root
    window()
    Label(root,text = "Select the Field for Tillage",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e= Entry(root)
    e.pack(side="top",anchor=CENTER,pady=20,padx=40)
    name = e.get()
    cursor.execute("Update Fields SET Tillage = True WHERE Name = %s",(name,))
    submit=Button(root,text="Submit",fg="black",bg="white",borderwidth=0,font=myFont,command=home).pack(side="top",anchor=CENTER,pady=15)
def harvests():
    global root
    window()
    Label(root,text = "Select the Field for Harvest",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    e= Entry(root)
    e.pack(side="top",anchor=CENTER,pady=20,padx=40)
    name = e.get()
    cursor.execute("Update Fields SET Harvest = True WHERE Name = %s",(name,))
    submit=Button(root,text="Submit",fg="black",bg="white",borderwidth=0,font=myFont,command=home).pack(side="top",anchor=CENTER,pady=15)
           
def update_op():
    global root
    global Corn
    global Soybean
    global Potato
    global Cotton
    global Rice
    window()
    Label(root,text = "Select the Field to update",fg="black",bg="white",pady=20,font=myFont).pack(side="top",anchor=CENTER)
    seed = Button(root,text="Seeding",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=up_seeding).pack(side="top",pady=10,anchor=CENTER)
    spray= Button(root,text="Spraying",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=up_spraying).pack(side='top',pady=10,anchor=CENTER)
    tillage= Button(root,text="Tillage",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=up_tillages).pack(side="top",pady=10,anchor=CENTER)
    harvest= Button(root,text="Harvest",bg="white",fg="black",padx=10,pady=20,borderwidth=0,font=myFont,command=up_harvests).pack(side="top",pady=10,anchor=CENTER)    
    
def delete_op():
    pass
def spectate_all():
    sql = "Select * from Fields";
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in range(0,len(data)):
        print(data[i])
def spectate_op():
    pass
    
    
home()

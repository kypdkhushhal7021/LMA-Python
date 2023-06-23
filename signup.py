import tkinter as tk
from tkinter import ttk
import subprocess
import mysql.connector
from PIL import Image, ImageTk
import runpy

hostname = 'localhost'  
username = 'root'  
password = ''  
database_name = 'LMA'  
cnc = mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database_name
)
crs = cnc.cursor()
# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO users(email, password, name)"
   "VALUES (%s, %s, %s)"
)
def sign():
    e=id_textbox.get()
    p=pass_textbox.get()
    n=id_name.get()
    data=(e,p,n)
    try:
       # Executing the SQL command
       crs.execute(insert_stmt, data)
       #print("hi")
       # Commit your changes in the database
       cnc.commit()

    except:
       # Rolling back in case of error
       cnc.rollback()

    #print("Data inserted")
    root.destroy()
    runpy.run_path("LMA login.py")
    # Closing the connection
    cnc.close()
root = tk.Tk()
root.title("Sign Up")
def home():
    print("Opening Home")
    root.destroy()
    runpy.run_path("LMA login.py")
home_button = tk.Button(root, text="Home",command=home).grid(row=1,column=2)
image = Image.open("logo.jpg")
image = image.resize((240, 180))
photo = ImageTk.PhotoImage(image)

# Create label with image
label = tk.Label(root, image=photo)
label.grid(row=2,column=2)
#Create email
id_label = ttk.Label(text="Email")
id_label.grid(row=3,column=2)

# Create a text box widget
id_t=tk.StringVar()
id_textbox = ttk.Entry(root, textvariable=id_t)
id_textbox.grid(row=4,column=2)


pass_label = ttk.Label(text="Password")
pass_label.grid(row=5,column=2)

# Create a text box widget
pass_t=tk.StringVar()
pass_textbox = ttk.Entry(root,show="*", textvariable=pass_t)
pass_textbox.grid(row=6,column=2)

id_label = ttk.Label(text="Name")
id_label.grid(row=7,column=2)

# Create a text box widget
id_t1=tk.StringVar()
id_name = ttk.Entry(root, textvariable=id_t1)
id_name.grid(row=8,column=2)


button1 = tk.Button(root, text="Sign Up", command=sign)
button1.grid(row=10,column=2)

#Extracting values from list_lang dictionary for showing in Combobox
# Start the main event loop
root.mainloop()

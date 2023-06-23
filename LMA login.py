import tkinter as tk
from tkinter import ttk
import subprocess
import mysql.connector
from PIL import Image, ImageTk
import runpy

from functools import partial


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
q="select * from users"
crs.execute(q)

table = crs.fetchall()
d=dict()
print('\n Table Data:')
for row in table:
    d[row[0]]=row[1]
    print(row[0], end=" ")
    print(row[1], end=" ")
    print(row[2], end="\n")
crs.close()
cnc.close()
#Create the main window
root = tk.Tk()

def validateLogin():
    #print(d)
    id_text=id_textbox.get()
    pass_text=pass_textbox.get()
    for row in table:
        if(id_text==row[0] and pass_text==d[row[0]]):
            print("Login Succesfull")
            root.destroy()
            runpy.run_path("index.py")
        else:
            print("Try Again")
            ttk.Label(root, text="Wrong Username/Password", font= ('Century 15 bold')).grid(row=10,column=2)





root.title('LMA')

def home():
    print("Opening Home")
    root.destroy()
    runpy.run_path("LMA login.py")
def sign():
    root.destroy()
    runpy.run_path("signup.py")
home_button = tk.Button(root, text="Home",command=home).grid(row=1,column=2)
image = Image.open("logo.jpg")
image = image.resize((240, 180))
photo = ImageTk.PhotoImage(image)

# Create label with image
label = tk.Label(root, image=photo)
label.grid(row=2,column=2)
#Create email
id_label = ttk.Label(text="Email/User ID")
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

button = tk.Button(root, text="Login", command=validateLogin)
button.grid(row=7,column=2)

or_ = ttk.Label(text="or")
or_.grid(row=8,column=2)

sign = tk.Button(root, text="Sign Up", command=sign)
sign.grid(row=9,column=2)
#validateLogin = partial(validateLogin, id_t, pass_t)


#Extracting values from list_lang dictionary for showing in Combobox
# Start the main event loop
root.mainloop()


 

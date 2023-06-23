import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from gtts import gTTS
import os 
import speech_recognition
import time
import vlc
import pyttsx3
import googletrans
import time
import re
import runpy
import mysql.connector
movies = [
        {'name': 'Guitar', 'classification': 'String instrument', 'description': 'The guitar is a fretted musical instrument that typically has six strings.\n It is usually held flat against the players body and played by strumming or plucking the strings with \nthe dominant hand, while simultaneously pressing selected strings against frets with the fingers of the opposite hand. ', 'image_path': 'Guitar.png'},
    
]

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
q="select * from products"
crs.execute(q)

table = crs.fetchall()

print('\n Table Data:')


def added_cart():
    print("Added")
    
def buy_now():
    print("Opening Buy")
    root.destroy()
    runpy.run_path("LMA login.py")

def show_buy(i):
    print(i)
    window1 = tk.Toplevel(root)
    #window1.state('zoomed') 
    #root.destroy()
    buy_button=tk.Button(window1,text="Pay Rs. 10,000").pack()






        #time_taken =end_time - start_time
        #time_t=time_taken
#contact_button.pack(side="left", padx=10)
# Create a function to display the movie details when a button is clicked.
def show_details(movie):
    # Create a new window to display the movie details.
    window = tk.Toplevel(root)
    window.title(movie[1])
    img=movie[1]
    # Load the movie poster image and resize it to 10cm x 20cm.
    with Image.open('images/'+movie[4]) as img:
        dpi = 96  # Default DPI for most screens
        new_width = 180
        new_height = 180
        resized_img = img.resize((new_width, new_height))
        image = ImageTk.PhotoImage(resized_img)
    combo_values= []
    
    # Create labels to display the movie name, genre, and description.
    name_label = tk.Label(window, text=movie[1], font=('Arial', 16, 'bold'))
    genre_label = tk.Label(window, text=f"Classification: {movie[2]}")
    description_label = tk.Label(window, text=movie[3])

    # Create a label to display the movie poster image.
    image_label = tk.Label(window, image=image)
    image_label.image = image  # Keep a reference to the image to prevent it from being garbage collected.
    print("Movie Selected",movie[1])
    m_name=movie[1]
    #m_link=movie['link']
    cart_button = tk.Button(window, text="Add to Cart",command=added_cart)
    buy_button = tk.Button(window,text="Buy Now", command=show_buy(img))
    #buy_button=tk.Button(window,text="Buy Now",command=buy_now)
    #to make combobox uneditable
    
    # Pack the labels into the window.
    image_label.pack(pady=5)
    name_label.pack(pady=5)
    genre_label.pack()
    description_label.pack()
    
    
    cart_button.pack(pady=10)
    buy_button.pack(pady=10)

    # Create the main window.
    

root = tk.Tk()
root.title('LMA')
root.state('zoomed')  # Open window in maximize mode

def home():
    print("Opening Home")
    root.destroy()
    runpy.run_path("index.py")
def open_subtitle():
    print("Logout")
    root.destroy()
    runpy.run_path("LMA login.py")


def search():
    #genre=['drama','romance','Action','Adventure','Bollywood','Crime','Horror','Mystery','Sci-fi','Thriller','Sports','Comedy']
    search_text = search_var.get()
    row = 1
    column = 0
    for button in buttons:
        if search_text.lower() in button["text"].lower():
            button.grid(row=row, column=column, padx=10, pady=10)
            column += 1
            if column > 5:
                column = 0
                row += 1
        
        else:
            button.grid_forget()

# Navigation bar
nav_frame = tk.Frame(root)
nav_frame.pack(side=tk.TOP, fill=tk.X)

home_button = tk.Button(nav_frame, text='Home',command=home)
home_button.pack(side=tk.LEFT, padx=10)

open_button = tk.Button(nav_frame, text='Logout',command=open_subtitle)
open_button.pack(side=tk.LEFT, padx=10)

search_var = tk.StringVar()
search_var.trace("w", lambda name, index, mode, search_var=search_var: search())
search_entry = ttk.Entry(nav_frame, textvariable=search_var)
search_entry.pack(side=tk.RIGHT, padx=10)
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox('all'))
# Main content
content_frame = tk.Frame(root)
content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(content_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
#canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

buttons_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=buttons_frame, anchor='nw')

canvas.bind('<Configure>', configure_canvas)

buttons=[]
rowm=1
colm=0

for row in table:
    print(row[0], end=" ")
    print(row[1], end=" ")
    print(row[2], end=" ")
    print(row[3], end=" ")
    print(row[4], end="\n")


    with Image.open('images/'+row[4]) as img:
        dpi = 96  # Default DPI for most screens
        new_width = 175
        new_height = 180
        resized_img = img.resize((new_width, new_height))
        image = ImageTk.PhotoImage(resized_img)
    id_=row[0]
    button = tk.Button(buttons_frame, image=image, text=row[1]+'\n'+row[2], font=('Arial', 10), compound='top', command=lambda row=row: show_details(row))
    button.image = image  # Keep a reference to the image to prevent it from being garbage collected.
    buttons.append(button)
    search_text = search_var.get()
    row = 1
    column = 0
    for button in buttons:
        if search_text.lower() in button["text"].lower():
            button.grid(row=row, column=column, padx=10, pady=10)
            column += 1
            if column > 5:
                column = 0
                row += 1
        
    #button.grid(row=rowm//6, column=colm%6)
    rowm=rowm+1
    colm=colm+1
    

    


crs.close()
cnc.close()
    

root.mainloop()

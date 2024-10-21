from tkinter import *
from tkinter import ttk
import math

#---------------------------------Definitions--------------------------------

#widgets = GUI elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets
#label = area widget that holds text and/or image within a window

#---------------------------------Requirements--------------------------------

#---NEED---
#Modes (Endurance)
#Gyroscope
#Speedometer
#Gear: (R, 1, 2, 3, 4)
#Fuel
#


#---WANT---



#---------------------------------Coding-------------------------------------
            
#important concepts https://docs.python.org/3/library/tkinter.html#important-tk-concepts

#start an instance of a window
window = Tk() 

#change the size
window.geometry("800x480")

#change title of window
window.title("First Program")



#----------------------------------------------------------
#icon/picture of the window (Not working when sharing)
#icon = PhotoImage(file='BAJALOGO-removebg-preview.png')
#window.iconphoto(True,icon)
#----------------------------------------------------------



img = PhotoImage(file="media/newborder2.png")

# Set the window to fullscreen
# window.attributes('-fullscreen', True)

#label ((name of the window), text = '(string)', font = ('font family'))
label = Label(window, 
              text="dashbord", 
              font =('Georgia', 40, 'bold'), 
              fg = 'green', 
              bg='#00000f', 
              relief=RAISED, 
              bd=10,
              padx=10,
              pady=20,
              image=img,
              compound=CENTER)

#pack adds label onto the window
label.pack(expand=True, anchor="center")

# Optionally, bind the Escape key to exit fullscreen mode
# window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

#background can also beinputted as a hexvalue
window.config(background = "#5cfcff") #(background = #5cfcff) -> skyblue

window.mainloop() #display the window, listen for events

#---------------------------------------------------------------------------
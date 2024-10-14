from tkinter import *
from tachometer import Tachometer  # Import the Tachometer class

# Create the main window
window = Tk()
window.geometry("800x480")
window.title("First Program")

# Create a canvas to hold the background image and tachometer
canvas = Canvas(window, width=800, height=480, bg='black')
canvas.pack(fill=BOTH, expand=True)

# Load the background image
img = PhotoImage(file="media/newborder2.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# Create and place the tachometer
tachometer = Tachometer(master=canvas, width=400, height=400)
canvas.create_window(400, 240, window=tachometer)  # Center the tachometer vertically

# Simulate RPM changes for the tachometer
rpm = 0

def update_rpm():
    global rpm
    if rpm >= 10000:
        rpm = 0
    else:
        rpm += 500  # Increment RPM
    
    tachometer.update_rpm(rpm)
    window.after(1000, update_rpm)  # Update every second

update_rpm()  # Start updating the RPM

# Start the main loop
window.mainloop()

from tkinter import *
from tachometer import Tachometer
from fuel import FuelMeter
from textedits import create_shadow_text, create_gradient_text  # Import the functions

# Create the main window
window = Tk()
window.geometry("800x480")
window.title("Dashboard")

# Create a canvas to hold the background image and tachometer
canvas = Canvas(window, width=800, height=480, bg='black')
canvas.pack(fill=BOTH, expand=True)

# Load the background image
img = PhotoImage(file="media/newborder2.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# Create the tachometer
tach = Tachometer(window)
tach.place(x=274, y=330)  # Adjust x and y as needed to position the tachometer

# Create a label for "x1000 R.P.M" with gradient effect
rpm_colors = ["#FF4500", "#FFD700"]
create_gradient_text(canvas, "x1000 R.P.M", font=("Helvetica", 12), x=590, y=350, colors=rpm_colors)

# Create the gear label with shadow effect
gear_font = ("Impact", 60)
create_shadow_text(canvas, "3", font=gear_font, x=400, y=220, shadow_offset=(4, 4), shadow_color="black", text_color="blue")

# Create the speed label with shadow effect
speed_font = ("Helvetica", 24)
create_shadow_text(canvas, "90 km/h", font=speed_font, x=600, y=240, shadow_offset=(2, 2), shadow_color="black", text_color="blue")

# Create the fuel meter and place it on the left side
fuel_meter = FuelMeter(window, width=20, height=180, bg_color='black', fg_color='green', border_color='black')
fuel_meter.place(x=56, y=155)  # Adjust the x and y as needed for the left side of the dashboard

# Start checking the fuel indicator
fuel_meter.check_fuel_indicator()

# Start the main loop
window.mainloop()

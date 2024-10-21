from tkinter import *
from tkinter import ttk
from math import cos, sin, radians
import random

# Speedometer parameters
# rpm = 1000 
# speed = 25  # mph
# temp = 75   # Celsius

rpm = 0
speed = 0
temp = 0


# Function to update the display values
def update_display():
    rpm = random.randint(0, 8000)  # Simulating RPM values
    speed = random.randint(0, 180)  # Simulating speed in km/h
    temp = random.randint(20, 120)  # Simulating temperature in Celsius

    rpm_label.config(text=f"RPM: {rpm}")
    speed_label.config(text=f"Speed: {speed} km/h")
    temp_label.config(text=f"Temp: {temp}°C")

    # Update the needle on the speedometer
    update_needle(rpm_speedometer, rpm, max_value=8000)  # RPM scale up to 8000
    update_needle(speed_speedometer, speed, max_value=180)  # Speed scale up to 180 km/h
    update_needle(temp_speedometer, temp, max_value=120)  # Temp scale up to 120°C

    main.after(50, update_display)

# Function to draw the speedometer
def draw_speedometer(canvas, label):
    canvas.create_oval(50, 50, 250, 250, outline="black", width=2)
    canvas.create_text(150, 140, text=label, font=("Helvetica", 14))

    # Draw speedometer tick marks
    for i in range(0, 181, 20):
        angle = radians(180 - i)
        x1 = 150 + 90 * cos(angle)
        y1 = 150 - 90 * sin(angle)
        x2 = 150 + 100 * cos(angle)
        y2 = 150 - 100 * sin(angle)
        canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

# Function to update the needle position based on the speed
def update_needle(canvas, value, max_value):
    angle = 180 - (value * 180 / max_value)  # Scale the value
    x2 = 150 + 90 * cos(radians(angle))
    y2 = 150 - 90 * sin(radians(angle))

    # Update needle on the canvas
    canvas.coords(canvas.needle, 150, 150, x2, y2)

# Set up tkinter window
main = Tk()
main.geometry("800x400")
main.title("WESTERN BAJA front")

# Add labels for RPM, speed, and temperature
rpm_label = Label(main, text=f"RPM: {rpm}", font=("Helvetica", 16))
rpm_label.grid(row = 0, column = 0)

speed_label = Label(main, text=f"Speed: {speed} km/h", font=("Helvetica", 16))
speed_label.grid(row = 0, column = 1)

temp_label = Label(main, text=f"Temp: {temp} °C", font=("Helvetica", 16))
temp_label.grid(row = 0, column = 2)

# Create a canvas for the speedometer
rpm_speedometer = Canvas(main, width=300, height=300)
rpm_speedometer.grid(row=1, column=0)
speed_speedometer = Canvas(main, width=300, height=300)
speed_speedometer.grid(row=1, column=1)
temp_speedometer = Canvas(main, width=300, height=300)
temp_speedometer.grid(row=1, column=2)

# Draw the speedometer
draw_speedometer(rpm_speedometer, "RPM")
draw_speedometer(speed_speedometer, "km/h")
draw_speedometer(temp_speedometer, "°C")

# Create the speedometer needle
rpm_speedometer.needle = rpm_speedometer.create_line(150, 150, 150, 60, width=4, fill='red')
speed_speedometer.needle = speed_speedometer.create_line(150, 150, 150, 60, width=4, fill='red')
temp_speedometer.needle = temp_speedometer.create_line(150, 150, 150, 60, width=4, fill='red')

# Update the display with initial values
update_display()

main.mainloop()

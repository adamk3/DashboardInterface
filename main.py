from tkinter import *
from tachometer import Tachometer
from meters import Meters  # Import the new Dashboard class
from textedits import create_shadow_text, create_gradient_text
from gear import GearDisplay
import time
import dashboard
from simulations import Speedometer

# Create the main window with dashboard border
window = Tk()
window.geometry("800x480")
window.title("Dashboard")
canvas = Canvas(window, width=800, height=480, bg='black')
canvas.pack(fill=BOTH, expand=True)
img = PhotoImage(file="media/newborder2.png")  # Border for the blue outline
canvas.create_image(0, 0, anchor=NW, image=img)

# --- Create Dashboard Widgets ---

# Tachometer (RPM Meter)
tach = Tachometer(window)
tach.place(x=100, y=30)

# Gear Display
gear_display = GearDisplay(window)
gear_display.place(x=350, y=400)
gear_display.update_gear("R", True)

# Fuel, Battery, Throttle, and Brake Meters
meter_dashboard = Meters(window)  # Instantiate the Dashboard class with meters
meter_dashboard.place(x=56, y=150)   # Position it within the main window

# --- Create Dashboard Labels ---

# Creating all the labels
speed_label, lap_label, lap_avg_label, clock_label = dashboard.create_labels(canvas)

# Ensuring clock counts down and toggling modes
dashboard.start_timer(canvas, clock_label, window)
dashboard.setup_mode_toggle(canvas, lap_label, lap_avg_label, clock_label, window)

# x1000 R.P.M label with gradient effect
create_gradient_text(canvas, "x1000 R.P.M", font=("Helvetica", 10), x=590, y=350, colors=["#FF4500", "#FFD700"])

# --- Initialize the Dashboard ---

current_speed = 0
mode_on = True

# Start checking fuel, battery, throttle, and brake levels
meter_dashboard.check_levels()

# Update tachometer RPM indicator
tach.check_rpm_indicator()

# Speedometer setup and simulation
speedometer = Speedometer(canvas, speed_label, window)
speedometer.simulate_speed_change()  # Start speed simulation

# Main loop
window.mainloop()

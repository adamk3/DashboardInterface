from tkinter import *
from tachometer import Tachometer
from meters import Meters
from textedits import create_shadow_text, create_gradient_text
from gear import GearDisplay
import dashboard
from simulations import Speedometer

# Create the main window with dashboard border
window = Tk()
window.geometry("800x480")
window.title("Dashboard")
canvas = Canvas(window, width=800, height=480, bg='black')
canvas.pack(fill=BOTH, expand=True)
img = PhotoImage(file="media/newborder2.png")
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
meter_dashboard = Meters(window)
meter_dashboard.place(x=45, y=210)

# --- Create Dashboard Labels ---

# Creating all the labels, including the new ones
(speed_label, lap_label, lap_best_label, lap_previous_label, place_label,
 car_infront_label, clock_label) = dashboard.create_labels(canvas)

# Ensuring clock counts down and toggling modes, including new labels
dashboard.start_timer(canvas, clock_label, window)
dashboard.setup_mode_toggle(canvas, lap_label, lap_best_label, lap_previous_label, 
                            place_label, car_infront_label, clock_label, window)

# x1000 R.P.M label with gradient effect
create_gradient_text(canvas, "x1000 R.P.M", font=("Helvetica", 10), x=650, y=90, colors=["#FF4500", "#FFD700"])

# --- Initialize the Dashboard ---

current_speed = 0
mode_on = True

# Start checking fuel, battery, throttle, and brake levels
meter_dashboard.check_levels()

# Update tachometer RPM indicator
tach.check_rpm_indicator()

# Speedometer setup and simulation
speedometer = Speedometer(canvas, speed_label, window)
speedometer.simulate_speed_change()

# Main loop
window.mainloop()

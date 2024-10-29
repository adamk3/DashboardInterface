from tkinter import *
from tachometer import Tachometer
from fuel import FuelMeter
from textedits import create_shadow_text, create_gradient_text
from gear import GearDisplay
import time
import dashboard
from simulations import Speedometer

#create the window with the dashboard border
window = Tk()
window.geometry("800x480")
window.title("Dashboard")
canvas = Canvas(window, width=800, height=480, bg='black')
canvas.pack(fill=BOTH, expand=True)
img = PhotoImage(file="media/newborder2.png") #Border for the blue outline
canvas.create_image(0, 0, anchor=NW, image=img)

# --- Create Dashboard Widgets ---

#Tachometer (RPM Meter)
tach = Tachometer(window)
tach.place(x=274, y=330) 

#Gear Label
gear_display = GearDisplay(window)
gear_display.place(x=350, y=135)
#Update Gear
gear_display.update_gear("R")

#Fuel Meter
fuel_meter = FuelMeter(window, width=20, height=180, bg_color='black', fg_color='green', border_color='black')
fuel_meter.place(x=56, y=155) 

# --- Create Dashboard Labels ---

speed_label, lap_label, lap_avg_label, clock_label = dashboard.create_labels(canvas) #creating all the labels

#making sure clock counts down 
dashboard.start_timer (canvas, clock_label, window) 
dashboard.setup_mode_toggle(canvas, lap_label, lap_avg_label, clock_label, window)


#x1000 R.P.M 
create_gradient_text(canvas, "x1000 R.P.M", font=("Helvetica", 10), x=590, y=350, colors=["#FF4500", "#FFD700"])


current_speed = 0
mode_on = True
    
# --- Initialize the Dashboard ---

fuel_meter.check_fuel_indicator()
tach.check_rpm_indicator()

speedometer = Speedometer(canvas, speed_label, window)
speedometer.simulate_speed_change()  # Start speed simulation

#Main loop
window.mainloop()
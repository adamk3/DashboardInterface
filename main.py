from tkinter import *
from tachometer import Tachometer
from fuel import FuelMeter
from textedits import create_shadow_text, create_gradient_text
from gear import GearDisplay
import time

#create the window with the dashboard border
window = Tk()
window.geometry("800x480")
window.title("Dashboard")
canvas = Canvas(window, width=800, height=480, bg='black')
canvas.pack(fill=BOTH, expand=True)
img = PhotoImage(file="media/newborder2.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# --- Create Dashboard Widgets ---

#Tachometer (RPM Meter)
tach = Tachometer(window)
tach.place(x=274, y=330) 

#Gear Label
gear_display = GearDisplay(window)
gear_display.place(x=350, y=150)

#Update Gear
gear_display.update_gear("R")

#Fuel Meter
fuel_meter = FuelMeter(window, width=20, height=180, bg_color='black', fg_color='green', border_color='black')
fuel_meter.place(x=56, y=155) 

# --- Create Dashboard Labels ---

#Speedometer
speed_label = canvas.create_text(600, 240, text="90 km/h", fill="#8766ed", font=("Helvetica", 24))

#x1000 R.P.M 
create_gradient_text(canvas, "x1000 R.P.M", font=("Helvetica", 10), x=590, y=350, colors=["#FF4500", "#FFD700"])

#Lap
lap_label = canvas.create_text(600, 290, text="Lap: 1", fill="#8766ed", font=("Helvetica", 24))

#Lap Average
lap_avg_label = canvas.create_text(365, 320, text="AVG: ", fill="#8766ed", font=("Helvetica", 12))

#Timer/Clock
clock_label = canvas.create_text(406, 290, text="00:00:00", fill="#8766ed", font=("Helvetica", 24))

# --- Update Labels & Widgets ---

#Update Lap
def update_lap(new_lap):
    canvas.itemconfig(lap_label, text=f"Lap: {new_lap}")

#Update Lap Average
def update_lap_avg(new_avg):
    canvas.itemconfig(lap_avg_label, text=f"AVG: {new_avg:.2f}")

#Start and update the timer
start_time = time.time()

def update_timer():
    elapsed_time = time.time() - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    time_string = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
    canvas.itemconfig(clock_label, text=time_string)
    window.after(1000, update_timer)
    
#Update Speedometer
def update_speed(new_speed):
    canvas.itemconfig(speed_label, text=f"{new_speed} km/h")
    
# Function to increment speed every 10ms, for concept
current_speed = 0
def simulate_speed_change():
    global current_speed

    current_speed += 1
    if current_speed > 200:
        current_speed = 0

    update_speed(current_speed)
    window.after(10, simulate_speed_change)

simulate_speed_change()

# --- Dashboard Mode Toggle Function ---
mode_on = True

def toggle_dashboard_mode():
    global mode_on
    if mode_on:
        canvas.itemconfig(lap_label, state='hidden')
        canvas.itemconfig(lap_avg_label, state='hidden')
        canvas.itemconfig(clock_label, state='hidden')
        mode_button.config(text="Cycle Modes (Current: )")
    else:
        canvas.itemconfig(lap_label, state='normal')
        canvas.itemconfig(lap_avg_label, state='normal')
        canvas.itemconfig(clock_label, state='normal')
        mode_button.config(text="Cycle Modes (Current: Endurance)")
    
    mode_on = not mode_on  # Toggle the mode

mode_button = Button(window, text="Cycle Modes (Current: Endurance)", command=toggle_dashboard_mode)
mode_button.place(x=600, y=435)    
    
# --- Initialize the Dashboard ---

fuel_meter.check_fuel_indicator()
tach.check_rpm_indicator()

#Start timer
update_timer()

#Main loop
window.mainloop()
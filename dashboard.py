from tkinter import Button
import time
from tkinter import Canvas

def create_labels(canvas):
    # Speedometer
    speed_label = canvas.create_text(600, 240, text="90 km/h", fill="#8766ed", font=("Helvetica", 24))
    
    # Lap
    lap_label = canvas.create_text(600, 290, text="Lap: 1", fill="#8766ed", font=("Helvetica", 24))

    # Lap Average
    lap_avg_label = canvas.create_text(365, 200, text="AVG: ", fill="#8766ed", font=("Helvetica", 12))

    # Timer/Clock
    clock_label = canvas.create_text(406, 140, text="00:00:00", fill="#8766ed", font=("Helvetica", 64))

    return speed_label, lap_label, lap_avg_label, clock_label

# Functions to update widgets
def update_lap(canvas, lap_label, new_lap):
    canvas.itemconfig(lap_label, text=f"Lap: {new_lap}")

def update_lap_avg(canvas, lap_avg_label, new_avg):
    canvas.itemconfig(lap_avg_label, text=f"AVG: {new_avg:.2f}")

def update_speed(canvas, speed_label, new_speed):
    canvas.itemconfig(speed_label, text=f"{new_speed} km/h")

# Timer Functionality
def start_timer(canvas, clock_label, window):
    start_time = 14400 #4 hours converted to seconds

    def update_timer():
        nonlocal start_time
        if start_time > 0:
            hours, rem = divmod(start_time, 3600)
            minutes, seconds = divmod(rem, 60)
            time_string = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            canvas.itemconfig(clock_label, text=time_string)
            start_time -= 1  # Decrement time by 1 second
            window.after(1000, update_timer)
        else:
            canvas.itemconfig(clock_label, text="00:00:00")  # Display zero at the end

    update_timer()


def setup_mode_toggle(canvas, lap_label, lap_avg_label, clock_label, window):
    mode_on = True

    def toggle_dashboard_mode():
        nonlocal mode_on
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

from tkinter import Button
import time
from tkinter import Canvas

def create_labels(canvas):
    # Speedometer
    speed_label = canvas.create_text(600, 240, text="90 km/h", fill="#8766ed", font=("Helvetica", 24))
    
    # Lap
    lap_label = canvas.create_text(600, 290, text="Lap: 1", fill="#8766ed", font=("Helvetica", 24))

    # Lap Best
    lap_best_label = canvas.create_text(365, 200, text="Best Lap:", fill="#8766ed", font=("Helvetica", 12))

    # Lap Previous
    lap_previous_label = canvas.create_text(365, 220, text="Previous Lap:", fill="#8766ed", font=("Helvetica", 12))

    # Place
    place_label = canvas.create_text(600, 330, text="Position: 1", fill="#FFD700", font=("Helvetica", 24))

    # Car In Front
    car_infront_label = canvas.create_text(600, 370, text="Car In Front: 2", fill="#FF6347", font=("Helvetica", 18))

    # Timer/Clock
    clock_label = canvas.create_text(406, 140, text="00:00:00", fill="#8766ed", font=("Helvetica", 64))

    return speed_label, lap_label, lap_best_label, lap_previous_label, place_label, car_infront_label, clock_label

# Functions to update widgets
def update_lap(canvas, lap_label, new_lap):
    canvas.itemconfig(lap_label, text=f"Lap: {new_lap}")

def update_lap_best(canvas, lap_best_label, new_best):
    canvas.itemconfig(lap_best_label, text=f"Best Lap: {new_best}")

def update_lap_previous(canvas, lap_previous_label, new_previous):
    canvas.itemconfig(lap_previous_label, text=f"Previous Lap: {new_previous}")

def update_place(canvas, place_label, new_position):
    canvas.itemconfig(place_label, text=f"Position: {new_position}")

def update_car_infront(canvas, car_infront_label, new_car_infront):
    canvas.itemconfig(car_infront_label, text=f"Car In Front: {new_car_infront}")

def update_speed(canvas, speed_label, new_speed):
    canvas.itemconfig(speed_label, text=f"{new_speed} km/h")

# Timer Functionality
def start_timer(canvas, clock_label, window):
    start_time = 14400  # 4 hours converted to seconds

    def update_timer():
        nonlocal start_time
        if start_time > 0:
            hours, rem = divmod(start_time, 3600)
            minutes, seconds = divmod(rem, 60)
            time_string = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            canvas.itemconfig(clock_label, text=time_string)
            start_time -= 1
            window.after(1000, update_timer)
        else:
            canvas.itemconfig(clock_label, text="00:00:00")

    update_timer()

def setup_mode_toggle(canvas, lap_label, lap_best_label, lap_previous_label, 
                      place_label, car_infront_label, clock_label, window):
    mode_on = True

    def toggle_dashboard_mode():
        nonlocal mode_on
        if mode_on:
            canvas.itemconfig(lap_label, state='hidden')
            canvas.itemconfig(lap_best_label, state='hidden')
            canvas.itemconfig(lap_previous_label, state='hidden')
            canvas.itemconfig(place_label, state='hidden')
            canvas.itemconfig(car_infront_label, state='hidden')
            canvas.itemconfig(clock_label, state='hidden')
            mode_button.config(text="Cycle Modes (Current: )")
        else:
            canvas.itemconfig(lap_label, state='normal')
            canvas.itemconfig(lap_best_label, state='normal')
            canvas.itemconfig(lap_previous_label, state='normal')
            canvas.itemconfig(place_label, state='normal')
            canvas.itemconfig(car_infront_label, state='normal')
            canvas.itemconfig(clock_label, state='normal')
            mode_button.config(text="Cycle Modes (Current: Endurance)")

        mode_on = not mode_on

    mode_button = Button(window, text="Cycle Modes (Current: Endurance)", command=toggle_dashboard_mode)
    mode_button.place(x=600, y=435)

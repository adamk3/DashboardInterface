# speedometer.py
from tkinter import Canvas

class Speedometer:
    def __init__(self, canvas: Canvas, speed_label, window):
        self.canvas = canvas
        self.speed_label = speed_label
        self.window = window
        self.current_speed = 0
        self.max_speed = 200  # Max speed limit for the simulation

    def update_speed(self, new_speed):
        """Update the speed on the canvas."""
        self.canvas.itemconfig(self.speed_label, text=f"{new_speed} km/h")

    def simulate_speed_change(self):
        """Simulate speed changes by incrementing the current speed."""
        self.current_speed += 1
        if self.current_speed > self.max_speed:
            self.current_speed = 0  # Reset to 0 once max speed is reached

        self.update_speed(self.current_speed)
        self.window.after(10, self.simulate_speed_change)  # Repeat every 10ms

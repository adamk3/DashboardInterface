import tkinter as tk
import math

class Tachometer(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.width = kwargs.get("width", 400)
        self.height = kwargs.get("height", 400)
        self.rpm = 0
        self.create_arc(50, 50, self.width-50, self.height-50, start=30, extent=300, outline="black", width=5)

        # Add labels for RPM display
        self.rpm_label = self.create_text(self.width // 2, self.height // 2, text="0 RPM", font=("Arial", 24))

        # Draw ticks
        self.draw_ticks()

    def draw_ticks(self):
        for i in range(0, 301, 30):
            angle = math.radians(i + 30)
            x_start = (self.width // 2) + (self.width // 2 - 50) * math.cos(angle)
            y_start = (self.height // 2) - (self.height // 2 - 50) * math.sin(angle)
            x_end = (self.width // 2) + (self.width // 2 - 20) * math.cos(angle)
            y_end = (self.height // 2) - (self.height // 2 - 20) * math.sin(angle)
            self.create_line(x_start, y_start, x_end, y_end, fill="black", width=2)

    def update_rpm(self, new_rpm):
        self.rpm = new_rpm
        self.itemconfig(self.rpm_label, text=f"{self.rpm} RPM")
        
        # Update the needle
        self.draw_needle()

    def draw_needle(self):
        # Calculate the needle position
        angle = math.radians(self.rpm * 300 / 10000)  # Scale RPM to fit the arc
        x_end = (self.width // 2) + (self.width // 2 - 100) * math.cos(angle)
        y_end = (self.height // 2) - (self.height // 2 - 100) * math.sin(angle)

        # Clear previous needle
        self.delete("needle")

        # Draw new needle
        self.create_line(self.width // 2, self.height // 2, x_end, y_end, fill="red", width=3, tags="needle")

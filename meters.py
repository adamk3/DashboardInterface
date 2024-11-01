from tkinter import Frame, Canvas, Label

class Meters(Frame):
    def __init__(self, parent, fuel_width=40, fuel_height=220, battery_width=20, battery_height=180, 
                 throttle_width=20, throttle_height=180, brake_width=20, brake_height=180, 
                 bg_color='black', fuel_color='green', battery_color='yellow', throttle_color='blue', brake_color='red', 
                 border_color='black', bar_border_color='gray'):
        super().__init__(parent, bg=bg_color)  # Set background color of the frame to black
        
        self.bg_color = bg_color
        self.border_color = border_color
        self.bar_border_color = bar_border_color
        
        # Create the fuel bar, with a y_offset of 10 pixels
        self.fuel_canvas = self.create_meter(fuel_width, fuel_height, fuel_color, "E", side="left", y_offset=20)
        
        # Create the battery bar with no y_offset
        self.battery_canvas = self.create_meter(battery_width, battery_height, battery_color, "E", side="left")

        # Create the throttle position bar with no y_offset
        self.throttle_canvas = self.create_meter(throttle_width, throttle_height, throttle_color, "E", side="left")

        # Create the brake position bar with no y_offset
        self.brake_canvas = self.create_meter(brake_width, brake_height, brake_color, "E", side="left")

        # Initialize levels
        self.fuel_level = 1.0
        self.battery_level = 1.0
        self.throttle_level = 0.5
        self.brake_level = 0.0

    def create_meter(self, width, height, color, label_text, side, y_offset=0):
        """Helper method to create a meter with the given attributes."""
        # Outer frame for border
        canvas_frame = Canvas(self, width=width + 12, height=height + 32, bg=self.border_color, highlightthickness=0)
        canvas_frame.pack(side=side, padx=10)
        
        # Inner canvas for the actual meter, moved up by y_offset for the fuel bar
        inner_canvas = Canvas(canvas_frame, width=width + 4, height=height + 4, bg=self.bg_color, highlightthickness=0)
        inner_canvas.place(x=6, y=26 - y_offset)

        # Draw the outer border for each bar
        inner_canvas.create_rectangle(2, 2, width + 2, height + 2, outline=self.bar_border_color, width=2)
        
        # Draw the main bar inside the border
        bar = inner_canvas.create_rectangle(4, height + 2, width, height + 2, fill=color, outline="")

        # Add reference lines at 25%, 50%, and 75%
        inner_canvas.create_line(4, height * 0.25, width, height * 0.25, fill="white", dash=(2, 2))
        inner_canvas.create_line(4, height * 0.5, width, height * 0.5, fill="white", dash=(2, 2))
        inner_canvas.create_line(4, height * 0.75, width, height * 0.75, fill="white", dash=(2, 2))
        
        # Update and place the label once the widget is packed to get correct coordinates
        self.after(10, lambda: self.place_label_below_meter(canvas_frame, label_text, color))
        
        return {'frame': canvas_frame, 'inner_canvas': inner_canvas, 'bar': bar, 'height': height, 'width': width}

    def place_label_below_meter(self, meter_frame, label_text, color):
        """Places a label below the given meter."""
        if color == 'green':
            x = meter_frame.winfo_x() + 10
            y = meter_frame.winfo_y() + meter_frame.winfo_height() - 20  # Offset below the meter
        else:
            x = meter_frame.winfo_x() + 10
            y = meter_frame.winfo_y() + meter_frame.winfo_height() + 0  # Offset below the meter
            
        label = Label(self, text=label_text, bg=self.bg_color, fg=color, font=("Helvetica", 10))
        label.place(x=x, y=y)

    def update_meter(self, meter, level):
        """Updates the specified meter bar based on level (0 to 1)."""
        bar_height = meter['height'] * level
        meter['inner_canvas'].coords(meter['bar'], 4, meter['height'] - bar_height + 2, meter['width'], meter['height'] + 2)

    def check_levels(self):
        """Checks and updates all levels periodically."""
        # Update each meter based on current levels
        self.update_meter(self.fuel_canvas, self.fuel_level)
        self.update_meter(self.battery_canvas, self.battery_level)
        self.update_meter(self.throttle_canvas, self.throttle_level)
        self.update_meter(self.brake_canvas, self.brake_level)

        # Simulate level changes for testing purposes
        self.fuel_level -= 0.005
        self.battery_level -= 0.002
        self.throttle_level = max(0, (self.throttle_level + 0.005) % 1.0)  # Loop throttle level
        self.brake_level = max(0, (self.brake_level + 0.003) % 1.0)       # Loop brake level
        
        if self.fuel_level < 0:
            self.fuel_level = 1.0
        if self.battery_level < 0:
            self.battery_level = 1.0

        # Repeat every 10ms
        self.after(10, self.check_levels)

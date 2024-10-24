from tkinter import Frame, Canvas, Label, PhotoImage

class FuelMeter(Frame):
    def __init__(self, parent, width=20, height=180, bg_color='black', fg_color='green', border_color='black'):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.border_color = border_color
        
        # Extend the frame width to accommodate the "E" label and fuel indicator
        extended_width = width + 100  # Increase width to allow for the label and image
        
        # Create a canvas with a stylish border around the fuel meter
        self.canvas = Canvas(self, width=extended_width + 10, height=self.height + 10, bg=self.border_color, highlightthickness=0)
        self.canvas.pack()

        # Create an inner canvas for the fuel meter itself (inside the border)
        self.inner_canvas = Canvas(self.canvas, width=self.width, height=self.height, bg=self.bg_color, highlightthickness=0)
        self.inner_canvas.place(x=5, y=5)

        # Create the background (empty tank)
        self.inner_canvas.create_rectangle(0, 0, self.width, self.height, fill=self.bg_color, outline="")

        # Create the fuel bar (fuel level indicator)
        self.fuel_bar = self.inner_canvas.create_rectangle(0, self.height, self.width, self.height, fill=self.fg_color, outline="")

        # Create fuel level lines at 25%, 50%, and 75%
        self.inner_canvas.create_line(0, self.height * 0.25, self.width, self.height * 0.25, fill="white", dash=(2, 2))  # 25%
        self.inner_canvas.create_line(0, self.height * 0.5, self.width, self.height * 0.5, fill="white", dash=(2, 2))   # 50%
        self.inner_canvas.create_line(0, self.height * 0.75, self.width, self.height * 0.75, fill="white", dash=(2, 2))  # 75%

        # Add a static "E" label for empty (adjusting x and y for visibility)
        self.empty_label = Label(self, text="E", bg=self.bg_color, fg='red', font=("Helvetica", 10))
        self.empty_label.place(x=self.width + 15, y=160)  # Adjust y to fit inside the frame

        # Load fuel indicator images and keep a reference
        self.fuel_indicator_on = PhotoImage(file="media/indicator_fuel_on.png")
        self.fuel_indicator_off = PhotoImage(file="media/indicator_fuel_off.png")

        # Add fuel indicator next to the fuel meter (adjusting position for visibility)
        self.indicator_label = Label(self, image=self.fuel_indicator_off, bg=self.border_color)
        self.indicator_label.place(x=self.width + 5, y=self.height - 110)  # Adjust y to fit inside the frame

        # Initialize fuel level (set to 1.0 for full)
        self.fuel_level = 1.0

    def update_fuel(self, fuel_level):
        """Updates the fuel bar and indicator based on fuel_level (0 to 1)."""
        self.fuel_level = fuel_level  # Store the current fuel level
        fuel_height = self.height * fuel_level
        self.inner_canvas.coords(self.fuel_bar, 0, self.height - fuel_height, self.width, self.height)

        # Turn the indicator on if fuel is below 25%
        if fuel_level < 0.15:
            self.indicator_label.config(image=self.fuel_indicator_on)
        else:
            self.indicator_label.config(image=self.fuel_indicator_off)

    def check_fuel_indicator(self):
        """Checks the fuel level and updates the indicator accordingly."""
        # Update the fuel meter based on the current fuel level
        self.update_fuel(self.fuel_level)

        #Simulate fuel consumption (replace this logic with actual fuel level updates)
        self.fuel_level -= 0.01  # Decreasing the fuel level over time
        if self.fuel_level < 0:
            self.fuel_level = 1.0  # Reset to full when it goes below zero for testing purposes

        # Repeat the check every 1000ms (1 second)
        self.after(10, self.check_fuel_indicator)  # Calls itself again after 1 second

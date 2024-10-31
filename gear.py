from tkinter import Frame, Label, PhotoImage

class GearDisplay(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(width=200, height=100, bg='black')  # Adjust size and background as needed
        
        # Load the ON and OFF images for Forward (F) and Reverse (R) gears
        self.gear_images = {
            'F_ON': PhotoImage(file="media/Gear_F_ON.png"),
            'F_OFF': PhotoImage(file="media/Gear_F_OFF.png"),
            'R_ON': PhotoImage(file="media/Gear_R_ON.png"),
            'R_OFF': PhotoImage(file="media/Gear_R_OFF.png")
        }

        # Create a frame for gear indicators
        self.gear_frame = Frame(self, bg='black')
        self.gear_frame.pack()

        # Create labels to display the current gear images
        self.f_label = Label(self.gear_frame, bg='black')
        self.r_label = Label(self.gear_frame, bg='black')
        
        # Pack the labels side by side
        self.f_label.pack(side='left', padx=5)  # Padding for spacing
        self.r_label.pack(side='left', padx=5)  # Padding for spacing

        # Track the current gear state and initialize with 'F' in OFF state
        self.current_gear = 'F'
        self.is_on = False
        self.update_gear(self.current_gear, self.is_on)

    def update_gear(self, gear, is_on):
        """Updates the displayed gear image based on the gear ('F' or 'R') and the state (ON/OFF)."""
        # Set current gear and ON/OFF state
        self.current_gear = gear
        self.is_on = is_on

        # Update Forward gear image
        forward_image_key = f"F_{'ON' if self.is_on and gear == 'F' else 'OFF'}"
        if forward_image_key in self.gear_images:
            self.f_label.config(image=self.gear_images[forward_image_key])

        # Update Reverse gear image
        reverse_image_key = f"R_{'ON' if self.is_on and gear == 'R' else 'OFF'}"
        if reverse_image_key in self.gear_images:
            self.r_label.config(image=self.gear_images[reverse_image_key])

    def toggle_gear_state(self):
        """Toggles the ON/OFF state of the current gear."""
        self.is_on = not self.is_on
        self.update_gear(self.current_gear, self.is_on)

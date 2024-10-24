# gear.py
from tkinter import Frame, Label, PhotoImage

class GearDisplay(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(width=100, height=100, bg='black')  # Adjust size and background as needed
        
        #Load the Gears
        self.gear_images = {
            '1': PhotoImage(file="media/Gear1.png"),
            '2': PhotoImage(file="media/Gear2.png"),
            '3': PhotoImage(file="media/Gear3.png"),
            '4': PhotoImage(file="media/Gear4.png"),
            '5': PhotoImage(file="media/Gear5.png"),
            'N': PhotoImage(file="media/GearN.png"),
            'R': PhotoImage(file="media/GearR.png")
        }

        # Create a label to display the current gear image
        self.gear_label = Label(self, bg='black')
        self.gear_label.pack()

        # Initialize with gear 'N' (neutral) by default
        self.update_gear('N')

    def update_gear(self, gear):
        """Updates the displayed gear based on the given gear ('1', '2', '3', '4', '5', 'N', 'R')."""
        if gear in self.gear_images:
            self.gear_label.config(image=self.gear_images[gear])
        else:
            print(f"Invalid gear: {gear}")

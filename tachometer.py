from tkinter import Canvas, Frame

class Tachometer(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(width=264, height=42, bg='black')  # Increase height to make room for labels

        # Create a canvas for the progress bar
        self.canvas = Canvas(self, width=264, height=42, bg='black', highlightthickness=0)
        self.canvas.pack()

        # Draw the progress bar background
        self.canvas.create_rectangle(0, 20, 264, 42, outline='', fill='black')  # Adjust Y positions to fit

        # Create tick marks and labels (1 - 5) to represent the RPMs
        self.draw_ticks()

        # Store current RPM progress (from 0 to 1)
        self.rpm_level = 0.0

    def draw_ticks(self):
        tick_positions = [0, 66, 132, 198, 264]  # Positions for tick marks (labels 1 - 5)
        labels = ['1', '2', '3', '4', '5']

        # Add padding for the first and last labels
        text_offsets = [5, 0, 0, 0, -5]  # Shift the '1' slightly right, '5' slightly left

        for i, pos in enumerate(tick_positions):
            # Draw vertical tick marks on the bar
            self.canvas.create_line(pos, 20, pos, 42, fill='white', width=2)

            # Adjust the label positions for padding at the edges
            label_x = pos + text_offsets[i]

            # Draw labels directly on the canvas above the progress bar
            self.canvas.create_text(label_x, 10, text=labels[i], fill='white', font=("Helvetica", 10))  # Set Y to 10 for above bar

    def update_rpm(self, rpm_level):
        """
        Updates the RPM meter based on the rpm_level (a value from 0 to 1).
        1 represents the maximum RPM (5000), and 0 represents idle RPM (1000).
        """
        self.rpm_level = rpm_level  # Store the current RPM level
        self.update_progress(rpm_level)

    def update_progress(self, progress):
        """Updates the progress bar with the current RPM level."""
        # Clear previous progress
        self.canvas.delete("progress")

        total_lines = 60  # Number of lines in the bar
        line_spacing = 264 / total_lines  # Space between lines
        filled_lines = int(progress * total_lines)  # How many lines to fill

        for i in range(filled_lines):
            start_x = i * line_spacing
            self.canvas.create_rectangle(start_x, 20, start_x + (line_spacing - 2), 42, fill='yellow', outline='', tags="progress")

    def check_rpm_indicator(self):
        """
        Continuously checks and updates the RPM meter, simulating RPM changes.
        Replace this logic with actual RPM data if available.
        """
        # Simulate RPM increase or decrease (replace this logic with actual RPM data)
        self.rpm_level += 0.01  # Increase RPM level for testing
        if self.rpm_level > 1:
            self.rpm_level = 0.0  # Reset to idle when it reaches max RPM

        # Update the RPM meter with the current level
        self.update_rpm(self.rpm_level)

        # Repeat the check every 100ms (0.1 second)
        self.after(100, self.check_rpm_indicator)  # Calls itself again after 100ms

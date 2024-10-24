from tkinter import Canvas

# This class exists to help us create sophisticated styling for the text on the dashboard.

def create_gradient_text(canvas: Canvas, text: str, font: tuple, x: int, y: int, colors: list):
    """
    Creates a gradient effect text on the given canvas.
    """
    steps = len(colors)
    for i, color in enumerate(colors):
        offset = i * 2
        canvas.create_text(x, y + offset, text=text, fill=color, font=font)

def create_shadow_text(canvas: Canvas, text: str, font: tuple, x: int, y: int,
                       shadow_offset: tuple = (2, 2), shadow_color: str = '#555555', text_color: str = 'blue', glow_radius: int = 3):
    """
    Creates a faint shadow effect text with a subtle glow on the given canvas.
    """

    # Create multiple layers of shadow to simulate a glow effect
    for i in range(glow_radius, 0, -1):
        offset_x = shadow_offset[0] * (i / glow_radius)
        offset_y = shadow_offset[1] * (i / glow_radius)
        # Draw shadow at gradually reduced offsets to create a subtle glow
        canvas.create_text(x + offset_x, y + offset_y, text=text, fill=shadow_color, font=font)
    
    # Draw the main text over the shadow
    canvas.create_text(x, y, text=text, fill=text_color, font=font)
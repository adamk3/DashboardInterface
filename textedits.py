from tkinter import Canvas

# This class exists to help us create sophisticated styling for the text on the dashboard.


def create_gradient_text(canvas: Canvas, text: str, font: tuple, x: int, y: int, colors: list):
    """
    Creates a gradient effect text on the given canvas.
    
    Parameters:
    - canvas: The canvas to draw on.
    - text: The text to be displayed.
    - font: The font properties of the text.
    - x: The x-coordinate for the text.
    - y: The y-coordinate for the text.
    - colors: A list of colors for the gradient effect.
    """
    steps = len(colors)
    for i, color in enumerate(colors):
        offset = i * 2
        canvas.create_text(x, y + offset, text=text, fill=color, font=font)

def create_shadow_text(canvas: Canvas, text: str, font: tuple, x: int, y: int,
                       shadow_offset: tuple = (4, 4), shadow_color: str = 'black', text_color: str = 'blue'):
    """
    Creates shadow effect text on the given canvas.
    
    Parameters:
    - canvas: The canvas to draw on.
    - text: The text to be displayed.
    - font: The font properties of the text.
    - x: The x-coordinate for the text.
    - y: The y-coordinate for the text.
    - shadow_offset: The offset for the shadow effect.
    - shadow_color: The color of the shadow.
    - text_color: The color of the main text.
    """
    canvas.create_text(x + shadow_offset[0], y + shadow_offset[1], text=text, fill=shadow_color, font=font)
    canvas.create_text(x, y, text=text, fill=text_color, font=font)

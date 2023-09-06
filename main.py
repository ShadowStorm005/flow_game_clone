import tkinter as tk
import colorama

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Flow game")

# Set the window dimensions
screen_width = "800"
screen_height = "600"
window.geometry(f"{screen_width}x{screen_height}")  # Width x Height

def button_click(row, col):
    selected_button = buttons[row][col]
    if selected_button["relief"] == tk.RAISED:
        selected_button.configure(relief=tk.SUNKEN)
    else:
        selected_button.configure(relief=tk.RAISED)
    print(f"Button clicked at row {row+1}, column {col+1}")

colors = [colorama.Back.BLUE, colorama.Back.CYAN, colorama.Back.GREEN, colorama.Back.LIGHTBLUE_EX, colorama.Back.LIGHTGREEN_EX, colorama.Back.LIGHTMAGENTA_EX, colorama.Back.LIGHTRED_EX, colorama.Back.LIGHTYELLOW_EX, colorama.Back.MAGENTA, colorama.Back.RED, colorama.Back.YELLOW]

def select_color():
    return colors.pop(0)
    
def generate_color_selecter(how_many_colors,button_width=10,button_height=5):
    if how_many_colors <= 5:
        colums = 1
    elif 5 < how_many_colors <= 10:
        colums = 2
    elif 10 < how_many_colors <= 15:
        colums = 3
    rows = how_many_colors // colums
    select_color_frame = tk.Frame(window, width=colums*button_width, height=rows*button_height)
    select_color_frame.pack(side="right", pady=10, padx=10)
    for row in range(rows):
        button_row = []
        for col in range(colums):
            button = tk.Button(select_color_frame, text=" ", background=["red", "blue", "yellow", "magenta", "purple", "pink", "green"].pop(0), relief=tk.RAISED, width=button_width, height=button_height, command=lambda r=row,c=col: button_click(r, c))
            button.grid(row=row,column=col)
            button_row.append(button)
        buttons.append(button_row)
    
    window.update()
    select_color_frame_width = select_color_frame.winfo_width()
    select_color_frame_height = select_color_frame.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - select_color_frame_width) // 2
    y = (screen_height - select_color_frame_height) // 2
    window.geometry(f"{select_color_frame_width}x{select_color_frame_height}+{x}+{y}")

# Create a grid of buttons
buttons = []
def generate_gridd_buttons(colums,rows,button_width=10,button_height=5):
    # Create a frame to hold the grid
    game_board_frame = tk.Frame(window, width=colums*button_width, height=rows*button_height)
    game_board_frame.pack(pady=10, padx=10)
    for row in range(rows):
        button_row = []
        for col in range(colums):
            button = tk.Button(game_board_frame, text=" ", relief=tk.RAISED, width=button_width, height=button_height, command=lambda r=row, c=col: button_click(r, c))
            button.grid(row=row, column=col)
            button_row.append(button)
        buttons.append(button_row)

# Center the frame within the window
    window.update()  # Update the window to calculate the frame size
    game_board_frame_width = game_board_frame.winfo_width()
    game_board_frame_height = game_board_frame.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - game_board_frame_width) // 2
    y = (screen_height - game_board_frame_height) // 2
    window.geometry(f"{game_board_frame_width}x{game_board_frame_height}+{x}+{y}")

if __name__ == "__main__":
    generate_gridd_buttons(5,5)
    generate_color_selecter(5)
    # Start the main event loop
    window.mainloop()
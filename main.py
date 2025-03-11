import tkinter as tk
from routine import routine  # Import routine data

# Function to display the routine
def show_routine(day):
    activity_list.delete(0, tk.END)  # Clear the list before adding new items
    for time, activity in routine[day]:
        activity_list.insert(tk.END, f"{time}: {activity}")

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Graphical interface
window = tk.Tk()
window.title("MyDailyFlow")

# Center the window
center_window(window, 600, 400)

# Buttons for the days of the week
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

days_of_week = ["Segunda-feira", "Terça-feira", "Quarta-feira"]
for day in days_of_week:
    button = tk.Button(
        button_frame,
        text=day,
        command=lambda d=day: show_routine(d),
        bg="#4CAF50",  # Green background
        fg="white",    # White text
        font=("Arial", 12),
        padx=10,
        pady=5
    )
    button.pack(side=tk.LEFT, padx=5)

# Activity list with scrollbar
list_frame = tk.Frame(window)
list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

activity_list = tk.Listbox(
    list_frame,
    width=60,
    height=20,
    yscrollcommand=scrollbar.set,
    font=("Arial", 10))
activity_list.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=activity_list.yview)

# Run the application
window.mainloop()
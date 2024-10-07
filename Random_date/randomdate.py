import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime, timedelta

# Function to generate a random date
def generate_random_date():
    # Get the current date
    today = datetime.today()

    # Generate a random number of days between 0 and some large number of days in the past
    random_days = random.randint(0, 365*100)  # Random days within the past 100 years

    # Subtract random number of days from today to get the random past date
    random_date = today - timedelta(days=random_days)
    
    # Format the date as YYYY-MM-DD
    formatted_date = random_date.strftime('%Y-%m-%d')

    # Show the generated random date in a message box
    messagebox.showinfo("Random Date", f"Random Date: {formatted_date}")

# Setting up the GUI window
window = tk.Tk()
window.title("Random Date Generator")
window.geometry("300x150")

# Label for instructions
label = tk.Label(window, text="Click the button to generate a random date!")
label.pack(pady=20)

# Button to generate random date
generate_button = tk.Button(window, text="Generate Date", command=generate_random_date)
generate_button.pack(pady=10)

# Run the GUI event loop
window.mainloop()

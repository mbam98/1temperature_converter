import tkinter as tk

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    fahrenheit = float(ent_temperature.get())
    celsius = (fahrenheit - 32) * 5 / 9
    lbl_result["text"] = f"{celsius:.2f} \N{DEGREE CELSIUS}"

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create a frame for the entry and Fahrenheit label
frm_entry = tk.Frame(master=window)

# Entry widget for Fahrenheit temperature
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Label for Fahrenheit symbol
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Arrange entry and label in the frame
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Button to convert temperature
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)

# Label to display Celsius result
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Arrange widgets in the window
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()

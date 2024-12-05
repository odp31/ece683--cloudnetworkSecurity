import RPi.GPIO as GPIO
import tkinter as tk
import threading

# define GPIO pins
input_pin = 18
output_pin = 23

# set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN)
GPIO.setup(output_pin, GPIO.OUT)

# create GUI window
window = tk.TK()
window.title("GPIO Control")

# create label to display input status
input_lable = tk.Label(window, text="Input: ")
intput_label.pack()

# create button to toggle output
output_button = tk.Button(window, text="Toggle Output", command=lambda: GPIO.output(output_pin, not GPIO.input(output_pin)))
output_button.pack()

# create an exit button
exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack()

# function to update input status label
def update_input_label():
  input_status = "HIGH" if GPIO.input(input_pin) else "LOW"
  input_label.config(text="Input: " + input_status)
  window.after(100, update_input_label)

# start input status update loop
update_input_label()

# start GUI event loop
window.mainloop()

# keep GPIO pins configured after GUI closes
GPIO.cleanup()

import machine
import time

# Define GPIO pins
input_pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
output_pin = machine.Pin(27, machine.Pin.OUT)

def read_input():
    return input_pin.value()

def toggle_output():
    output_pin.value(not output_pin.value())

while True:
    input_state = read_input()
    print(f"Input: {'HIGH' if input_state else 'LOW'}")

    user_input = input("Enter 't' to toggle output: ")
    if user_input.lower() == 't':
        toggle_output()

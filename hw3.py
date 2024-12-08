import machine
import time

# Define GPIO pins
button_pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
led_pin = machine.Pin(27, machine.Pin.OUT)

# Debounce time
debounce_time = 0.2

# Initial LED state
led_state = False

def button_callback(pin):
    global led_state
    # Debounce the button press
    time.sleep(debounce_time)
    if pin.value() == 0:
        led_state = not led_state
        led_pin.value(led_state)

# Set up the button interrupt
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

while True:
    #  can add other functionalities here, such as logging or printing the LED state
    pass
